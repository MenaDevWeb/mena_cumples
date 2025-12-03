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

    # Precios base (año 2025)
    PACK_BASE_PRICES = {
        "Pack_15": 90,
        "Pack_20": 120,
        "Pack_25": 150,
        "Pack_30": 180,
    }
    
    # Incremento de precio para 2026 en adelante
    PRICE_INCREASE_2026 = 20

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

    @rx.var
    def get_pack_price(self) -> int:
        """Calcula el precio del pack según el año de la fecha seleccionada."""
        if not self.selected_pack or not self.birth_date:
            return self.PACK_BASE_PRICES.get(self.selected_pack, 0)
        
        try:
            # Extraer el año de la fecha (formato: YYYY-MM-DD)
            year = int(self.birth_date.split("-")[0])
            base_price = self.PACK_BASE_PRICES.get(self.selected_pack, 0)
            
            # Si es 2026 o posterior, aplicar incremento
            if year >= 2026:
                return base_price + self.PRICE_INCREASE_2026
            return base_price
        except (ValueError, IndexError):
            # Si hay error al parsear la fecha, devolver precio base
            return self.PACK_BASE_PRICES.get(self.selected_pack, 0)

    @rx.var
    def pack_title_with_price(self) -> str:
        """Genera el título del pack con el precio dinámico."""
        pack_names = {
            "Pack_15": "PACK DE 15 PERSONAS",
            "Pack_20": "PACK DE 20 PERSONAS",
            "Pack_25": "PACK DE 25 PERSONAS",
            "Pack_30": "PACK DE 30 PERSONAS",
        }
        pack_name = pack_names.get(self.selected_pack, "")
        price = self.get_pack_price
        return f"{pack_name}--{price}€" if pack_name else ""



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
    # Variables para Extras
    extra_pizza_selected: Dict[str, int] = {}
    extra_rosca_selected: Dict[str, int] = {}
    extra_drink_selected: Dict[str, int] = {}
    candy_count: int = 0
    total_extra_food_price: float = 0.0
    total_extra_drink_price: float = 0.0
    total_candy_price: float = 0.0

    # Variables computadas para precios unitarios dinámicos
    @rx.var
    def price_extra_pizza_margarita(self) -> float:
        return 6.50 if self.is_2026_or_later else 6.00

    @rx.var
    def price_extra_pizza_general(self) -> float:
        return 7.50 if self.is_2026_or_later else 6.00

    @rx.var
    def price_extra_drink_general(self) -> float:
        return 4.00 if self.is_2026_or_later else 3.50
    
    @rx.var
    def price_extra_water(self) -> float:
        return 2.50 # Precio constante

    @rx.var
    def price_candy(self) -> float:
        return 2.00 # Precio constante

    @rx.var
    def is_2026_or_later(self) -> bool:
        """Determina si la fecha seleccionada es 2026 o posterior."""
        if not self.birth_date:
            return False
        try:
            year = int(self.birth_date.split("-")[0])
            return year >= 2026
        except (ValueError, IndexError):
            return False

    @rx.event
    def update_extra_pizza_selected(self, pizza_type: str, value: str):
        """Actualiza la selección de pizzas extra."""
        new_value = int(value) if str(value).isdigit() else 0
        self.extra_pizza_selected[pizza_type] = new_value
        self.calculate_extra_prices()

    @rx.event
    def update_extra_rosca_selected(self, rosca_type: str, value: str):
        """Actualiza la selección de roscas extra."""
        new_value = int(value) if str(value).isdigit() else 0
        self.extra_rosca_selected[rosca_type] = new_value
        self.calculate_extra_prices()

    @rx.event
    def update_extra_drink_selected(self, drink_type: str, value: str):
        """Actualiza la selección de bebidas extra."""
        new_value = int(value) if str(value).isdigit() else 0
        self.extra_drink_selected[drink_type] = new_value
        self.calculate_extra_prices()

    @rx.event
    def update_candy_count(self, value: str):
        """Actualiza la cantidad de platos de chuches."""
        try:
            self.candy_count = int(value)
            if self.candy_count < 0: self.candy_count = 0
        except ValueError:
            self.candy_count = 0
        self.calculate_extra_prices()

    @rx.event
    def calculate_extra_prices(self):
        """Calcula el precio total de todos los extras."""
        # Calcular comida
        food_total = 0.0
        for pizza, qty in self.extra_pizza_selected.items():
            if pizza.lower() == "margarita":
                food_total += qty * self.price_extra_pizza_margarita
            else:
                food_total += qty * self.price_extra_pizza_general
        
        for rosca, qty in self.extra_rosca_selected.items():
            food_total += qty * self.price_extra_pizza_general # Roscas usan precio general
            
        self.total_extra_food_price = food_total

        # Calcular bebidas
        drink_total = 0.0
        for drink, qty in self.extra_drink_selected.items():
            if "agua" in drink.lower():
                drink_total += qty * self.price_extra_water
            else:
                drink_total += qty * self.price_extra_drink_general
        
        self.total_extra_drink_price = drink_total

        # Calcular chuches
        self.total_candy_price = self.candy_count * self.price_candy

    # Variables para Repostería
    bakery_price: float = 0.0
    bakery_weight: float = 1.0 # Peso por defecto 1kg

    @rx.event
    def update_bakery_option(self, value: str):
        """Actualiza la opción de repostería y calcula su precio."""
        self.selected_bakery_option = value
        self.calculate_bakery_price()

    @rx.event
    def update_bakery_weight(self, value: str):
        """Actualiza el peso de la tarta y recalcula el precio."""
        try:
            self.bakery_weight = float(value)
            if self.bakery_weight < 0:
                self.bakery_weight = 0
        except ValueError:
            self.bakery_weight = 0
        self.calculate_bakery_price()

    @rx.event
    def calculate_bakery_price(self):
        """Calcula el precio de la repostería seleccionada."""
        option = self.selected_bakery_option.lower()
        price = 0.0

        # Usar palabras clave únicas para identificar la opción
        if "tarta de galletas" in option:
            price = 15.0
        elif "bizcocho" in option:
            price = 10.0
        elif "tarta panadería" in option:
            price = 18.0 * self.bakery_weight
        elif "kinder" in option: # Palmera kinder (más específica primero)
            price = 28.0
        elif "palmera gigante de chocolate" in option: # Palmera normal
            price = 25.0
        elif "la tarta la traemos nosotros" in option:
            price = 0.0
        
        self.bakery_price = price

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
            "extra_pizza_selected": self.extra_pizza_selected,
            "extra_rosca_selected": self.extra_rosca_selected,
            "extra_drink_selected": self.extra_drink_selected,
            "candy_count": self.candy_count,
            "total_extra_food_price": self.total_extra_food_price,
            "total_extra_drink_price": self.total_extra_drink_price,
            "total_candy_price": self.total_candy_price,
            "selected_bakery_option": self.selected_bakery_option,
            "bakery_price": self.bakery_price,
            "bakery_weight": self.bakery_weight,
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

        if data['extra_selected']: # Solo añadir si hay extras de texto
            message += f"OTROS EXTRAS:\n{data['extra_selected']}\n\n"

        # Añadir extras de comida (pizzas y roscas)
        extra_food_items = []
        if data['extra_pizza_selected']:
            for pizza, qty in data['extra_pizza_selected'].items():
                if qty > 0:
                    extra_food_items.append(f"Pizza Extra {pizza}: {qty}")
        
        if data['extra_rosca_selected']:
            for rosca, qty in data['extra_rosca_selected'].items():
                if qty > 0:
                    extra_food_items.append(f"Rosca Extra {rosca}: {qty}")
        
        if extra_food_items:
            message += "EXTRAS COMIDA:\n" + "\n".join(extra_food_items) + "\n"
            message += f"Precio Extras Comida: {data['total_extra_food_price']:.2f}€\n\n"

        # Añadir extras de bebidas
        extra_drink_items = []
        if data['extra_drink_selected']:
            for drink, qty in data['extra_drink_selected'].items():
                if qty > 0:
                    extra_drink_items.append(f"Bebida Extra {drink}: {qty}")
        
        if extra_drink_items:
            message += "EXTRAS BEBIDAS:\n" + "\n".join(extra_drink_items) + "\n"
            message += f"Precio Extras Bebidas: {data['total_extra_drink_price']:.2f}€\n\n"

        # Añadir chuches
        if data['candy_count'] > 0:
            message += f"EXTRAS CHUCHES:\nPlatos de Chuches: {data['candy_count']}\n"
            message += f"Precio Chuches: {data['total_candy_price']:.2f}€\n\n"

        message += f"REPOSTERÍA:\n{data['selected_bakery_option']}\n"
        if "tarta panadería" in data['selected_bakery_option'].lower():
            message += f"Peso aproximado: {data['bakery_weight']} kg\n"
        message += f"Precio Repostería: {data['bakery_price']:.2f}€\n\n"

        if data['observation_selected']:  # Solo añadir si hay observaciones
            message += f"OBSERVACIONES:\n{data['observation_selected']}\n\n"

        # Calcular y mostrar precio total
        total_price = price + data['total_extra_food_price'] + data['total_extra_drink_price'] + data['total_candy_price'] + data['bakery_price']
        message += f"TOTAL A PAGAR: {total_price:.2f}€"

        return message

    @rx.event
    def send_whatsapp_message(self):
        """Envía el mensaje de WhatsApp con los datos del formulario."""
        pack_map = {
            "Pack_15": ("PACK DE 15 PERSONAS", False),
            "Pack_20": ("PACK DE 20 PERSONAS", False),
            "Pack_25": ("PACK DE 25 PERSONAS", True),
            "Pack_30": ("PACK DE 30 PERSONAS", True),
        }
        if self.selected_pack in pack_map:
            pack_name, include_tortillas = pack_map[self.selected_pack]
            price = self.get_pack_price  # Obtener precio dinámico
            pack_name_with_price = f"{pack_name}--{price}€"
            message = self._generate_whatsapp_message(pack_name_with_price, price, include_tortillas)
            encoded_message = quote(message) # Usar urllib.parse.quote para una codificación correcta
            phone_number = '34952520965'
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
            return rx.call_script(f"window.location.href = '{whatsapp_url}'")
