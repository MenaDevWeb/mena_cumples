import reflex as rx
from mena_cumples.styles.styles import Color, Shadow, BorderRadius, Transition
from .radio_group_button import radio_button_food
from .radio_group_button import radio_button_bakery
from mena_cumples.states.form_state import FormBaseState


# ============================================================
# Helpers de diseño reutilizables
# ============================================================

def _section_card(title: str, children, icon_tag: str = "", bg_color: str = Color.CARD_PURPLE) -> rx.Component:
    """Card de sección con encabezado e icono."""
    header = (
        rx.hstack(
            rx.icon(tag=icon_tag, color=Color.PURPLE, size=18),
            rx.text(title, weight="bold", color=Color.PURPLE_DARK, size="4"),
            spacing="2",
            align_items="center",
        )
        if icon_tag
        else rx.text(title, weight="bold", color=Color.PURPLE_DARK, size="4")
    )
    return rx.box(
        header,
        children,
        width="100%",
        padding="1.25rem",
        border_radius="1rem",
        background_color=bg_color,
        border="1px solid rgba(124, 58, 237, 0.12)",
        box_shadow=Shadow.CARD,
        margin_bottom="1rem",
    )


def _question(text: str, margin_top: str = "0.75rem") -> rx.Component:
    """Título de pregunta dentro de una sección."""
    return rx.text(text, weight="bold", color=Color.PURPLE_DARK, margin_top=margin_top)


def _hint(text: str) -> rx.Component:
    """Texto de ayuda en cursiva."""
    return rx.text(
        text,
        style={"font_style": "italic", "font_size": "14px", "color": Color.PURPLE_DARK},
    )


def _quantity_input(value, on_change, max_length: int = 1) -> rx.Component:
    """Input de cantidad pequeño y consistente."""
    return rx.input(
        placeholder="0",
        value=value,
        on_change=on_change,
        max_length=max_length,
        type="number",
        min=0,
        width="50px",
        height="40px",
        font_size="16px",
        text_align="center",
        background_color=Color.WHITE,
        border="1px solid rgba(124, 58, 237, 0.25)",
        border_radius="0.5rem",
    )


def _option_row(value, on_change, label, price=None, max_length: int = 1) -> rx.Component:
    """Fila de opción: input de cantidad + etiqueta (con precio opcional)."""
    return rx.hstack(
        _quantity_input(value, on_change, max_length),
        rx.vstack(
            rx.text(label, style={"font_size": "16px", "font_style": "italic", "color": Color.PURPLE_DARK}),
            rx.cond(
                price is not None,
                rx.text(price, style={"font_size": "12px", "color": Color.PINK}),
                rx.fragment(),
            ),
            spacing="0",
            align_items="start",
        ),
        align_items="center",
        spacing="3",
        margin_bottom="10px",
    )


def _total_row(label: str, value) -> rx.Component:
    """Fila de total con el precio formateado."""
    return rx.hstack(
        rx.text(label, weight="medium"),
        rx.text(f"{value:.2f}€", weight="bold"),
        justify_content="space-between",
        width="100%",
    )


def _alert_dialog() -> rx.Component:
    """Modal de alerta con la paleta del diseño."""
    return rx.cond(
        FormBaseState.show_alert,
        rx.box(
            rx.box(
                rx.hstack(
                    rx.icon(tag="triangle-alert", color=Color.ERROR, size=22),
                    rx.heading(
                        FormBaseState.alert_title,
                        font_size="1.25rem",
                        color=Color.ERROR,
                        font_weight="700",
                    ),
                    spacing="2",
                    align_items="center",
                    margin_bottom="0.75rem",
                ),
                rx.text(
                    FormBaseState.alert_message,
                    color=Color.PURPLE_DARK,
                    font_size="0.9rem",
                    line_height="1.5",
                ),
                rx.el.div(
                    rx.button(
                        "Entendido",
                        on_click=FormBaseState.reset_alert,
                        type="button",
                        background_color=Color.PURPLE,
                        color=Color.WHITE,
                        font_weight="700",
                        border_radius=BorderRadius.FULL,
                        padding="0.5rem 1.5rem",
                        transition=Transition.DEFAULT,
                        _hover={"background_color": Color.PURPLE_DARK},
                    ),
                    display="flex",
                    justify_content="flex-end",
                    padding_top="1rem",
                ),
                background_color=Color.WHITE,
                padding="1.5rem",
                border_radius="1rem",
                box_shadow="0 25px 50px -12px rgba(0, 0, 0, 0.3)",
                width="100%",
                max_width="28rem",
            ),
            position="fixed",
            inset="0",
            background_color=Color.BG_OVERLAY,
            display="flex",
            align_items="center",
            justify_content="center",
            z_index="50",
            padding="1rem",
        ),
        rx.fragment(),
    )


