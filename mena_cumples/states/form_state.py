import reflex as rx


class FormBaseState(rx.State):
    # Variables del estado base
    child_name: str = ""
    child_age: str = ""
    birth_date: str = ""
    birth_time: str = ""
    selected_food_option: str = ""
    pizza_selected: dict = {}
    rosca_selected: dict = {}
    total_pizza_rosca = 0
    drink_selected: dict = {}  # Nuevo diccionario para bebidas
    total_drinks = 0  # Nuevo total para bebidas
    extra_selected: str = ""
    selected_bakery_option: str = ""
    observation_selected: str = ""
    menu_number: str = ""
    menu_selection: str = ""
    conditions_acepted: bool = False
    show_alert: bool = False
    update_trigger: int = 0
    alert_message: str = ""
    alert_type:str=""
    max_allowed_pizza_rosca: int = 3  # Inicializado a 0 por defecto
    max_allowed_drinks: int = 4  # Nuevo límite para bebidas
    selected_pack: str = ""  # Nuevo campo para almacenar el pack seleccionado

    def select_pack(self, pack_type: str):
        self.selected_pack = pack_type
        self.max_allowed_pizza_rosca = self.set_max_allowed(pack_type)
        self.max_allowed_drinks = self.set_max_allowed_drinks(pack_type)
        # Forzar una actualización del estado
        self.update_trigger += 1
        print(f"Pack seleccionado: {self.selected_pack}, Máximo permitido pizzas/roscas: {self.max_allowed_pizza_rosca}, Máximo permitido bebidas: {self.max_allowed_drinks}")

    def set_max_allowed_drinks(self, pack_type: str) -> int:
        if pack_type == "Pack_15":
            return 4
        elif pack_type == "Pack_20":
            return 5
        elif pack_type == "Pack_25":
            return 8
        elif pack_type == "Pack_30":
            return 10
        else:
            return 4

    def update_drink_selected(self, drink_type, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        
        new_drink_selected = self.drink_selected.copy()
        new_drink_selected[drink_type] = value

        # Calcular el nuevo total
        new_total = sum(new_drink_selected.values())
        
        if new_total > self.max_allowed_drinks:
            self.show_alert_dialog(f"No puedes seleccionar más de {self.max_allowed_drinks} bebidas.")
        else:
            self.drink_selected = new_drink_selected
            self.calculate_total_drinks()

    def calculate_total_drinks(self):
        self.total_drinks = sum(self.drink_selected.values())

    # Funciones para mostrar y cerrar el diálogo de alerta
    def show_alert_dialog(self, message: str, alert_type: str = "pizzas_roscas"):
        self.show_alert = True
        self.alert_message = message
        self.alert_type = alert_type

    def close_alert_dialog(self):
        self.show_alert = False

    def update_pizza_selected(self, pizza_type, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        
        new_pizza_selected = self.pizza_selected.copy()
        new_pizza_selected[pizza_type] = value

        # Calcular el nuevo total
        new_total = sum(new_pizza_selected.values()) + sum(self.rosca_selected.values())
        
        if new_total > self.max_allowed_pizza_rosca:
            self.show_alert_dialog(f"No puedes seleccionar más de {self.max_allowed_pizza_rosca} pizzas o roscas.", "pizzas_roscas")
        else:
            self.pizza_selected = new_pizza_selected
            self.calculate_total()

    def update_rosca_selected(self, rosca_type, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        
        new_rosca_selected = self.rosca_selected.copy()
        new_rosca_selected[rosca_type] = value

        # Calcular el nuevo total
        new_total = sum(self.pizza_selected.values()) + sum(new_rosca_selected.values())
        
        if new_total > self.max_allowed_pizza_rosca:
            self.show_alert_dialog(f"No puedes seleccionar más de {self.max_allowed_pizza_rosca} pizzas o roscas.", "pizzas_roscas")
        else:
            self.rosca_selected = new_rosca_selected
            self.calculate_total()

    def calculate_total(self):
        self.total_pizza_rosca = sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())

    def update_drink_selected(self, drink_type, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        
        new_drink_selected = self.drink_selected.copy()
        new_drink_selected[drink_type] = value

        # Calcular el nuevo total
        new_total = sum(new_drink_selected.values())
        
        if new_total > self.max_allowed_drinks:
            self.show_alert_dialog(f"No puedes seleccionar más de {self.max_allowed_drinks} bebidas.", "drinks")
        else:
            self.drink_selected = new_drink_selected
            self.calculate_total_drinks()

    def calculate_total_drinks(self):
        self.total_drinks = sum(self.drink_selected.values())

    # Actualización de campos genérica
    def update_field(self, field, value):
        if hasattr(self, field):
            setattr(self, field, value)
        else:
            raise AttributeError(f"Field {field} does not exist in FormBaseState.")
        
    def handle_button_click(self):
        if self.conditions_acepted:
            return rx.redirect("/contact_form_page")
        else:
            return rx.window_alert("Por favor, acepta las condiciones antes de continuar.")
        
    def set_birth_time(self, new_birth_time):
        self.birth_time = new_birth_time

    # Recopilar datos del estado actual
    def collect_data(self):
        """Función para recopilar datos del estado actual en un diccionario."""
        return {
            "child_name": self.child_name,
            "child_age" : self.child_age,
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "selected_food_option": self.selected_food_option,
            "pizza_selected": self.pizza_selected,
            "rosca_selected": self.rosca_selected,
            "drink_selected": self.drink_selected,
            "extra_selected": self.extra_selected,
            "selected_bakery_option": self.selected_bakery_option,
            "observation_selected": self.observation_selected,
            "menu_number": self.menu_number,
            "menu_selection": self.menu_selection,
        }

    def generate_whatsapp_message(self, pack_name, price, include_tortillas=False):
        data = self.collect_data()
        message = (
            f"Fecha: {data['birth_date']}\n"
            f"Hora: {data['birth_time']}\n"
            f"Cumpleaños de: {data['child_name']} edad {data['child_age']}\n\n"
            f"{pack_name}\n\n"
            "Los packs de cumpleaños incluyen patatas, palomitas, bollería/galletas y frutos secos.\n\n"
        )
        if include_tortillas:
            message += "+ 2 TORTILLAS DE PATATAS INCLUIDAS\n\n"
        message += f"{data['selected_food_option']}\n\n"
        
        # Formatear pizzas seleccionadas
        if data.get('pizza_selected') and any(data['pizza_selected'].values()):
            message += "PIZZAS:\n"
            for pizza_type, quantity in data['pizza_selected'].items():
                if quantity > 0:
                    message += f"{pizza_type}: {quantity}\n"
            message += "\n"
        
        # Formatear roscas seleccionadas
        if data.get('rosca_selected') and any(data['rosca_selected'].values()):
            message += "ROSCAS:\n"
            for rosca_type, quantity in data['rosca_selected'].items():
                if quantity > 0:
                    message += f"{rosca_type}: {quantity}\n"
            message += "\n"
        
        # Formatear bebidas seleccionadas
        if data.get('drink_selected') and any(data['drink_selected'].values()):
            message += "BEBIDAS:\n"
            for drink_type, quantity in data['drink_selected'].items():
                if quantity > 0:
                    message += f"{drink_type}: {quantity}\n"
            message += "\n"
        
        # Formatear extras seleccionados
        if data.get('extra_selected'):
            message += f"EXTRAS:\n{data['extra_selected']}\n\n"
        
        message += (
            f"REPOSTERÍA:\n{data['selected_bakery_option']}\n\n"
            f"OBSERVACIONES:\n{data['observation_selected']}"
        )

        # Formatear el mensaje para WhatsApp
        message = message.replace(" ", "%20").replace("\n", "%0A")
        phone_number = '34952520965'
        whatsapp_url = f"https://wa.me/{phone_number}?text={message}"
        return rx.call_script(f"window.location.href = '{whatsapp_url}'")
    
    # Funciones para enviar el WhatsApp según el pack seleccionado
    def send_whatsapp_message(self):
        if self.selected_pack == "Pack_15":
            return self.generate_whatsapp_message("PACK DE 15 PERSONAS--90€", 90)
        elif self.selected_pack == "Pack_20":
            return self.generate_whatsapp_message("PACK DE 20 PERSONAS--120€", 120)
        elif self.selected_pack == "Pack_25":
            return self.generate_whatsapp_message("PACK DE 25 PERSONAS--150€", 150, include_tortillas=True)
        elif self.selected_pack == "Pack_30":
            return self.generate_whatsapp_message("PACK DE 30 PERSONAS--180€", 180, include_tortillas=True)

    # Método para establecer el máximo permitido de pizzas y roscas
    def set_max_allowed(self, pack_type: str) -> int:
        if pack_type == "Pack_15":
            return 3
        elif pack_type == "Pack_20":
            return 4
        elif pack_type == "Pack_25":
            return 4
        elif pack_type == "Pack_30":
            return 5
        else:
            return 3

# Función para la selección de pizzas y roscas con inputs pequeños (1 dígito)
def seleccion_pizzas(pizza_title, pizza_description, pizza_selected_values, rosca_selected_values, max_allowed):
    pizza_types = ["Margarita", "Prosciutto", "Salchicha", "Pepperoni", "Atún"]
    rosca_types = ["Mixta", "Atún", "Lomo", "Catalana"]

    # Ensure pizza_selected_values is a dictionary
    if not isinstance(pizza_selected_values, dict):
        pizza_selected_values = {pizza_type: 0 for pizza_type in pizza_types}

    # Ensure rosca_selected_values is a dictionary
    if not isinstance(rosca_selected_values, dict):
        rosca_selected_values = {rosca_type: 0 for rosca_type in rosca_types}

    # Filtrar las pizzas seleccionadas que tienen un valor mayor que 0
    filtered_pizza_inputs = [
        rx.hstack(
            rx.input(
                placeholder="0",
                value=str(pizza_selected_values.get(pizza_type, 0)),
                on_change=lambda new_value, pizza_type=pizza_type: FormBaseState.update_pizza_selected(pizza_type, new_value),
                max_length=1,
                type="number",
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},
            ),
            rx.text(pizza_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for pizza_type in pizza_types if pizza_selected_values.get(pizza_type, 0) > 0
    ]

    # Filtrar las roscas seleccionadas que tienen un valor mayor que 0
    filtered_rosca_inputs = [
        rx.hstack(
            rx.input(
                placeholder=f"0",  # Placeholder for a single digit
                value=str(rosca_selected_values.get(rosca_type, 0)),
                on_change=lambda new_value, rosca_type=rosca_type: FormBaseState.update_rosca_selected(rosca_type, new_value),
                max_length=1,  # Restrict to 1 character (single digit)
                type="number",  # Ensure it's a number
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},  # Smaller width for single-digit input
            ),
            rx.text(rosca_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for rosca_type in rosca_types if rosca_selected_values.get(rosca_type, 0) > 0
    ]

    return rx.vstack(
        rx.text(pizza_title, weight="bold"),
        rx.text(pizza_description, style={"font_style": "italic", "font_size": "16px"}),
        rx.hstack(
            rx.vstack(
                rx.text("Pizzas", weight="bold"),
                *filtered_pizza_inputs,
                align_items="start",
                margin_right="20px"
            ),
            rx.vstack(
                rx.text("Roscas", weight="bold"),
                *filtered_rosca_inputs,
                align_items="start"
            ),
            justify_content="space-between"
        ),
        margin_top="20px"
    )