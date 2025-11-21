import reflex as rx
from typing import Dict
from urllib.parse import quote

class FormBaseState(rx.State):
    """Estado base para el formulario de packs de cumpleaños."""

    # Variables de estado
    child_name: str = ""
    child_age: str = ""
    birth_date: str = ""
    birth_time: str = ""
    selected_food_option: str = ""
    butter_on_sandwiches: bool = False
    pizza_selected: Dict[str, int] = {}
    rosca_selected: Dict[str, int] = {}
    total_pizza_rosca: int = 0
    drink_selected: Dict[str, int] = {}
    total_drinks: int = 0
    extra_selected: str = ""
    selected_bakery_option: str = ""
    observation_selected: str = ""
    menu_number: str = ""
    menu_selection: str = ""
    show_alert: bool = False
    update_trigger: int = 0
    alert_message: str = ""
    alert_type: str = ""
    max_allowed_pizza_rosca: int = 3
    max_allowed_drinks: int = 4
    selected_pack: str = ""

    # Límites por pack
    PACK_PIZZA_ROSCA_LIMITS = {
        "Pack_15": 3,
        "Pack_20": 4,
        "Pack_25": 4,
        "Pack_30": 5,
    }
    PACK_DRINK_LIMITS = {
        "Pack_15": 4,
        "Pack_20": 5,
        "Pack_25": 8,
        "Pack_30": 10,
    }

    @rx.event
    def select_pack(self, pack_type: str):
        """Selecciona el pack y reinicia las selecciones."""
        self.selected_pack = pack_type
        self.max_allowed_pizza_rosca = self.PACK_PIZZA_ROSCA_LIMITS.get(pack_type, 3)
        self.max_allowed_drinks = self.PACK_DRINK_LIMITS.get(pack_type, 4)
        self.pizza_selected.clear()
        self.rosca_selected.clear()
        self.drink_selected.clear()
        self.total_pizza_rosca = 0
        self.total_drinks = 0
        self.update_trigger += 1

    @rx.event
    def show_alert_dialog(self, message: str, alert_type: str = "pizzas_roscas"):
        """Muestra un diálogo de alerta."""
        self.show_alert = True
        self.alert_message = message
        self.alert_type = alert_type

    @rx.event
    def reset_alert(self):
        """Oculta el diálogo de alerta."""
        self.show_alert = False
        self.alert_message = ""

    @rx.event
    def update_pizza_selected(self, pizza_type: str, value: str):
        """Actualiza la selección de pizzas."""
        new_value = int(value) if str(value).isdigit() else 0
        old_value = self.pizza_selected.get(pizza_type, 0)

        self.pizza_selected[pizza_type] = new_value # Actualizar temporalmente
        new_total = sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())

        if new_total > self.max_allowed_pizza_rosca:
            self.pizza_selected[pizza_type] = old_value # Revertir al valor antiguo
            self.show_alert_dialog(
                f"No puedes seleccionar más de {self.max_allowed_pizza_rosca} pizzas o roscas en total. "
                f"Tu selección actual es {sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())}.",
                "pizzas_roscas"
            )
            self.calculate_total()
        else:
            self.calculate_total() # Calcular con el nuevo valor

    @rx.event
    def update_rosca_selected(self, rosca_type: str, value: str):
        """Actualiza la selección de roscas."""
        new_value = int(value) if str(value).isdigit() else 0
        old_value = self.rosca_selected.get(rosca_type, 0)

        self.rosca_selected[rosca_type] = new_value # Actualizar temporalmente
        new_total = sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())

        if new_total > self.max_allowed_pizza_rosca:
            self.rosca_selected[rosca_type] = old_value # Revertir al valor antiguo
            self.show_alert_dialog(
                f"No puedes seleccionar más de {self.max_allowed_pizza_rosca} pizzas o roscas en total. "
                f"Tu selección actual es {sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())}.",
                "pizzas_roscas"
            )
            self.calculate_total()
        else:
            self.calculate_total() # Calcular con el nuevo valor

    @rx.event
    def calculate_total(self):
        """Calcula el total de pizzas y roscas."""
        self.total_pizza_rosca = sum(self.pizza_selected.values()) + sum(self.rosca_selected.values())
    @rx.event
    def update_drink_selected(self, drink_type: str, value: str):
        """Actualiza la selección de bebidas."""
        new_value = int(value) if str(value).isdigit() else 0
        old_value = self.drink_selected.get(drink_type, 0)

        self.drink_selected[drink_type] = new_value # Actualizar temporalmente
        new_total = sum(self.drink_selected.values())

        if new_total > self.max_allowed_drinks:
            self.drink_selected[drink_type] = old_value # Revertir
            self.show_alert_dialog(
                f"No puedes seleccionar más de {self.max_allowed_drinks} bebidas en total. "
                f"Tu selección actual es {sum(self.drink_selected.values())}.",
                "drinks"
            )
            self.calculate_total_drinks()
        else:
            self.calculate_total_drinks() # Calcular con el nuevo valor

    @rx.event
    def calculate_total_drinks(self):
        """Calcula el total de bebidas."""
        self.total_drinks = sum(self.drink_selected.values())

    @rx.event
    def update_field(self, field: str, value):
        """Actualiza cualquier campo del estado por nombre."""
        if hasattr(self, field):
            setattr(self, field, value)
        else:
            raise AttributeError(f"Field {field} does not exist in FormBaseState.")

    @rx.var
    def can_send(self) -> bool:
        """Valida si el formulario está listo para enviar."""
        return (
            bool(self.child_name.strip()) and
            bool(self.child_age.strip()) and
            bool(self.birth_date.strip()) and
            bool(self.birth_time.strip()) and
            bool(self.selected_food_option.strip()) and
            bool(self.selected_bakery_option.strip()) and
            self.total_pizza_rosca == self.max_allowed_pizza_rosca and
            self.total_drinks == self.max_allowed_drinks
        )

    @rx.event
    def set_birth_time(self, new_birth_time: str):
        """Actualiza la hora de nacimiento."""
        self.birth_time = new_birth_time

    @rx.var
    def collected_data(self) -> dict:
        """Devuelve los datos del formulario."""
        return {
            "child_name": self.child_name,
            "child_age": self.child_age,
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "selected_food_option": self.selected_food_option,
            "butter_on_sandwiches": self.butter_on_sandwiches,
            "pizza_selected": self.pizza_selected,
            "rosca_selected": self.rosca_selected,
            "drink_selected": self.drink_selected,
            "extra_selected": self.extra_selected,
            "selected_bakery_option": self.selected_bakery_option,
            "observation_selected": self.observation_selected,
            "menu_number": self.menu_number,
            "menu_selection": self.menu_selection,
        }

    def _generate_whatsapp_message(self, pack_name: str, price: int, include_tortillas: bool = False) -> str:
        data = self.collected_data
        message = (
            f"Fecha: {data['birth_date']}\n"
            f"Hora: {data['birth_time']}\n"
            f"Cumpleaños de: {data['child_name']} edad {data['child_age']}\n\n"
            f"{pack_name}\n"
            "Los packs de cumpleaños incluyen patatas, palomitas, bollería/galletas y frutos secos.\n\n"
        )
        if include_tortillas:
            message += "+ 2 TORTILLAS DE PATATAS INCLUIDAS\n\n"

        message += f"{data['selected_food_option']}\n"
        
        # Añadir información sobre mantequilla si está marcado
        if data['butter_on_sandwiches']:
            message += "Untar bocadillos con mantequilla\n"
        
        message += "\n"

        if data['pizza_selected']:
            pizzas_items = [f"{pizza_type}: {quantity}" for pizza_type, quantity in data['pizza_selected'].items() if quantity > 0]
            if pizzas_items:
                message += "PIZZAS:\n" + "\n".join(pizzas_items) + "\n\n"

        if data['rosca_selected']:
            roscas_items = [f"{rosca_type}: {quantity}" for rosca_type, quantity in data['rosca_selected'].items() if quantity > 0]
            if roscas_items:
                message += "ROSCAS:\n" + "\n".join(roscas_items) + "\n\n"

        if data['drink_selected']:
            drinks_items = [f"{drink_type}: {quantity}" for drink_type, quantity in data['drink_selected'].items() if quantity > 0]
            if drinks_items:
                message += "BEBIDAS:\n" + "\n".join(drinks_items) + "\n\n"

        if data['extra_selected']: # Solo añadir si hay extras
            message += f"EXTRAS:\n\n{data['extra_selected']}\n\n"

        message += f"REPOSTERÍA:\n{data['selected_bakery_option']}\n\n"

        if data['observation_selected']:  # Solo añadir si hay observaciones
            message += f"OBSERVACIONES:\n{data['observation_selected']}"

        return message

    @rx.event
    def send_whatsapp_message(self):
        """Envía el mensaje de WhatsApp con los datos del formulario."""
        pack_map = {
            "Pack_15": ("PACK DE 15 PERSONAS--90€", 90, False),
            "Pack_20": ("PACK DE 20 PERSONAS--120€", 120, False),
            "Pack_25": ("PACK DE 25 PERSONAS--150€", 150, True),
            "Pack_30": ("PACK DE 30 PERSONAS--180€", 180, True),
        }
        if self.selected_pack in pack_map:
            pack_name, price, include_tortillas = pack_map[self.selected_pack]
            message = self._generate_whatsapp_message(pack_name, price, include_tortillas)
            encoded_message = quote(message) # Usar urllib.parse.quote para una codificación correcta
            phone_number = '34952520965'
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
            return rx.call_script(f"window.location.href = '{whatsapp_url}'")