def _header_card(image_url: str, pack_description: str) -> rx.Component:
    """Card de encabezado del pack con título responsive."""
    return rx.box(
        rx.cond(
            image_url != "",
            rx.image(
                src=image_url,
                width="100%",
                height="auto",
                border_radius="0.75rem",
                margin_bottom="1rem",
                max_height="260px",
                object_fit="cover",
            ),
            rx.fragment(),
        ),
        rx.heading(
            FormBaseState.pack_title_with_price,
            align="center",
            width="100%",
            font_size="1.6rem",
            line_height="2rem",
            color=Color.PURPLE,
            font_weight="700",
            margin_top="0.5rem",
        ),
        rx.text(
            pack_description,
            margin_top="1rem",
            color=Color.PURPLE_DARK,
            size="3",
            weight="medium",
            style={"font_style": "italic"},
            text_align="center",
        ),
        padding="1.25rem",
        border_radius="1rem",
        background_color=Color.CARD_PINK,
        border="1px solid rgba(190, 24, 93, 0.12)",
        box_shadow=Shadow.CARD,
        margin_bottom="1rem",
        width="100%",
    )


def _reserva_content() -> rx.Component:
    """Contenido de la card de código de reserva."""
    return rx.vstack(
        _hint("Introduce el código de reserva que recibiste por WhatsApp para poder hacer tu pedido."),
        rx.input(
            placeholder="Código de reserva (ej: CUM-7XD4)",
            value=FormBaseState.reservation_code,
            read_only=FormBaseState.code_locked,
            on_change=lambda new_value: FormBaseState.update_field("reservation_code", new_value),
            width="100%",
            height="45px",
            font_size="18px",
            font_weight="700",
            text_transform="uppercase",
            letter_spacing="2px",
            background_color=Color.WHITE,
            border="1px solid rgba(124, 58, 237, 0.25)",
            border_radius="0.5rem",
        ),
        rx.cond(
            FormBaseState.code_locked,
            rx.text(
                f"Reserva {FormBaseState.reservation_code} cargada desde tu enlace. "
                "Solo tienes que rellenar tu pedido.",
                style={"font_style": "italic", "font_size": "13px"},
                color="#16a34a",
            ),
            rx.fragment(),
        ),
        width="100%",
        spacing="3",
    )


def _extras_toggle() -> rx.Component:
    """Checkbox para mostrar u ocultar la sección de extras."""
    return rx.box(
        rx.checkbox(
            " QUIERO AÑADIR EXTRAS (pizzas, roscas, bebidas extra, chuches) ",
            checked=FormBaseState.show_extras,
            on_change=FormBaseState.toggle_extras,
            size="3",
            color_scheme="purple",
        ),
        width="100%",
        text_align="center",
        margin_y="0.5rem",
        margin_bottom="1rem",
        padding="0.9rem",
        background_color=Color.CARD_EXTRAS_TOGGLE,
        border_radius="0.75rem",
        border=f"2px solid {Color.WARNING}",
    )


