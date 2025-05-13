import reflex as rx
from mena_cumples.states.contact_form_state import ContactFormState


@rx.page(route="/contact_form_page")
def create_page_layout():
    """Create the overall page layout with gradient background and centered form container."""
    return rx.fragment(
        rx.box(
            create_form_container(),
            class_name="bg-gradient-to-br from-pink-100 to-purple-100",
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
        )
    )


def create_form_container():
    """Create a container for the birthday party request form with a heading."""
    return rx.box(
        rx.heading(
            "Preguntar Disponibilidad",
            font_weight="700",
            margin_bottom="1.5rem",
            font_size="1.5rem",
            line_height="2rem",
            text_align="center",
            color="#6D28D9",
            as_="h2",
        ),
        create_birthday_request_form(),
        background_color="#ffffffcc",
        max_width="28rem",
        padding="2rem",
        border_radius="0.5rem",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        width="100%",
    )


def create_birthday_request_form():
    return rx.form(
        create_labeled_input(
            label_text="Nombre de contacto",
            input_id="parentName",
            input_name="parentName",
            input_type="text",
        ),
        create_labeled_input(
            label_text="Nombre del niñ@ del cumple",
            input_id="childName",
            input_name="childName",
            input_type="text",
        ),
        create_labeled_input(
            label_text="Edad del niñ@ (máximo 12 años para poder reservar packs)",
            input_id="childAge",
            input_name="childAge",
            input_type="number",
        ),
        create_labeled_input(
            label_text="Fecha del cumple",
            input_id="birthdayDate",
            input_name="birthdayDate",
            input_type="date",
        ),
        create_label(label_text="Hora del cumple"),
        rx.select(
            ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30"],
            name="birth_time",  # Debe coincidir con el estado
            placeholder="Hora",
            on_change=lambda new_value: ContactFormState.set_birthday_time(new_value),
            value=ContactFormState.birthday_time,  # Consistencia en el estado
            required=True,
            background_color="#FDF2F8",
            border_width="1px",
            border_color="#F9A8D4",
            transition_duration="300ms",
            _focus={
                "border-color": "#8B5CF6",
                "outline-style": "none",
                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                "--ring-color": "#DDD6FE",
            },
            padding_left="0.75rem",
            padding_right="0.75rem",
            padding_top="0.5rem",
            padding_bottom="0.5rem",
            border_radius="0.5rem",
            color="#6D28D9",
            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
            width="100%",
        ),
        create_labeled_input(
            label_text="Número de personas",
            input_id="approximatePeople",
            input_name="approximatePeople",
            input_type="number",
        ),
        rx.box(
            create_label(label_text="Observaciones"),
            create_message_textarea(),
            margin_bottom="1.5rem",
        ),
        rx.flex(
            create_submit_button(),
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        on_submit=ContactFormState.handle_submit,
    )

def create_labeled_input(label_text, input_id, input_name, input_type):
    """Create a labeled input field with the given label text and input attributes."""
    return rx.box(
        create_label(label_text=label_text),
        create_input_field(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
        margin_bottom="1rem",
    )


def create_label(label_text):
    """Create a styled label element with the given text."""
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        color="#BE185D",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_input_field(input_id, input_name, input_type):
    """Create a styled input field with the specified id, name, and type."""
    return rx.el.input(
        id=input_id,
        name=input_name,
        required=True,
        type=input_type,
        background_color="#FDF2F8",
        border_width="1px",
        border_color="#F9A8D4",
        transition_duration="300ms",
        _focus={
            "border-color": "#8B5CF6",
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#DDD6FE",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#6D28D9",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_message_textarea():
    """Create a styled textarea for message input."""
    return rx.el.textarea(
        id="message",
        name="message",
        required=False,
        rows=4,
        placeholder="En caso de que necesite informar de algo más, escriba el mensaje",
        background_color="#FDF2F8",
        border_width="1px",
        border_color="#F9A8D4",
        transition_duration="300ms",
        _focus={
            "border-color": "#8B5CF6",
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#DDD6FE",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.5rem",
        color="#6D28D9",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )


def create_submit_button():
    """Create a styled submit button for the form."""
    return rx.el.button(
        " Enviar Whatsapp ",
        class_name="bg-gradient-to-r from-pink-400 hover:from-pink-500 hover:to-purple-600 to-purple-500 transform",
        type="submit",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#C4B5FD",
        },
        font_weight="700",
        _hover={"transform": "scale(1.05)"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.75rem",
        padding_bottom="0.75rem",
        border_radius="0.5rem",
        color="#ffffff",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )