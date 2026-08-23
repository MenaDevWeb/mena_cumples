import reflex as rx
from mena_cumples.styles.styles import Size, Color, FontSize, BorderRadius, Shadow, Transition
from mena_cumples.states.state import State
from mena_cumples.states.form_state import FormBaseState
from mena_cumples.components.navbar import navbar
from mena_cumples.components.footer import footer
from mena_cumples.data.conditions import CONDITIONS
from ..routes import Routes


@rx.page(route=Routes.PACK_SELECTION.value)
def pack_selection() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.box(
                navbar(),
                class_name=Color.GRADIENT_NAVBAR,
                padding_y=Size.XS.value,
                padding_x=Size.SMALL.value,
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    pack_options_grid(),
                    rx.cond(
                        FormBaseState.code_locked,
                        rx.box(
                            rx.text(
                                f"Reserva con código {FormBaseState.reservation_code} cargada. "
                                "Elige tu pack para continuar.",
                                weight="bold",
                                color=Color.PURPLE_DARK,
                            ),
                            padding=Size.SMALL.value,
                            border_radius=BorderRadius.SMALL,
                            background_color=Color.CARD_PINK,
                        ),
                        rx.fragment(),
                    ),
                    spacing="7",
                    align="center",
                    width="100%",
                    padding_y=Size.LARGE.value,
                ),
                width="100%",
                flex_grow="1",
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.box(
                footer(),
                class_name=Color.GRADIENT_NAVBAR,
                padding_y=Size.MEDIUM.value,
                width="100%",
                margin_top="auto",
            ),
            min_height="100vh",
            width="100%",
            display="flex",
            flex_direction="column",
            background_color=Color.PAGE_BG,
            on_mount=FormBaseState.ensure_order_access,
        ),
        conditions_modal(),
    )


def conditions_modal() -> rx.Component:
    """Modal de condiciones obligatorio antes de seleccionar pack.

    Solo se muestra si el cliente no las ha aceptado aún (llega con el
    enlace directo que ya trae el código). No se puede cerrar sin aceptar.
    """
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                "Condiciones del cumpleaños",
                color=Color.PURPLE_DARK,
            ),
            rx.text(
                "Debes aceptar las condiciones para poder continuar con tu pedido.",
                color=Color.PURPLE,
                font_size=FontSize.SMALL,
                margin_bottom="1rem",
            ),
            rx.box(
                rx.vstack(
                    *[
                        rx.hstack(
                            rx.icon(tag="check", color=Color.PURPLE, size=16),
                            rx.text(
                                cond,
                                font_size=FontSize.SMALL,
                                color=Color.PURPLE_DARK,
                            ),
                            align_items="flex-start",
                            spacing="2",
                        )
                        for cond in CONDITIONS
                    ],
                    spacing="2",
                    align_items="stretch",
                    width="100%",
                ),
                max_height="50vh",
                overflow_y="auto",
                padding_right="0.5rem",
                margin_bottom="1rem",
            ),
            rx.checkbox(
                rx.text(
                    "He leído y acepto las condiciones.",
                    color=Color.PURPLE_DARK,
                    font_weight="600",
                ),
                checked=State.conditions_checked,
                on_change=State.set_conditions_checked,
                color_scheme="purple",
            ),
            rx.hstack(
                rx.button(
                    "Aceptar y continuar",
                    on_click=State.accept_conditions,
                    disabled=~State.conditions_checked,
                    background_color=Color.PURPLE,
                    color=Color.WHITE,
                    font_weight="700",
                    border_radius=BorderRadius.FULL,
                    width="100%",
                    _disabled={"opacity": 0.5, "cursor": "not-allowed"},
                    _hover={"background_color": Color.PURPLE_DARK},
                ),
                width="100%",
                margin_top="1rem",
            ),
            rx.text(
                rx.link(
                    "Volver al inicio",
                    href=Routes.INDEX.value,
                    color=Color.PINK,
                ),
                align="center",
                margin_top="0.75rem",
                font_size=FontSize.SMALL,
            ),
            background_color=Color.WHITE,
            padding="1.5rem",
            border_radius="1rem",
            max_width="36rem",
            width="100%",
        ),
        open=~State.conditions_acepted,
        modal=True,
    )



def main_title() -> rx.Component:    
    return rx.flex(  
        rx.vstack(
            rx.image(
                src="/pedido_ic.png", 
                width="300px", 
                height="auto",
                # margin_top="20px" # Eliminado para control centralizado del espaciado
            ),
            align="center", # Asegura que la imagen esté centrada en este vstack
        ),
        width="100%",
        justify_content="center"    
    )


