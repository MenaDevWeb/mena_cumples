import reflex as rx
from mena_cumples.styles.styles import Size, Color, FontSize, BorderRadius, Shadow, Transition
from mena_cumples.states.state import State
from mena_cumples.components.navbar import navbar
from mena_cumples.components.footer import footer
from ..routes import Routes


@rx.page(route=Routes.PACK_SELECTION.value)
def pack_selection() -> rx.Component:
    return rx.box(
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


def _create_pack_card(title: str, price: int, num_people: int, image_src: str, on_click_action: str | None = None) -> rx.Component:
    button_or_link = rx.link(
        rx.button(
            rx.text("Selecciona"),
            variant="surface",
            color_scheme="plum",
            width="100%",
        ),
        href=on_click_action if on_click_action else "#",
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
        _hover={"box_shadow": "0px 6px 12px rgba(0,0,0,0.15)"},
        transition=Transition.SHADOW,
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
                        on_click_action=pack["on_click"]
                    )
                    for pack in PACK_OPTIONS_DATA
                ],
                columns=rx.breakpoints(initial="1", sm="2", md="2", lg="4"), # Columnas responsivas
                spacing="7", # Espaciado entre cards
                width="100%",
                max_width="1200px", # Pero se limita a 1200px
                padding=Size.MEDIUM.value, # Padding dentro del grid
            ),
            width="100%", # El center ocupa todo el ancho disponible para poder centrar el grid
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