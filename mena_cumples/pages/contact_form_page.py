import reflex as rx
from ..routes import Routes
from mena_cumples.styles.styles import Color, FontSize, Size, BorderRadius, Shadow, Transition
from mena_cumples.states.contact_form_state import ContactFormState
from mena_cumples.components.navbar import navbar, mobile_drawer
from mena_cumples.components.footer import footer


@rx.page(route=Routes.CONTACT_FORM_PAGE.value)
def create_page_layout():
    return rx.box(
        navbar(),
        mobile_drawer(),
        rx.box(
            _form_hero(),
            create_form_container(),
            rx.link(
                rx.hstack(
                    rx.icon(tag="arrow-left", size=16),
                    rx.text("Volver al inicio"),
                    spacing="2",
                    align="center",
                ),
                href=Routes.INDEX.value,
                color=Color.PURPLE_DARK,
                font_weight="700",
                font_size=FontSize.SMALL,
                text_decoration="none",
                margin_top="1rem",
            ),
            width="100%",
            max_width="34rem",
            margin_left="auto",
            margin_right="auto",
            padding_x="1rem",
            padding_top="1rem",
            padding_bottom="3rem",
            display="flex",
            flex_direction="column",
            align_items="center",
        ),
        footer(),
        min_height="100vh",
        width="100%",
        background_color="#FFF7FB",
    )


def _form_hero():
    return rx.box(
        rx.vstack(
            rx.badge(
                rx.hstack(
                    rx.icon(tag="calendar-check", size=14),
                    rx.text("Paso 1 de 3"),
                    spacing="1",
                    align="center",
                ),
                color_scheme="purple",
                variant="soft",
                radius="full",
                size="2",
            ),
            rx.heading(
                "Pregunta tu fecha",
                font_size=rx.breakpoints({"0px": "1.9rem", "768px": "3rem"}),
                line_height="1.1",
                color=Color.WHITE,
                font_weight="900",
                text_align="center",
            ),
            rx.text(
                "Cuéntanos cuándo quieres celebrar y te respondemos "
                "por WhatsApp con tu código de reserva.",
                color="rgba(255,255,255,0.9)",
                text_align="center",
            ),
            spacing="3",
            align_items="center",
        ),
        class_name="bg-gradient-to-r from-fuchsia-500 via-purple-500 to-indigo-500",
        border_radius="1.5rem",
        padding="2rem 1.5rem",
        width="100%",
        box_shadow=Shadow.CARD,
    )


def create_form_container():
    return rx.box(
        create_birthday_request_form(),
        background_color=Color.WHITE,
        width="100%",
        margin_top="1.25rem",
        padding="1.5rem",
        border_radius="1.25rem",
        box_shadow=Shadow.CARD,
    )


def create_birthday_request_form():
    return rx.form(
        create_labeled_input(
            label_text="Nombre de contacto",
            input_id="parentName",
            input_name="parentName",
            input_type="text",
            icon="user",
        ),
        create_labeled_input(
            label_text="Nombre del niñ@ del cumple",
            input_id="childName",
            input_name="childName",
            input_type="text",
            icon="smile",
        ),
        rx.box(
            rx.box(
                create_label(label_text="Edad del niñ@", icon="cake"),
                rx.el.select(
                    rx.el.option("Elige edad", value="", disabled=True),
                    *[rx.el.option(f"{i} años", value=str(i)) for i in range(1, 13)],
                    name="childAge",
                    id="childAge",
                    required=True,
                    background_color="#FDF2F8",
                    border_width="2px",
                    border_style="solid",
                    border_color=Color.PURPLE_RING,
                    padding="0.5rem 0.75rem",
                    border_radius="1rem",
                    color=Color.PURPLE_DARK,
                    width="100%",
                    height="3rem",
                    font_size=FontSize.INPUT,
                    cursor="pointer",
                ),
                min_width="0",
            ),
            create_labeled_input(
                label_text="Número de personas",
                input_id="approximatePeople",
                input_name="approximatePeople",
                input_type="number",
                icon="users",
            ),
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "640px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            gap="1rem",
        ),
        rx.box(
            create_labeled_input(
                label_text="Fecha del cumple",
                input_id="birthdayDate",
                input_name="birthdayDate",
                input_type="date",
                icon="calendar",
            ),
            rx.box(
                create_label(label_text="Hora del cumple", icon="clock"),
                rx.el.select(
                    rx.el.option("Elige hora", value="", disabled=True),
                    *[
                        rx.el.option(h, value=h)
                        for h in ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"]
                    ],
                    name="birth_time",
                    on_change=lambda new_value: ContactFormState.set_birthday_time(new_value),
                    value=ContactFormState.birthday_time,
                    required=True,
                    background_color="#FDF2F8",
                    border_width="2px",
                    border_style="solid",
                    border_color=Color.PURPLE_RING,
                    padding="0.5rem 0.75rem",
                    border_radius="1rem",
                    color=Color.PURPLE_DARK,
                    width="100%",
                    height="3rem",
                    font_size=FontSize.INPUT,
                    cursor="pointer",
                ),
            ),
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "640px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            gap="1rem",
            align_items="end",
        ),
        rx.box(
            create_label(label_text="Observaciones", icon="pencil"),
            create_message_textarea(),
        ),
        rx.box(
            create_submit_button(),
            rx.text(
                "Se abrirá WhatsApp con tu mensaje listo para enviar. Te responderemos con disponibilidad y tu código.",
                font_size=FontSize.SMALL,
                color=Color.GRAY_TEXT,
                text_align="center",
                margin_top="0.75rem",
            ),
            margin_top="0.25rem",
        ),
        on_submit=ContactFormState.handle_submit,
        display="flex",
        flex_direction="column",
        gap="1.1rem",
    )