def _create_pack_card(title: str, price: int, num_people: int, image_src: str, on_click_action: str | None = None, delay: str = "0s") -> rx.Component:
    # Si el código de reserva viene del enlace de WhatsApp, se arrastra al
    # formulario del pack para que el cliente no tenga que volver a teclearlo.
    href = on_click_action if on_click_action else "#"
    if on_click_action:
        href = rx.cond(
            FormBaseState.code_locked,
            f"{on_click_action}?codigo={FormBaseState.reservation_code}",
            on_click_action,
        )
    button_or_link = rx.link(
        rx.button(
            rx.text("Selecciona"),
            variant="surface",
            color_scheme="plum",
            width="100%",
        ),
        href=href,
        is_external=False,
        width="90%",
        margin_top=Size.SMALL.value,
        margin_bottom=Size.SMALL.value,
        style={"text_decoration": "none"},
        ) if on_click_action else rx.button(
        rx.text("Selecciona"),
        variant="surface", color_scheme="plum", width="90%",
        margin_top=Size.SMALL.value, margin_bottom=Size.SMALL.value,
        disabled=True,
    )

    return rx.card(
        rx.vstack(
            rx.image(
                src=image_src,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="10px 10px 0 0"
            ),
            rx.text(
                f"PACK DE {num_people} PERSONAS",
                weight="bold",
                align="center",
                size="5",
                margin_top="0.5rem",
            ),
            rx.vstack(
                rx.text(f"{price}€", weight="bold", size="6", color=Color.PURPLE),
                spacing="1",
                align="center",
                padding_y="0.5rem",
            ),
            button_or_link,
            spacing="2",
            align="center",
            width="100%"
        ),
        variant="surface",
        border_radius=BorderRadius.CARD,
        width="100%",
        box_shadow=Shadow.CARD,
        transition=Transition.CARD,
        class_name="card-hover",
        style={"animation_delay": delay},
    )



def _tipo_cumple_selector() -> rx.Component:
    """Selector Cumple Mediodía vs Tarde — mismo pack/precio, distinta carta/horario."""
    return rx.box(
        rx.vstack(
            rx.text(
                "Elige tipo de cumple",
                weight="bold",
                size="5",
                color=Color.PURPLE_DARK,
                align="center",
            ),
            rx.text(
                "Mismo precio. Mediodía usa menú con bebida (13:00-15:00). Tarde usa pizzas/roscas (16:00-19:00).",
                size="2",
                color=Color.PURPLE,
                align="center",
                style={"font_style": "italic"},
            ),
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="sun", size=18),
                        rx.text("Cumple Mediodía"),
                        rx.text("13:00-15:00", size="1", color=Color.PURPLE_DARK),
                        spacing="2",
                        align="center",
                    ),
                    on_click=lambda: FormBaseState.set_cumple_tipo("Cumple Mediodía"),
                    variant=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Mediodía",
                        "solid",
                        "outline",
                    ),
                    color_scheme=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Mediodía",
                        "amber",
                        "gray",
                    ),
                    size="3",
                    style={"flex": "1"},
                ),
                rx.button(
                    rx.hstack(
                        rx.icon(tag="moon", size=18),
                        rx.text("Cumple Tarde"),
                        rx.text("16:00-19:00", size="1", color=Color.PURPLE_DARK),
                        spacing="2",
                        align="center",
                    ),
                    on_click=lambda: FormBaseState.set_cumple_tipo("Cumple Tarde"),
                    variant=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Tarde",
                        "solid",
                        "outline",
                    ),
                    color_scheme=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Tarde",
                        "cyan",
                        "gray",
                    ),
                    size="3",
                    style={"flex": "1"},
                ),
                spacing="4",
                width="100%",
                margin_top="0.75rem",
            ),
            rx.box(
                rx.cond(
                    FormBaseState.cumple_tipo == "Cumple Mediodía",
                    rx.hstack(
                        rx.icon(tag="info", size=16, color="#b45309"),
                        rx.text(
                            "Has elegido Cumple Mediodía. El formulario mostrará menú (4 opciones) con cantidad + nota por producto.",
                            size="2",
                            color="#92400e",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.hstack(
                        rx.icon(tag="info", size=16, color="#0891b2"),
                        rx.text(
                            "Has elegido Cumple Tarde. El formulario mostrará bocadillos, pizzas/roscas y bebidas.",
                            size="2",
                            color="#0e7490",
                        ),
                        spacing="2",
                        align="center",
                    ),
                ),
                margin_top="0.5rem",
                padding="0.6rem 0.8rem",
                background_color=rx.cond(
                    FormBaseState.cumple_tipo == "Cumple Mediodía",
                    "#fffbeb",
                    "#ecfeff",
                ),
                border_radius="0.5rem",
                width="100%",
            ),
            spacing="2",
            width="100%",
        ),
        padding="1rem",
        background_color=Color.WHITE,
        border_radius=BorderRadius.MEDIUM,
        border=f"1px solid {Color.GRAY_BORDER}",
        box_shadow=Shadow.CARD,
        max_width="800px",
        width="100%",
        margin_bottom="1rem",
    )


