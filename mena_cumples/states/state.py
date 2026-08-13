import reflex as rx
import asyncio
from urllib.parse import quote
from ..routes import Routes

class State(rx.State):
    conditions_acepted: bool = False
    
    @rx.event
    def set_conditions_acepted(self, value: bool):
        """
        Actualiza el estado de si las condiciones han sido aceptadas.
        Llamado por el checkbox en la página de índice.
        """
        self.conditions_acepted = value

    order_code: str = ""

    @rx.event
    def set_order_code(self, value: str):
        """Actualiza el código de reserva introducido en la landing.
        Normaliza el texto a mayúsculas para mantener el formato esperado.
        """
        self.order_code = (value or "").strip().upper()

    @rx.event
    async def submit_order_code(self):
        """
        Redirige a la selección de pack con el código introducido en la landing.
        Solo permite entrar si el código existe en la base de datos (veracidad).
        """
        from mena_cumples.supabase_utils import verificar_codigo_reserva

        codigo = self.order_code.strip().upper()
        if not codigo:
            return rx.window_alert("Introduce tu código de reserva para continuar.")
        if not await asyncio.to_thread(verificar_codigo_reserva, codigo):
            self.order_code = ""
            return rx.window_alert(
                "Ese código no es válido. Revisa el enlace que recibiste por WhatsApp."
            )
        return rx.redirect(f"{Routes.PACK_SELECTION.value}?codigo={quote(codigo)}")

    @rx.event
    def handle_ask_availability_click(self):
        """
        Maneja el evento de clic para el botón 'PREGUNTAR DISPONIBILIDAD'.
        Redirige a la página de solicitud de contacto si las condiciones son aceptadas.
        """
        if self.conditions_acepted:
            return rx.redirect(Routes.CONTACT_FORM_PAGE.value) 
        else:
            return rx.window_alert("Debe aceptar las condiciones para continuar.")

    @rx.event
    async def handle_url_code(self):
        """
        Si se llega al índice con ?codigo=CUM-XXXX (enlace de WhatsApp),
        redirige directamente a la selección de pack con el código incorporado,
        pero solo si el código existe en la base de datos (veracidad).
        Si el código no es válido, lo deja escrito en el campo para que el
        usuario lo corrija.
        """
        from mena_cumples.supabase_utils import verificar_codigo_reserva

        codigo = (self.router.url.query_parameters.get("codigo") or "").strip().upper()
        if not codigo:
            return
        if await asyncio.to_thread(verificar_codigo_reserva, codigo):
            return rx.redirect(f"{Routes.PACK_SELECTION.value}?codigo={quote(codigo)}")
        self.order_code = codigo

