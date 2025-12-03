import reflex as rx
# Importar navbar y footer
from mena_cumples.components.navbar import navbar
from mena_cumples.components.footer import footer
from mena_cumples.styles.styles import Size # Si usas Size para padding


@rx.page(route="/packs_information")
def packs_information():
    """Create the page for displaying birthday packs."""
    return rx.box( # Contenedor principal que ocupa toda la altura
        # Navbar Container
        rx.box(
            navbar(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200", # Estilo consistente
            padding_y="0.5rem",
            padding_x="1rem",
            width="100%",
        ),
        # Main Content Container
        rx.box(
            rx.vstack( # Contenedor VStack para el contenido principal
                # Contenedor para centrar la imagen del encabezado
                rx.box(
                    rx.image(
                        src="/packs_image.webp",
                        width="400px",
                        margin_bottom="2rem",
                    ),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    # margin_top ya no es necesario aquí si el vstack tiene padding o spacing
                ),
                # Callout informativo sobre precios
                rx.callout(
                    "📅 Precios 2025. Para reservas en 2026, todos los packs tienen un incremento de 20€.",
                    icon="info",
                    color_scheme="blue",
                    size="2",
                    width="100%",
                    max_width="800px",
                    margin_bottom="2rem",
                ),
                # Pack para 15 Personas
                rx.hstack(
                    rx.box(
                        rx.image(
                            src=("/pack_15_image.webp"),
                            width="280px",
                            height="auto"),
                    ),
                    rx.box(
                        rx.heading("Pack para 15 Personas", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.3rem"),
                        rx.hstack(
                            rx.text("2025:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("90€", weight="bold", color="#8B5CF6", font_size="1.2rem"),
                            rx.text("•", color="#6B7280", margin_x="0.5rem"),
                            rx.text("2026:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("110€", weight="bold", color="#4F46E5", font_size="1.2rem"),
                            rx.badge("+20€", color_scheme="red", size="1"),
                            spacing="2",
                            margin_bottom="0.8rem",
                        ),
                        rx.text("• 30 Bocadillos ó 15 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                        rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                        rx.text("• A elegir o combinar: 3 Pizzas ó 3 roscas.", color="black", margin_bottom="0.5rem"),
                        rx.text("• 4 Botellas de refresco.", color="black", margin_bottom="1rem"),
                        padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                        width="100%"
                    ),
                    max_width="800px", # Limitar ancho del contenido del pack
                    width="100%",
                    spacing="5",
                ),
                # Pack para 20 Personas
                rx.hstack(
                    rx.box(
                        rx.image(src=("/pack_20_image.webp"), width="280px", height="auto"),
                    ),
                    rx.box(
                        rx.heading("Pack para 20 Personas", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.3rem"),
                        rx.hstack(
                            rx.text("2025:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("120€", weight="bold", color="#8B5CF6", font_size="1.2rem"),
                            rx.text("•", color="#6B7280", margin_x="0.5rem"),
                            rx.text("2026:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("140€", weight="bold", color="#4F46E5", font_size="1.2rem"),
                            rx.badge("+20€", color_scheme="red", size="1"),
                            spacing="2",
                            margin_bottom="0.8rem",
                        ),
                        rx.text("• 40 Bocadillos ó 20 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                        rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                        rx.text("• A elegir o combinar: 4 Pizzas ó 4 roscas.", color="black", margin_bottom="0.5rem"),
                        rx.text("• 5 Botellas de refresco.", color="black", margin_bottom="1rem"),
                        padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                        width="100%"
                    ),
                    max_width="800px",
                    width="100%",
                    spacing="5",
                ),
                # Pack para 25 Personas
                rx.hstack(
                    rx.box(
                        rx.image(src=("/pack_25_image.webp"), width="280px", height="auto"),
                    ),
                    rx.box(
                        rx.heading("Pack para 25 Personas", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.3rem"),
                        rx.hstack(
                            rx.text("2025:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("150€", weight="bold", color="#8B5CF6", font_size="1.2rem"),
                            rx.text("•", color="#6B7280", margin_x="0.5rem"),
                            rx.text("2026:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("170€", weight="bold", color="#4F46E5", font_size="1.2rem"),
                            rx.badge("+20€", color_scheme="red", size="1"),
                            spacing="2",
                            margin_bottom="0.8rem",
                        ),
                        rx.text("• 50 Bocadillos ó 25 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                        rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos", color="black", margin_bottom="0.5rem"),
                        rx.text("• A elegir o combinar: 4 Pizzas ó 4 roscas + 2 Tortillas de patatas", color="black", margin_bottom="0.5rem"),
                        rx.text("• 8 Botellas de refresco.", color="black", margin_bottom="1rem"),
                        padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                        width="100%"
                    ),
                    max_width="800px",
                    width="100%",
                    spacing="5",
                ),
                # Pack para 30 Personas
                rx.hstack(
                    rx.box(
                        rx.image(src=("/pack_30_image.jpeg"), width="280px", height="auto"),
                    ),
                    rx.box(
                        rx.heading("Pack para 30 Personas", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.3rem"),
                        rx.hstack(
                            rx.text("2025:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("180€", weight="bold", color="#8B5CF6", font_size="1.2rem"),
                            rx.text("•", color="#6B7280", margin_x="0.5rem"),
                            rx.text("2026:", weight="bold", color="#6B7280", font_size="1.1rem"),
                            rx.text("200€", weight="bold", color="#4F46E5", font_size="1.2rem"),
                            rx.badge("+20€", color_scheme="red", size="1"),
                            spacing="2",
                            margin_bottom="0.8rem",
                        ),
                        rx.text("• 60 Bocadillos ó 30 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                        rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                        rx.text("• A elegir o combinar: 5 Pizzas ó 5 roscas + 2 Tortillas de patatas.", color="black", margin_bottom="0.5rem"),
                        rx.text("• 10 Botellas de refresco.", color="black", margin_bottom="1rem"),
                        padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                        width="100%"
                    ),
                    max_width="800px",
                    width="100%",
                    spacing="5",
                ),
                # Extras Section
                rx.box(
                    rx.heading("Extras", font_size="2rem", color="#BE185D", margin_bottom="1rem"),
                    rx.text("• Pizzas o roscas extras: 6€.", margin_bottom="0.5rem"),
                    rx.text("• Plato de chuches: 2€ cada uno.", margin_bottom="0.5rem"),
                    rx.text("• Botellas de refresco extras: 3,50€.", color="black", margin_bottom="0.5rem"),
                    rx.text("• Botella de agua extra: 2,50€.", color="black", margin_bottom="0.5rem"),
                    rx.text("• Bizcocho de cafetería (normal, de chocolate, con o sin cobertura) para 8 a 10 pax: 10€.", color="black", margin_bottom="0.5rem"),
                    rx.text("• Tarta de galletas de cafetería: 15€.", margin_bottom="0.5rem"),
                    rx.text("• Tarta panadería: 18€ el Kg.", color="black", margin_bottom="0.5rem"),
                    rx.text("• Palmera de chocolate: 25€ (Con relleno Kinder: 28€)", color="black", margin_bottom="1rem"),
                    padding="1rem", border="2px solid #BE185D", border_radius="10px", color="black", background_color="#e2d5f4 ",
                    max_width="800px", # Limitar ancho
                    width="100%",
                    margin_bottom=Size.LARGE.value, # Espacio inferior
                ),
                # Estilos que estaban en el rx.box de la "card" ahora se aplican aquí o se eliminan
                spacing="7", # Espaciado vertical entre elementos del vstack
                align_items="center",
                width="100%",
                max_width="900px", # Limita el ancho máximo del contenido de los packs
                padding_x="1rem", # Padding horizontal para el contenido
            ),
            # Propiedades del contenedor que envuelve el vstack
            width="100%",
            flex_grow="1", # Permite que este contenedor crezca
            display="flex",
            flex_direction="column", # Para que el contenido interno se apile verticalmente
            align_items="center", # Centra el contenido (el rx.box interno)
            padding_y=Size.LARGE.value, # Padding vertical para el área de contenido
        ),
        # Footer Container
        rx.box(
            footer(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200", # Estilo consistente
            padding_y="2rem",
            width="100%",
            margin_top="auto", # Empuja el footer hacia abajo
        ),
        min_height="100vh",
        width="100%",
        display="flex",
        flex_direction="column",
        background_color="#EBE6EF", # Color de fondo general para el área entre navbar y footer
    )