def _create_mediodia_pack_card(pack: dict, index: int) -> rx.Component:
    """Card para Cumple Mediodía — mismo precio que tarde pero con menú + nota por producto."""
    # href con tipo=mediodia para que init_pack_page preseleccione Cumple Mediodía
    base_href = pack["on_click"]
    href_tarde = rx.cond(
        FormBaseState.code_locked,
        f"{base_href}?codigo={FormBaseState.reservation_code}",
        base_href,
    )
    href_mediodia = rx.cond(
        FormBaseState.code_locked,
        f"{base_href}?codigo={FormBaseState.reservation_code}&tipo=mediodia",
        f"{base_href}?tipo=mediodia",
    )
    # Usamos href_mediodia para esta variante
    button = rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="sun", size=16),
                rx.text("Mediodía"),
                spacing="1",
                align="center",
            ),
            variant="solid",
            color_scheme="amber",
            width="100%",
        ),
        href=href_mediodia,
        is_external=False,
        width="90%",
        margin_top=Size.SMALL.value,
        margin_bottom=Size.SMALL.value,
        style={"text_decoration": "none"},
    )
    return rx.card(
        rx.vstack(
            rx.box(
                rx.image(
                    src="/packs_image.webp",
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_radius="10px 10px 0 0",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="sun", size=14, color="white"),
                        rx.text("MEDIODÍA", size="1", weight="bold", color="white"),
                        rx.text("13:00-15:00", size="1", color="white"),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="10px",
                    left="10px",
                    background_color="#f59e0b",
                    padding="0.3rem 0.6rem",
                    border_radius="9999px",
                ),
                position="relative",
                width="100%",
            ),
            rx.text(
                f"PACK DE {pack['num_people']} PERSONAS",
                weight="bold",
                align="center",
                size="5",
                margin_top="0.5rem",
            ),
            rx.text(
                "Menú a elegir + bebida incluida",
                size="2",
                color="#92400e",
                align="center",
                style={"font_style": "italic"},
            ),
            rx.vstack(
                rx.text(f"{pack['price']}€", weight="bold", size="6", color="#f59e0b"),
                spacing="1",
                align="center",
                padding_y="0.5rem",
            ),
            button,
            spacing="2",
            align="center",
            width="100%",
        ),
        variant="surface",
        border_radius=BorderRadius.CARD,
        width="100%",
        box_shadow=Shadow.CARD,
        transition=Transition.CARD,
        class_name="card-hover",
        style={"animation_delay": f"{index * 0.15}s", "border": "2px solid #fde68a"},
    )


def _create_mediodia_single_card() -> rx.Component:
    """1 pack único Mediodía — mismo tamaño que packs Tarde, con menú + nota."""
    mediodia_href = rx.cond(
        FormBaseState.code_locked,
        f"{Routes.PACK_MEDIODOIA.value}?codigo={FormBaseState.reservation_code}&tipo=mediodia",
        f"{Routes.PACK_MEDIODOIA.value}?tipo=mediodia",
    )
    return rx.card(
        rx.vstack(
            rx.box(
                rx.image(
                    src="/packs_image.webp",
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_radius="10px 10px 0 0",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="sun", size=14, color="white"),
                        rx.text("MEDIODÍA", size="1", weight="bold", color="white"),
                        rx.text("13:00-15:00", size="1", color="white"),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="10px",
                    left="10px",
                    background_color="#f59e0b",
                    padding="0.3rem 0.6rem",
                    border_radius="9999px",
                ),
                position="relative",
                width="100%",
            ),
            rx.text(
                "PACK MEDIODÍA",
                weight="bold",
                align="center",
                size="5",
                margin_top="0.5rem",
            ),
            rx.text(
                "Menú a elegir + bebida incluida",
                size="2",
                color="#92400e",
                align="center",
                style={"font_style": "italic"},
            ),
            rx.vstack(
                rx.text("4 menús · con nota por producto", size="2", color=Color.PURPLE_DARK, align="center"),
                spacing="1",
                align="center",
                padding_y="0.5rem",
            ),
            rx.vstack(
                rx.text("5,90€", weight="bold", size="6", color="#f59e0b"),
                rx.text("por niño", size="2", color=Color.PURPLE_DARK),
                spacing="1",
                align="center",
            ),
            rx.link(
                rx.button(
                    rx.text("Selecciona"),
                    variant="surface",
                    color_scheme="plum",
                    width="100%",
                ),
                href=mediodia_href,
                is_external=False,
                width="90%",
                margin_top=Size.SMALL.value,
                margin_bottom=Size.SMALL.value,
                style={"text_decoration": "none"},
            ),
            spacing="2",
            align="center",
            width="100%",
        ),
        variant="surface",
        border_radius=BorderRadius.CARD,
        width="100%",
        box_shadow=Shadow.CARD,
        transition=Transition.CARD,
        class_name="card-hover",
        style={"animation_delay": "0.6s"},
    )


