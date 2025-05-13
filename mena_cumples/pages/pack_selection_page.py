import reflex as rx
from mena_cumples.styles.styles import Size
from mena_cumples.states.state import State
from mena_cumples.components.navbar import navbar # Importar navbar
from mena_cumples.components.footer import footer # Importar footer



# Datos de los packs
PACK_OPTIONS_DATA = [
    {
        "title": "PACK DE 90€---PARA 15 PERSONAS",
        "image_src": "/pack_15_image.webp", # Necesitarás crear esta imagen
        "on_click": State.navigate_to_15,
    },
    {
        "title": "PACK DE 120€---PARA 20 PERSONAS",
        "image_src": "/pack_20_image.webp", # Necesitarás crear esta imagen
        "on_click": State.navigate_to_20,
    },
    {
        "title": "PACK DE 150€---PARA 25 PERSONAS",
        "image_src": "/pack_25_image.webp", # Necesitarás crear esta imagen
        "on_click": State.navigate_to_25,
    },
    {
        "title": "PACK DE 180€---PARA 30 PERSONAS",
        "image_src": "/pack_30_image.jpeg", # Necesitarás crear esta imagen
        "on_click": State.navigate_to_30,
    },
]

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


def _create_pack_card(title: str, image_src: str, on_click_action: callable = None) -> rx.Component:
    """Crea una card para un pack específico."""
    return rx.card(
        rx.vstack(
            rx.image(
                src=image_src,
                width="100%",
                height="200px", # Ajusta la altura según tus imágenes
                object_fit="cover",
                border_radius="10px 10px 0 0" # Redondea solo las esquinas superiores de la imagen
            ),
            rx.text(
                title,
                weight="bold",
                align="center",
                padding_y=Size.SMALL.value,
                padding_x=Size.SMALL.value,
                size="4" # Ajusta el tamaño del texto si es necesario
            ),
            rx.button(
                rx.text("Selecciona"),
                variant="surface",
                color_scheme="plum",
                width="90%", # Un poco menos del 100% para que no toque los bordes de la card
                margin_top=Size.SMALL.value,
                margin_bottom=Size.SMALL.value, # Añadir margen inferior al botón
                on_click=on_click_action if on_click_action else lambda: None,
                disabled=not on_click_action, # Deshabilita el botón si no hay acción
            ),
            spacing="1",
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
            rx.grid(
                *[
                    _create_pack_card(
                        title=pack["title"],
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

@rx.page(route="/pack_selection")
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