def create_labeled_input(label_text, input_id, input_name, input_type, icon=None):
    return rx.box(
        create_label(label_text=label_text, icon=icon),
        create_input_field(
            input_id=input_id,
            input_name=input_name,
            input_type=input_type,
        ),
        min_width="0",
    )


def create_label(label_text, icon=None):
    if icon is None:
        return rx.el.label(
            label_text,
            display="block",
            font_weight="600",
            margin_bottom="0.4rem",
            color=Color.PURPLE_DARK,
            font_size=FontSize.SMALL,
            line_height="1.25rem",
        )
    return rx.hstack(
        rx.box(
            rx.icon(tag=icon, size=13, color=Color.WHITE),
            background_color=Color.PURPLE,
            padding="0.25rem",
            border_radius="0.5rem",
            flex_shrink="0",
        ),
        rx.el.label(
            label_text,
            font_weight="700",
            color=Color.PURPLE_DARK,
            font_size=FontSize.SMALL,
            line_height="1.25rem",
        ),
        spacing="2",
        align_items="center",
        margin_bottom="0.45rem",
    )


def create_input_field(input_id, input_name, input_type):
    return rx.el.input(
        id=input_id,
        name=input_name,
        required=True,
        type=input_type,
        background_color="#FDF2F8",
        border_width="2px",
        border_color=Color.PURPLE_RING,
        transition_duration="300ms",
        _focus={
            "border-color": Color.PURPLE_LIGHT,
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING,
        },
        padding="0.5rem 0.75rem",
        border_radius="1rem",
        color=Color.PURPLE_DARK,
        transition_property=Transition.INPUT,
        transition_timing_function=Transition.INPUT_TIMING,
        width="100%",
        height="3rem",
        font_size=FontSize.INPUT,
    )


def create_message_textarea():
    return rx.el.textarea(
        id="message",
        name="message",
        required=False,
        rows=4,
        placeholder="En caso de que necesite informar de algo más, escriba el mensaje",
        background_color="#FDF2F8",
        border_width="2px",
        border_color=Color.PURPLE_RING,
        transition_duration="300ms",
        _focus={
            "border-color": Color.PURPLE_LIGHT,
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING,
        },
        padding="0.5rem 0.75rem",
        border_radius="1rem",
        color=Color.PURPLE_DARK,
        transition_property=Transition.INPUT,
        transition_timing_function=Transition.INPUT_TIMING,
        width="100%",
        font_size=FontSize.INPUT,
    )


def create_submit_button():
    return rx.el.button(
        rx.hstack(
            rx.icon(tag="message-circle", size=18),
            rx.text("Enviar por WhatsApp"),
            spacing="2",
            align_items="center",
            justify_content="center",
        ),
        class_name="bg-gradient-to-r from-fuchsia-500 via-purple-500 to-indigo-500 w-full",
        type="submit",
        transition_duration="300ms",
        transition_timing_function=Transition.INPUT_TIMING,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": Color.PURPLE_RING_ALT,
        },
        font_weight="800",
        _hover={"filter": "brightness(1.08)"},
        padding="1rem 1.5rem",
        border_radius="9999px",
        color=Color.WHITE,
        cursor="pointer",
        transition_property=Transition.INPUT,
    )
