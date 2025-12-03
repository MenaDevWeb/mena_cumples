import reflex as rx
from mena_cumples.styles.styles import Size
from mena_cumples.states.state import State
from mena_cumples.components.navbar import navbar # Importar navbar
from mena_cumples.components.footer import footer # Importar footer
from ..routes import Routes # Asegúrate que Routes está importado


@rx.page(route=Routes.PACK_SELECTION.value)
def pack_selection() -> rx.Component:
    return rx.box(
        # Navbar Container
        rx.box(
            navbar(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200", # Estilo consistente
            padding_y="0.5rem", # Reduce el padding vertical (e.g., "0.5rem")
            padding_x="1rem",   # Mantenemos el padding horizontal o ajústalo si es necesario
            width="100%",
        ),
        # Main Content Container
        rx.box(
            rx.vstack(
                pack_options_grid(),
                spacing="7",  # Espacio entre main_title y pack_options_grid
                align="center",
                width="100%",
                padding_y=Size.LARGE.value, # Padding vertical arriba de main_title y abajo de pack_options_grid
            ),
            width="100%",
            flex_grow="1", # Permite que este contenedor crezca y ocupe el espacio disponible
            display="flex",
            align_items="center", # Centra el vstack verticalmente si el contenido es corto
            justify_content="center", # Centra el vstack horizontalmente (aunque width="100%" lo hace menos visible)
        ),
        # Footer Container
        rx.box(
            footer(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200", # Estilo consistente
            padding_y="2rem",
            width="100%",
            margin_top="auto", # Empuja el footer hacia abajo
        ),
        min_height="100vh", # Asegura que el rx.box ocupe al menos toda la altura de la ventana
        width="100%", # Ocupa todo el ancho
        display="flex",
        flex_direction="column", # Organiza navbar, contenido y footer verticalmente
        background_color="#EBE6EF", # Color de fondo para el área de contenido
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


def _create_pack_card(title: str, price_2025: int, price_2026: int, num_people: int, image_src: str, on_click_action: str | None = None) -> rx.Component:
    button_or_link = rx.link(
        rx.button(
            rx.text("Selecciona"),
            variant="surface",
            color_scheme="plum",
            width="100%", # El botón ocupa todo el ancho del enlace
        ),
        href=on_click_action if on_click_action else "#", # El enlace maneja la navegación
        is_external=False,
        width="90%", # Ancho del área clickeable del enlace
        margin_top=Size.SMALL.value,
        margin_bottom=Size.SMALL.value,
        style={"text_decoration": "none"}, # Para que no parezca un enlace subrayado tradicional
        disabled=not on_click_action, # rx.link no tiene 'disabled', esto es conceptual
        ) if on_click_action else rx.button( # Botón deshabilitado si no hay acción
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
                height="200px", # Ajusta la altura según tus imágenes
                object_fit="cover",
                border_radius="10px 10px 0 0" # Redondea solo las esquinas superiores de la imagen
            ),
            # Título del pack
            rx.text(
                f"PACK DE {num_people} PERSONAS",
                weight="bold",
                align="center",
                size="5",
                margin_top="0.5rem",
            ),
            # Precios
            rx.vstack(
                # Precio 2025
                rx.hstack(
                    rx.text("2025:", weight="medium", size="3", color="gray"),
                    rx.text(f"{price_2025}€", weight="bold", size="4", color="purple"),
                    spacing="2",
                    align="center",
                ),
                # Precio 2026
                rx.hstack(
                    rx.text("2026:", weight="medium", size="3", color="gray"),
                    rx.text(f"{price_2026}€", weight="bold", size="4", color="indigo"),
                    rx.badge("+20€", color_scheme="red", size="1"),
                    spacing="2",
                    align="center",
                ),
                spacing="1",
                align="center",
                padding_y="0.5rem",
            ),
            button_or_link,
            spacing="2",
            align="center",
            width="100%"
        ),
        variant="surface", # O puedes probar "outline" o "ghost"
        border_radius="15px", # Redondeo general de la card
        width="100%",
        _hover={"box_shadow": "0px 6px 12px rgba(0,0,0,0.15)"}, # Efecto hover sutil
        transition="box-shadow 0.3s ease-in-out", # Transición suave para el hover
    )



def pack_options_grid() -> rx.Component:
    """Crea el grid de cards para los packs."""
    return rx.center(
        rx.vstack(
            main_title(),
            # Nota informativa sobre precios
            rx.callout(
                "Los precios mostrados son para cumpleaños en 2025. Para reservas en 2026, el precio será 20€ superior.",
                icon="info",
                color_scheme="blue",
                size="2",
                width="100%",
                max_width="1200px",
                margin_bottom="1rem",
            ),
            rx.grid(
                *[
                    _create_pack_card(
                        title=pack["title"],
                        price_2025=pack["price_2025"],
                        price_2026=pack["price_2026"],
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
        "title": "PACK DE 90€---PARA 15 PERSONAS",
        "price_2025": 90,
        "price_2026": 110,
        "num_people": 15,
        "image_src": "/pack_15_image.webp",
        "on_click": Routes.PACK_15_PAX.value,
    },
    {
        "title": "PACK DE 120€---PARA 20 PERSONAS",
        "price_2025": 120,
        "price_2026": 140,
        "num_people": 20,
        "image_src": "/pack_20_image.webp",
        "on_click":Routes.PACK_20_PAX.value,
    },
    {
        "title": "PACK DE 150€---PARA 25 PERSONAS",
        "price_2025": 150,
        "price_2026": 170,
        "num_people": 25,
        "image_src": "/pack_25_image.webp",
        "on_click": Routes.PACK_25_PAX.value,
    },
    {
        "title": "PACK DE 180€---PARA 30 PERSONAS",
        "price_2025": 180,
        "price_2026": 200,
        "num_people": 30,
        "image_src": "/pack_30_image.jpeg",
        "on_click": Routes.PACK_30_PAX.value,
    },
]