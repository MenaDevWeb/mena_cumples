import reflex as rx
from ..routes import Routes
from mena_cumples.styles.styles import Color, FontSize, Size, BorderRadius, Shadow, Transition
from mena_cumples.states.contact_form_state import ContactFormState


@rx.page(route=Routes.CONTACT_FORM_PAGE.value)
def create_page_layout():
    return rx.fragment(
        rx.box(
            create_form_container(),
            class_name=Color.GRADIENT_FORM,
            display="flex",
            align_items="center",
            justify_content="center",
            min_height="100vh",
        )
    )


def create_form_container():
    return rx.box(
        rx.heading(
            "Preguntar Disponibilidad",
            font_weight="700",
            margin_bottom=Size.DEFAULT.value,
            font_size=FontSize.XL,
            line_height="2rem",
            text_align="center",
            color=Color.PURPLE_DARK,
            as_="h2",
        ),
        create_birthday_request_form(),
        background_color="#ffffffcc",
        max_width="28rem",
        padding=Size.MEDIUM.value,
        border_radius=BorderRadius.SMALL,
        box_shadow=Shadow.FORM,
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
            ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"],
            name="birth_time",
            placeholder="Hora",
            on_change=lambda new_value: ContactFormState.set_birthday_time(new_value),
            value=ContactFormState.birthday_time,
            required=True,
            background_color=Color.PINK_BG,
            border_width="1px",
            border_color=Color.PINK_LIGHT,
            transition_duration="300ms",
            _focus={
                "border-color": Color.PURPLE_LIGHT,
                "outline-style": "none",
                "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
                "--ring-color": Color.PURPLE_RING,
            },
            padding="0.5rem 0.75rem",
            border_radius=BorderRadius.SMALL,
            color=Color.PURPLE_DARK,
            transition_property=Transition.INPUT,
            transition_timing_function=Transition.INPUT_TIMING,
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
            margin_bottom=Size.DEFAULT.value,
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
    return rx.box(
        create_label(label_text=label_text),
        create_input_field(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
        margin_bottom=Size.SMALL.value,
    )


def create_label(label_text):
    return rx.el.label(
        label_text,
        display="block",
        font_weight="500",
        margin_bottom="0.5rem",
        color=Color.PINK,
        font_size=FontSize.SMALL,
        line_height="1.25rem",
    )


def create_input_field(input_id, input_name, input_type):
    return rx.el.input(
        id=input_id,
        name=input_name,
        required=True,
        type=input_type,
        background_color=Color.PINK_BG,
        border_width="1px",
        border_color=Color.PINK_LIGHT,
        transition_duration="300ms",
        _focus={
            "border-color": Color.PURPLE_LIGHT,
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING,
        },
        padding="0.5rem 0.75rem",
        border_radius=BorderRadius.SMALL,
        color=Color.PURPLE_DARK,
        transition_property=Transition.INPUT,
        transition_timing_function=Transition.INPUT_TIMING,
        width="100%",
    )


def create_message_textarea():
    return rx.el.textarea(
        id="message",
        name="message",
        required=False,
        rows=4,
        placeholder="En caso de que necesite informar de algo más, escriba el mensaje",
        background_color=Color.PINK_BG,
        border_width="1px",
        border_color=Color.PINK_LIGHT,
        transition_duration="300ms",
        _focus={
            "border-color": Color.PURPLE_LIGHT,
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING,
        },
        padding="0.5rem 0.75rem",
        border_radius=BorderRadius.SMALL,
        color=Color.PURPLE_DARK,
        transition_property=Transition.INPUT,
        transition_timing_function=Transition.INPUT_TIMING,
        width="100%",
    )


def create_submit_button():
    return rx.el.button(
        " Enviar Whatsapp ",
        class_name="bg-gradient-to-r from-pink-400 hover:from-pink-500 hover:to-purple-600 to-purple-500 transform",
        type="submit",
        transition_duration="300ms",
        transition_timing_function=Transition.INPUT_TIMING,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING_ALT,
        },
        font_weight="700",
        _hover={"transform": "scale(1.05)"},
        padding="0.75rem 1.5rem",
        border_radius=BorderRadius.SMALL,
        color=Color.WHITE,
        transition_property=Transition.INPUT,
    )