import reflex as rx

class State(rx.State):
    conditions_acepted: bool = False
    
        #navigation
    def navigate_to_15(self):
        return rx.redirect("/pack_15_pax")
    
    def navigate_to_20(self):
        return rx.redirect("/pack_20_pax")
    
    def navigate_to_25(self):
        return rx.redirect("/pack_25_pax")
    
    def navigate_to_30(self):
        return rx.redirect("/pack_30_pax")
    

    def set_conditions_acepted(self, value: bool):
        """
        Actualiza el estado de si las condiciones han sido aceptadas.
        Llamado por el checkbox en la página de índice.
        """
        self.conditions_acepted = value

    def handle_ask_availability_click(self):
        """
        Maneja el evento de clic para el botón 'PREGUNTAR DISPONIBILIDAD'.
        Redirige a la página de solicitud de contacto si las condiciones son aceptadas.
        """
        if self.conditions_acepted:
            return rx.redirect("/solicitud_contacto") 
        else:
            return rx.window_alert("Debe aceptar las condiciones para continuar.")

