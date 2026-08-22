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



def pack_options_grid() -> rx.Component:
    """Crea el grid de cards para los packs."""
    return rx.center(
        rx.vstack(
            main_title(),
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
                padding=Size.MEDIUM.value,
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