def _missing_notice() -> rx.Component:
    """Aviso visual cuando faltan elementos por seleccionar."""
    return rx.cond(
        ~FormBaseState.can_send,
        rx.box(
            rx.hstack(
                rx.icon(tag="circle-alert", color=Color.WARNING, size=20),
                rx.text(
                    "Falta",
                    rx.cond(
                        FormBaseState.total_missing == 1,
                        rx.fragment(" 1 elemento "),
                        rx.fragment(f" {FormBaseState.total_missing} elementos "),
                    ),
                    "por seleccionar: ",
                    rx.cond(
                        FormBaseState.missing_pizza_rosca > 0,
                        rx.el.span(
                            f"{FormBaseState.missing_pizza_rosca} pizza/rosca ",
                            style={"color": Color.ERROR, "font_weight": "600"},
                        ),
                        rx.fragment(),
                    ),
                    rx.cond(
                        FormBaseState.missing_drinks > 0,
                        rx.el.span(
                            f"{FormBaseState.missing_drinks} bebida",
                            style={"color": Color.ERROR, "font_weight": "600"},
                        ),
                        rx.fragment(),
                    ),
                    font_size="0.95rem",
                    color=Color.PURPLE_DARK,
                ),
                spacing="2",
                align_items="center",
            ),
            margin_top="0.5rem",
            margin_bottom="1rem",
            padding="0.9rem 1rem",
            background_color="#FEF3C7",
            border=f"1px solid {Color.WARNING}",
            border_radius="0.75rem",
            width="100%",
        ),
        rx.fragment(),
    )


def _submit_button() -> rx.Component:
    """Botón de envío a WhatsApp."""
    return rx.button(
        "ENVIAR PEDIDO",
        rx.image(
            src="/whatsapp_ico.ico",
            width="22px",
            height="22px",
            margin_left="0.75rem",
        ),
        type="submit",
        width="100%",
        background_color="#25D366",
        color=Color.WHITE,
        font_weight="700",
        font_size="1.1rem",
        padding="1.1rem 2rem",
        border_radius=BorderRadius.FULL,
        box_shadow="0 10px 20px -5px rgba(37, 211, 102, 0.45)",
        transition=Transition.SMOOTH,
        _hover={
            "background_color": "#1FB959",
            "transform": "translateY(-2px)",
            "box_shadow": "0 14px 28px -5px rgba(37, 211, 102, 0.55)",
        },
        _disabled={"opacity": 0.6, "cursor": "not-allowed"},
        disabled=~FormBaseState.can_send,
    )


def pack_form(
    pack_type: str = "",
    image_url: str = "",
    name_title: str = "",
    date_time: str = "",
    time_description: str = "",
    sandwiches_text: str = "",
    food_options: list[str] = [],
    pack_description: str = "",
    tortilla_description: str = "",
    pizza_title: str = "",
    pizza_description: str = "",
    drink_title: str = "",
    drink_description: str = "",
    extra_title: str = "",
    extra_description: str = "",
    bakery_title: str = "",
    bakery_options: list[str] = [],
    observation_title: str = "",
    child_name_value: str = "",
    child_age_value: str = "",
    birth_date_value: str = "",
    birth_time_value: str = "",
    pizza_selected_value: dict = {},
    rosca_selected_value: dict = {},
    drink_selected_value: dict = {},
    extra_selected: str = "",
    observation_selected_value: str = "",
    max_allowed: int = 3
) -> rx.Component:
    return rx.fragment(
        _alert_dialog(),
        rx.el.form(
            rx.el.div(
                _header_card(image_url, pack_description),
                _section_card(
                    "Tu reserva",
                    _reserva_content(),
                    icon_tag="ticket",
                    bg_color=Color.CARD_PINK,
                ),
                _section_card(
                    "Datos del cumpleañero",
                    datos_personales(name_title, child_name_value, child_age_value, date_time, time_description, birth_date_value),
                    icon_tag="user",
                ),
                _section_card(
                    "Comida",
                    seleccion_alimentos(sandwiches_text, food_options, tortilla_description),
                    icon_tag="utensils-crossed",
                ),
                _section_card(
                    "Pizzas y Roscas",
                    seleccion_pizzas(pizza_title, pizza_description, pizza_selected_value, rosca_selected_value, max_allowed),
                    icon_tag="pizza",
                ),
                _section_card(
                    "Bebidas",
                    seleccion_bebidas(drink_title, drink_description, drink_selected_value, max_allowed),
                    icon_tag="cup-soda",
                ),
                _extras_toggle(),
                rx.cond(
                    FormBaseState.show_extras,
                    _section_card(
                        "Extras",
                        seleccion_extras(
                            FormBaseState.extra_pizza_selected,
                            FormBaseState.extra_rosca_selected,
                            FormBaseState.extra_drink_selected,
                            FormBaseState.candy_count,
                        ),
                        icon_tag="sparkles",
                        bg_color=Color.CARD_EXTRAS,
                    ),
                ),
                _section_card(
                    "Repostería y Observaciones",
                    extras_y_observaciones(
                        extra_title,
                        extra_description,
                        extra_selected,
                        bakery_title,
                        bakery_options,
                        observation_title,
                        observation_selected_value,
                    ),
                    icon_tag="cake",
                ),
                _missing_notice(),
                _submit_button(),
                width="100%",
                align="center",
            ),
            on_submit=FormBaseState.send_whatsapp_message,
            reset_on_submit=True,
            class_name="max-w-3xl mx-auto my-8 p-4 md:p-6",
            style={
                "background": "linear-gradient(180deg, #FFFFFF 0%, #F7F4FA 100%)",
                "border_radius": "1.5rem",
                "box_shadow": Shadow.FORM,
            },
        )
    )


