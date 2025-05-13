import reflex as rx
from urllib.parse import quote

class ContactFormState(rx.State):
    parent_name: str = ""
    child_name: str = ""
    child_age: str = ""
    birthday_date: str = ""
    birthday_time: str = ""  
    aproximate_people: str = ""
    message: str = ""

    def set_birthday_time(self, new_birthday_time):
        """Método para actualizar la hora del cumpleaños"""
        self.birthday_time = new_birthday_time

    def collect_data(self):
        """Recoge los datos del formulario"""
        return {
            "parent_name": self.parent_name,
            "child_name": self.child_name,
            "child_age": self.child_age,
            "birthday_date": self.birthday_date,
            "birthday_time": self.birthday_time,  # Consistencia en nombres
            "aproximate_people": self.aproximate_people,
            "message": self.message
        }

    def generate_whatsapp_message(self):
        """Genera el mensaje de WhatsApp con los datos del formulario"""
        data = self.collect_data()
        # Formatear el mensaje para WhatsApp
        message = (
            f"¿Tendrían disponibilidad para celebrar un cumple la fecha indicada?\n\n"
            f"Nombre del padre: {data['parent_name']}\n"
            f"Nombre del niño: {data['child_name']}\n"
            f"Edad del niño: {data['child_age']}\n"
            f"Fecha del cumpleaños: {data['birthday_date']}\n"
            f"Hora: {data['birthday_time']}\n"  # Usar el nombre correcto
            f"Número de personas: {data['aproximate_people']}\n"
            f"Observaciones: {data['message']}"
        )

        # Codificar el mensaje en formato URL
        encoded_message = quote(message)
        phone_number = '+34952520965'  # Número de WhatsApp de destino
        whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"
        return rx.redirect(whatsapp_url, external=True)

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario y redirige a WhatsApp"""
        # Capturar los valores del formulario con los nombres correctos
        self.parent_name = form_data.get("parentName", "")
        self.child_name = form_data.get("childName", "")
        self.child_age = form_data.get("childAge", "")
        self.birthday_date = form_data.get("birthdayDate", "")
        self.birthday_time = form_data.get("birth_time", "")  # Corregido el nombre
        self.aproximate_people = form_data.get("approximatePeople", "")
        self.message = form_data.get("message", "")

        # Validar que los campos requeridos no estén vacíos
        if not all([self.parent_name, self.child_name, self.child_age, self.birthday_date, self.birthday_time]):
            return rx.window_alert(message="Por favor, complete todos los campos obligatorios.")

        # Generar el mensaje de WhatsApp y redirigir
        return self.generate_whatsapp_message()