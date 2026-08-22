import reflex as rx
import asyncio
from typing import Dict
from urllib.parse import quote
from ..routes import Routes

class FormBaseState(rx.State):
    """Estado base para el formulario de packs de cumpleaños."""

    # Variables de estado
    child_name: str = ""
    child_age: str = ""
    birth_date: str = ""
    birth_time: str = ""
    reservation_code: str = ""
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
    alert_title: str = ""
    max_allowed_pizza_rosca: int = 3
    max_allowed_drinks: int = 4
    selected_pack: str = ""

    # Código de reserva cargado desde el enlace de WhatsApp (?codigo=CUM-XXXX).
    # code_locked bloquea el campo para que el cliente no pueda modificar el código.
    code_locked: bool = False

    @rx.event
    async def ensure_order_access(self):
        """Candado de acceso a las páginas de pedido.

        Solo se puede entrar a seleccionar pack o rellenar el formulario si la
        URL trae un código de reserva REAL (?codigo=CUM-XXXX) existente en la
        base de datos. Si no hay código o no es válido, se redirige al inicio.
        """
        from mena_cumples.supabase_utils import verificar_codigo_reserva

        codigo = (self.router.url.query_parameters.get("codigo") or "").strip().upper()
        if not codigo or not await asyncio.to_thread(verificar_codigo_reserva, codigo):
            return rx.redirect(Routes.INDEX.value)
        self.reservation_code = codigo
        self.code_locked = True

    @rx.event
    async def init_pack_page(self, pack_type: str):
        """Inicializa la página del pack: selecciona el pack y precarga el código.

        Si la URL no trae un código de reserva válido (existente en la base de
        datos), redirige al inicio (candado de acceso).
        """
        from mena_cumples.supabase_utils import verificar_codigo_reserva

        codigo = (self.router.url.query_parameters.get("codigo") or "").strip().upper()
        if not codigo or not await asyncio.to_thread(verificar_codigo_reserva, codigo):
            return rx.redirect(Routes.INDEX.value)
        self.select_pack(pack_type)
        self.reservation_code = codigo
        self.code_locked = True

    # Precios base (año 2026)
    PACK_BASE_PRICES = {
        "Pack_15": 110,
        "Pack_20": 140,
        "Pack_25": 170,
        "Pack_30": 200,
    }

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
        self.selected_bakery_option = ""
        self.bakery_price = 0.0
        self.bakery_weight = 1.0
        self.update_trigger += 1

    @rx.var
    def get_pack_price(self) -> int:
        """Devuelve el precio del pack."""
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
    def show_alert_dialog(self, message: str, alert_type: str = "pizzas_roscas", title: str = ""):
        """Muestra un diálogo de alerta."""
        titles = {
            "pizzas_roscas": "Límite Excedido",
            "drinks": "Límite Excedido",
            "error": "Error",
            "success": "Éxito",
        }
        self.alert_title = title or titles.get(alert_type, "Aviso")
        self.show_alert = True
        self.alert_message = message
        self.alert_type = alert_type

    @rx.event
    def reset_alert(self):
        """Oculta el diálogo de alerta."""
        self.show_alert = False
        self.alert_message = ""
        self.alert_title = ""

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
    show_extras: bool = False
    extra_pizza_selected: Dict[str, int] = {}
    extra_rosca_selected: Dict[str, int] = {}
    extra_drink_selected: Dict[str, int] = {}
    candy_count: int = 0
    total_extra_food_price: float = 0.0
    total_extra_drink_price: float = 0.0
    total_candy_price: float = 0.0

    # Precios unitarios
    @rx.var
    def price_extra_pizza_margarita(self) -> float:
        return 6.50

    @rx.var
    def price_extra_pizza_general(self) -> float:
        return 7.50

    @rx.var
    def price_extra_drink_general(self) -> float:
        return 4.00
    
    @rx.var
    def price_extra_water(self) -> float:
        return 2.50 # Precio constante

    @rx.var
    def price_candy(self) -> float:
        return 2.00 # Precio constante


    @rx.event
    def toggle_extras(self, value: bool):
        """Muestra u oculta la sección de extras y resetea los valores."""
        self.show_extras = not self.show_extras if not isinstance(value, bool) else value
        if not self.show_extras:
            self.extra_pizza_selected = {}
            self.extra_rosca_selected = {}
            self.extra_drink_selected = {}
            self.candy_count = 0
            self.calculate_extra_prices()

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
            bool(self.reservation_code.strip()) and
            bool(self.selected_food_option.strip()) and
            bool(self.selected_bakery_option.strip()) and
            self.total_pizza_rosca == self.max_allowed_pizza_rosca and
            self.total_drinks == self.max_allowed_drinks
        )

    @rx.var
    def missing_pizza_rosca(self) -> int:
        """Devuelve la cantidad faltante de pizzas/roscas."""
        return max(0, self.max_allowed_pizza_rosca - self.total_pizza_rosca)

    @rx.var
    def missing_drinks(self) -> int:
        """Devuelve la cantidad faltante de bebidas."""
        return max(0, self.max_allowed_drinks - self.total_drinks)

    @rx.var
    def total_missing(self) -> int:
        """Devuelve la cantidad total faltante."""
        return self.missing_pizza_rosca + self.missing_drinks

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
            "reservation_code": self.reservation_code,
            "selected_food_option": self.selected_food_option,
            "butter_on_sandwiches": self.butter_on_sandwiches,
            "pizza_selected": self.pizza_selected,
            "rosca_selected": self.rosca_selected,
            "drink_selected": self.drink_selected,
            "extra_selected": self.extra_selected,
            "show_extras": self.show_extras,
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
            f"Cumpleaños de: {data['child_name']} edad {data['child_age']}\n"
            f"CÓDIGO DE RESERVA: {data['reservation_code']}\n\n"
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

    def _compute_total_price(self, pack_price: int) -> float:
        data = self.collected_data
        return (
            pack_price
            + data["total_extra_food_price"]
            + data["total_extra_drink_price"]
            + data["total_candy_price"]
            + data["bakery_price"]
        )

    async def _save_order_to_supabase(self, pack_name: str, pack_price: int) -> bool:
        """Guarda el pedido en Supabase actualizando la ficha existente por codigo_reserva.

        La ficha (reserva manual del hotel) ya existe en la tabla cumples_pedidos.
        Aquí SOLO se actualiza esa misma fila con el detalle del pedido web,
        evitando duplicados. Devuelve True si se actualizó (código válido).
        """
        try:
            from mena_cumples.supabase_utils import get_supabase_client

            data = self.collected_data
            total_price = self._compute_total_price(pack_price)
            codigo = (data["reservation_code"] or "").strip().upper()

            if not codigo:
                return False

            payload = {
                "pack": self.selected_pack,
                "nombre_nino": data["child_name"],
                "edad": data["child_age"],
                "fecha_cumple": data["birth_date"] or None,
                "hora_cumple": data["birth_time"],
                "opcion_comida": data["selected_food_option"],
                "mantequilla": data["butter_on_sandwiches"],
                "total_precio": round(total_price, 2),
                "estado": "Confirmado",
                "observaciones": data["observation_selected"],
                "detalle": data,
                "pedido_web": True,
            }

            client = get_supabase_client()
            response = await asyncio.to_thread(
                lambda: client.table("cumples_pedidos")
                .update(payload)
                .eq("codigo_reserva", codigo)
                .execute()
            )
            if response.data:
                print(f"Pedido {pack_name} vinculado a la ficha con código {codigo} (id={response.data[0]['id']})")
                return True
            print(f"Código de reserva {codigo} no encontrado")
            return False
        except Exception as e:
            print(f"Error guardando pedido en Supabase: {e}")
            return False

    @rx.event
    async def send_whatsapp_message(self):
        """Envía el mensaje de WhatsApp con los datos del formulario y guarda el pedido en Supabase."""
        pack_map = {
            "Pack_15": ("PACK DE 15 PERSONAS", False),
            "Pack_20": ("PACK DE 20 PERSONAS", False),
            "Pack_25": ("PACK DE 25 PERSONAS", True),
            "Pack_30": ("PACK DE 30 PERSONAS", True),
        }
        if self.selected_pack in pack_map:
            pack_name, include_tortillas = pack_map[self.selected_pack]
            price = self.get_pack_price  # Obtener precio dinámico
            # Guardar el pedido en Supabase (actualiza la ficha por código) antes de abrir WhatsApp.
            # Si el código no es válido o falla, se avisa al usuario y NO se abre WhatsApp.
            saved = await self._save_order_to_supabase(pack_name, price)
            if not saved:
                self.show_alert_dialog(
                    "No se ha podido realizar tu pedido. Comprueba que el CÓDIGO DE RESERVA es "
                    "correcto (lo recibiste por WhatsApp al reservar la fecha) e inténtalo de nuevo. "
                    "Si el problema continúa, contáctanos por WhatsApp.",
                    "error",
                )
                return
            pack_name_with_price = f"{pack_name}--{price}€"
            message = self._generate_whatsapp_message(pack_name_with_price, price, include_tortillas)
            encoded_message = quote(message)  # Usar urllib.parse.quote para una codificación correcta
            phone_number = "34952520965"
            # api.whatsapp.com/send es más fiable que wa.me para mensajes largos
            # (sobre todo en iOS/Safari). window.open con fallback a location.href
            # evita que un bloqueo de popup o un contexto async deje al usuario
            # sin abrir WhatsApp.
            whatsapp_url = f"https://api.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
            script = (
                f"const url = '{whatsapp_url}';"
                "const win = window.open(url, '_blank', 'noopener');"
                "if (!win) { window.location.href = url; }"
            )
            yield rx.call_script(script)