# Función para la sección de datos personales
def datos_personales(name_title, child_name_value, child_age_value, date_time, time_description, birth_date_value):
    return rx.vstack(
        _question(name_title),
        rx.flex(
            rx.input(
                placeholder="Nombre",
                value=child_name_value,
                on_change=lambda new_value: FormBaseState.update_field("child_name", new_value),
                height="40px",
                font_size="16px",
                background_color=Color.WHITE,
                border="1px solid rgba(124, 58, 237, 0.25)",
                border_radius="0.5rem",
                flex="1 1 200px",
                min_width="150px",
            ),
            rx.input(
                placeholder="Edad",
                value=child_age_value,
                on_change=lambda new_value: FormBaseState.update_field("child_age", new_value),
                height="40px",
                font_size="16px",
                type="number",
                background_color=Color.WHITE,
                border="1px solid rgba(124, 58, 237, 0.25)",
                border_radius="0.5rem",
                flex="0 1 100px",
                min_width="80px",
            ),
            wrap="wrap",
            width="100%",
            gap="1rem",
        ),
        _question(date_time, margin_top="1.5rem"),
        _hint(time_description),
        rx.flex(
            rx.input(
                placeholder="Fecha",
                type="date",
                value=birth_date_value,
                on_change=lambda new_value: FormBaseState.update_field("birth_date", new_value),
                height="40px",
                font_size="16px",
                background_color=Color.WHITE,
                border="1px solid rgba(124, 58, 237, 0.25)",
                border_radius="0.5rem",
                flex="1 1 180px",
                min_width="150px",
            ),
            rx.select(
                ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"],
                name="birth_time",
                placeholder="Hora",
                on_change=lambda new_value: FormBaseState.update_field("birth_time", new_value),
                size="3",
                value=FormBaseState.birth_time,
                height="40px",
                font_size="16px",
                flex="1 1 180px",
                min_width="150px",
            ),
            wrap="wrap",
            width="100%",
            gap="1rem",
        ),
        width="100%",
    )


# Función para la selección de alimentos
def seleccion_alimentos(sandwiches_text, food_options, tortilla_description):
    return rx.vstack(
        _question(sandwiches_text),
        rx.hstack(
            rx.checkbox(
                checked=FormBaseState.butter_on_sandwiches,
                on_change=lambda new_value: FormBaseState.update_field("butter_on_sandwiches", new_value),
                size="3",
                color_scheme="purple",
            ),
            rx.text(
                "Marcar si desea que los bocadillos lleven mantequilla",
                style={
                    "font_size": "15px",
                    "font_style": "italic",
                    "color": Color.ERROR,
                    "font_weight": "600",
                },
            ),
            align_items="center",
            spacing="3",
            margin_top="0.75rem",
        ),
        rx.flex(radio_button_food(food_options), margin_top="1rem", width="100%"),
        rx.cond(
            tortilla_description != "",
            rx.text(
                tortilla_description,
                size="3",
                weight="bold",
                style={"font_style": "italic"},
                margin_top="1.25rem",
                color_scheme="purple",
            ),
            rx.fragment(),
        ),
        width="100%",
    )