def pack_options_grid() -> rx.Component:
    """Crea el grid de cards para los packs — Tarde y Mediodía con mismo precio."""
    return rx.center(
        rx.vstack(
            main_title(),
            # --- Cumple Tarde (16:00-19:00) ---
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="moon", size=20, color=Color.PURPLE),
                    rx.heading(
                        "Cumple Tarde",
                        size="6",
                        color=Color.PURPLE_DARK,
                        weight="bold",
                    ),
                    rx.text(
                        "16:00-19:00 · Pizzas/roscas + bebidas",
                        size="2",
                        color=Color.PURPLE,
                        style={"font_style": "italic"},
                    ),
                    spacing="2",
                    align="center",
                    justify="center",
                    width="100%",
                ),
                rx.grid(
                    *[
                        _create_pack_card(
                            title=pack["title"],
                            price=pack["price"],
                            num_people=pack["num_people"],
                            image_src=pack["image_src"],
                            on_click_action=pack["on_click"],
                            delay=f"{i * 0.15}s",
                        )
                        for i, pack in enumerate(PACK_OPTIONS_DATA)
                    ],
                    columns=rx.breakpoints(initial="1", sm="2", md="2", lg="4"),
                    spacing="7",
                    width="100%",
                    max_width="1200px",
                    padding=Size.SMALL.value,
                ),
                spacing="3",
                width="100%",
                align="center",
            ),
            rx.divider(margin_y="1rem", width="100%", max_width="1200px"),
            # --- Cumple Mediodía (13:00-15:00) ---
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="sun", size=20, color="#f59e0b"),
                    rx.heading(
                        "Cumple Mediodía",
                        size="6",
                        color="#92400e",
                        weight="bold",
                    ),
                    rx.text(
                        "13:00-15:00 · Menú + bebida (con nota por producto)",
                        size="2",
                        color="#b45309",
                        style={"font_style": "italic"},
                    ),
                    spacing="2",
                    align="center",
                    justify="center",
                    width="100%",
                ),
                rx.text(
                    "Mismo precio que Tarde. Cada menú incluye patatas + 1 bebida. Límite = nº personas del pack. Extras y repostería iguales.",
                    size="2",
                    color="#92400e",
                    align="center",
                    max_width="800px",
                ),
                rx.center(
                    rx.box(
                        _create_mediodia_single_card(),
                        max_width="320px",
                        width="100%",
                    ),
                    width="100%",
                    padding=Size.SMALL.value,
                ),
                spacing="3",
                width="100%",
                align="center",
            ),
            width="100%",
        ),
        direction="column"
    )

# Datos de los packs
PACK_OPTIONS_DATA = [
    {
        "title": "PACK DE 110€---PARA 15 PERSONAS",
        "price": 110,
        "num_people": 15,
        "image_src": "/pack_15_image.webp",
        "on_click": Routes.PACK_15_PAX.value,
    },
    {
        "title": "PACK DE 140€---PARA 20 PERSONAS",
        "price": 140,
        "num_people": 20,
        "image_src": "/pack_20_image.webp",
        "on_click":Routes.PACK_20_PAX.value,
    },
    {
        "title": "PACK DE 170€---PARA 25 PERSONAS",
        "price": 170,
        "num_people": 25,
        "image_src": "/pack_25_image.webp",
        "on_click": Routes.PACK_25_PAX.value,
    },
    {
        "title": "PACK DE 200€---PARA 30 PERSONAS",
        "price": 200,
        "num_people": 30,
        "image_src": "/pack_30_image.jpeg",
        "on_click": Routes.PACK_30_PAX.value,
    },
]