# Función para la selección de pizzas y roscas con inputs pequeños (1 dígito)
def seleccion_pizzas(pizza_title, pizza_description, pizza_selected_values, rosca_selected_values, max_allowed):
    pizza_types = ["margarita", "prosciutto", "salchicha", "pepperoni", "atún"]
    rosca_types = ["mixta", "atún", "lomo", "catalana"]

    # Ensure pizza_selected_values is a dictionary
    if not isinstance(pizza_selected_values, dict):
        pizza_selected_values = {pizza_type: 0 for pizza_type in pizza_types}

    # Ensure rosca_selected_values is a dictionary
    if not isinstance(rosca_selected_values, dict):
        rosca_selected_values = {rosca_type: 0 for rosca_type in rosca_types}

    pizza_inputs = [
        _option_row(
            str(pizza_selected_values.get(pizza_type, 0)),
            lambda new_value, pt=pizza_type: FormBaseState.update_pizza_selected(pt, new_value),
            pizza_type,
        )
        for pizza_type in pizza_types
    ]

    rosca_inputs = [
        _option_row(
            str(rosca_selected_values.get(rosca_type, 0)),
            lambda new_value, rt=rosca_type: FormBaseState.update_rosca_selected(rt, new_value),
            rosca_type,
        )
        for rosca_type in rosca_types
    ]

    return rx.vstack(
        _question(pizza_title),
        _hint(pizza_description),
        rx.flex(
            rx.vstack(
                rx.text("Pizzas", weight="bold", color=Color.PINK, margin_bottom="0.25rem"),
                *pizza_inputs,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            rx.vstack(
                rx.text("Roscas", weight="bold", color=Color.PINK, margin_bottom="0.25rem"),
                *rosca_inputs,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            gap="2rem",
            wrap="wrap",
            width="100%",
            margin_top="0.75rem",
        ),
        width="100%",
    )


# Función para la selección de bebidas
def seleccion_bebidas(drink_title, drink_description, drink_selected_values, max_allowed):
    drink_types_col1 = ["Cola", "Cola Zero", "Cola Zero Zero", "Fanta Naranja", "Fanta Limón"]
    drink_types_col2 = ["Zumo de Piña", "Zumo de Melocotón", "Batido de Chocolate", "Batido de Fresa", "Botella de Agua"]

    # Ensure drink_selected_values is a dictionary
    if not isinstance(drink_selected_values, dict):
        drink_selected_values = {drink_type: 0 for drink_type in drink_types_col1 + drink_types_col2}

    drink_inputs_col1 = [
        _option_row(
            str(drink_selected_values.get(drink_type, 0)),
            lambda new_value, dt=drink_type: FormBaseState.update_drink_selected(dt, new_value),
            drink_type,
        )
        for drink_type in drink_types_col1
    ]

    drink_inputs_col2 = [
        _option_row(
            str(drink_selected_values.get(drink_type, 0)),
            lambda new_value, dt=drink_type: FormBaseState.update_drink_selected(dt, new_value),
            drink_type,
        )
        for drink_type in drink_types_col2
    ]

    return rx.vstack(
        _question(drink_title),
        _hint(drink_description),
        rx.flex(
            rx.vstack(
                rx.text("Refrescos", weight="bold", color=Color.PINK, margin_bottom="0.25rem"),
                *drink_inputs_col1,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            rx.vstack(
                rx.text("Zumos, batidos, agua", weight="bold", color=Color.PINK, margin_bottom="0.25rem"),
                *drink_inputs_col2,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            gap="2rem",
            wrap="wrap",
            width="100%",
            margin_top="0.75rem",
        ),
        width="100%",
    )


# Función para extras y observaciones
def extras_y_observaciones(extra_title, extra_description, extra_selected, bakery_title, bakery_options, observation_title, observation_selected_value):
    return rx.vstack(
        _question(bakery_title),
        rx.flex(radio_button_bakery(bakery_options), margin_top="0.75rem", width="100%"),

        # Input de peso para Tarta Panadería
        rx.cond(
            FormBaseState.selected_bakery_option.lower().contains("tarta panadería"),
            rx.hstack(
                rx.text("Peso aproximado (kg):", weight="medium"),
                rx.input(
                    value=FormBaseState.bakery_weight.to_string(),
                    on_change=FormBaseState.update_bakery_weight,
                    type="number",
                    width="100px",
                    min="0",
                    step="0.1",
                    background_color=Color.WHITE,
                    border="1px solid rgba(124, 58, 237, 0.25)",
                    border_radius="0.5rem",
                ),
                align_items="center",
                spacing="2",
                margin_top="0.75rem",
            ),
            rx.fragment(),
        ),

        # Precio de la repostería
        rx.hstack(
            rx.text("Precio Repostería:", weight="bold"),
            rx.text(f"{FormBaseState.bakery_price:.2f}€", weight="bold", color=Color.PINK),
            margin_top="0.75rem",
            spacing="2",
        ),

        rx.divider(margin_y="1rem"),

        _question(observation_title),
        rx.text_area(
            placeholder="Observaciones",
            value=observation_selected_value,
            on_change=lambda new_value: FormBaseState.update_field("observation_selected", new_value),
            width="100%",
            height="80px",
            margin_top="0.75rem",
            background_color=Color.WHITE,
            border="1px solid rgba(124, 58, 237, 0.25)",
            border_radius="0.5rem",
        ),
        width="100%",
    )


# Función para aceptar condiciones
def aceptar_condiciones():
    return rx.vstack(
        rx.checkbox(
            rx.text(
                "He leído y acepto las condiciones. (acepte para poder enviar el pedido)",
                color="black", font_size="14px", font_weight="bold", margin_bottom="20px"
            ),
            on_change=lambda new_value: FormBaseState.update_field("conditions_acepted", new_value),
            required=True
        ),
        spacing="2", margin_top="20px"
    )


# Función para seleccionar el pack
def select_pack_component():
    return rx.vstack(
        rx.select.root(
            rx.select.trigger(placeholder="Selecciona un pack", width="100%"),
            rx.select.content(
                rx.select.item("Pack 15", value="Pack_15"),
                rx.select.item("Pack 20", value="Pack_20"),
                rx.select.item("Pack 25", value="Pack_25"),
                rx.select.item("Pack 30", value="Pack_30"),
            ),
            on_change=lambda value: FormBaseState.select_pack(value),
            width="100%",
        ),
        rx.text(
            "Máximo permitido: {FormBaseState.max_allowed_pizza_rosca}",
            key="max_allowed_text",
        ),
    )


# Función para la selección de extras (comida y bebida)
def seleccion_extras(extra_pizza_selected, extra_rosca_selected, extra_drink_selected, candy_count):
    pizza_types = ["margarita", "prosciutto", "salchicha", "pepperoni", "atún"]
    rosca_types = ["mixta", "atún", "lomo", "catalana"]
    drink_types_col1 = ["Cola", "Cola Zero", "Cola Zero Zero", "Fanta Naranja", "Fanta Limón"]
    drink_types_col2 = ["Zumo de Piña", "Zumo de Melocotón", "Batido de Chocolate", "Batido de Fresa", "Botella de Agua"]

    # Ensure dictionaries
    if not isinstance(extra_pizza_selected, dict):
        extra_pizza_selected = {pizza_type: 0 for pizza_type in pizza_types}
    if not isinstance(extra_rosca_selected, dict):
        extra_rosca_selected = {rosca_type: 0 for rosca_type in rosca_types}
    if not isinstance(extra_drink_selected, dict):
        extra_drink_selected = {drink_type: 0 for drink_type in drink_types_col1 + drink_types_col2}

    pizza_inputs = [
        _option_row(
            str(extra_pizza_selected.get(pizza_type, 0)),
            lambda new_value, pt=pizza_type: FormBaseState.update_extra_pizza_selected(pt, new_value),
            pizza_type,
            price=rx.cond(
                pizza_type == "margarita",
                f"{FormBaseState.price_extra_pizza_margarita}€",
                f"{FormBaseState.price_extra_pizza_general}€",
            ),
            max_length=2,
        )
        for pizza_type in pizza_types
    ]

    rosca_inputs = [
        _option_row(
            str(extra_rosca_selected.get(rosca_type, 0)),
            lambda new_value, rt=rosca_type: FormBaseState.update_extra_rosca_selected(rt, new_value),
            rosca_type,
            price=f"{FormBaseState.price_extra_pizza_general}€",
            max_length=2,
        )
        for rosca_type in rosca_types
    ]

    drink_inputs_col1 = [
        _option_row(
            str(extra_drink_selected.get(drink_type, 0)),
            lambda new_value, dt=drink_type: FormBaseState.update_extra_drink_selected(dt, new_value),
            drink_type,
            price=f"{FormBaseState.price_extra_drink_general}€",
            max_length=2,
        )
        for drink_type in drink_types_col1
    ]

    drink_inputs_col2 = [
        _option_row(
            str(extra_drink_selected.get(drink_type, 0)),
            lambda new_value, dt=drink_type: FormBaseState.update_extra_drink_selected(dt, new_value),
            drink_type,
            price=(
                f"{FormBaseState.price_extra_water}€"
                if "agua" in drink_type.lower()
                else f"{FormBaseState.price_extra_drink_general}€"
            ),
            max_length=2,
        )
        for drink_type in drink_types_col2
    ]

    return rx.vstack(
        _hint("Selecciona las unidades adicionales que desees añadir a tu pedido."),

        # Sección Comida
        rx.text("Pizzas y Roscas", weight="bold", color=Color.PINK, margin_top="1rem"),
        rx.flex(
            rx.vstack(
                rx.text("Pizzas", weight="bold", color=Color.PURPLE_DARK, margin_bottom="0.25rem"),
                *pizza_inputs,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            rx.vstack(
                rx.text("Roscas", weight="bold", color=Color.PURPLE_DARK, margin_bottom="0.25rem"),
                *rosca_inputs,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            gap="2rem",
            wrap="wrap",
            width="100%",
            margin_top="0.5rem",
        ),

        rx.divider(margin_y="1rem"),

        # Sección Bebidas
        rx.text("Bebidas", weight="bold", color=Color.PINK),
        _hint("(tenga en cuenta que los cafés, bebidas alcohólicas etc. van aparte)"),
        rx.flex(
            rx.vstack(
                rx.text("Refrescos", weight="bold", color=Color.PURPLE_DARK, margin_bottom="0.25rem"),
                *drink_inputs_col1,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            rx.vstack(
                rx.text("Zumos, batidos, agua", weight="bold", color=Color.PURPLE_DARK, margin_bottom="0.25rem"),
                *drink_inputs_col2,
                align_items="start",
                flex="1 1 200px",
                min_width="180px",
            ),
            gap="2rem",
            wrap="wrap",
            width="100%",
            margin_top="0.5rem",
        ),

        rx.divider(margin_y="1rem"),

        # Sección Chuches
        rx.text("Chuches", weight="bold", color=Color.PINK),
        _option_row(
            candy_count.to_string(),
            FormBaseState.update_candy_count,
            "Plato de Chuches",
            price=f"{FormBaseState.price_candy}€",
            max_length=2,
        ),

        rx.divider(margin_y="1rem"),

        # Totales
        rx.vstack(
            _total_row("Total Extras Comida:", FormBaseState.total_extra_food_price),
            _total_row("Total Extras Bebida:", FormBaseState.total_extra_drink_price),
            _total_row("Total Extras Chuches:", FormBaseState.total_candy_price),
            rx.divider(margin_y="0.5rem"),
            rx.hstack(
                rx.text("TOTAL EXTRAS:", weight="bold", size="4"),
                rx.text(
                    f"{FormBaseState.total_extra_food_price + FormBaseState.total_extra_drink_price + FormBaseState.total_candy_price:.2f}€",
                    weight="bold",
                    size="5",
                    color=Color.PINK,
                ),
                justify_content="space-between",
                width="100%",
            ),
            width="100%",
        ),
        width="100%",
    )