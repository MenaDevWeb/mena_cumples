import reflex as rx


@rx.page(route="/packs_information")
def packs_information():
    """Create the page for displaying birthday packs."""
    return rx.container(
        # Contenedor para centrar la imagen del encabezado
        rx.box(
            rx.image(
                src="/packs_title.png", 
                width="500px", 
                margin_bottom="2rem",
                
                ),
            display="flex",
            justify_content="center",
            align_items="center"
        ),
        
        # Pack para 15 Personas
        rx.hstack( 
            rx.box(
                rx.image(
                    src=("/pack_15.webp"), 
                    width="280px",
                    height="auto"),
            ),            
            rx.box(
                rx.heading("Pack para 15 Personas - 90€", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.5rem"),
                rx.text("• 30 Bocadillos ó 15 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                rx.text("• A elegir o combinar: 3 Pizzas ó 3 roscas.", color="black", margin_bottom="0.5rem"),
                rx.text("• 4 Botellas de refresco.", color="black", margin_bottom="1rem"),
                padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                width="100%"
            ),
        ),

        # Pack para 20 Personas
        rx.hstack( 
            rx.box(
                rx.image(src=("/pack_20_image.webp"), width="280px", height="auto"),
            ),            
            rx.box(
                rx.heading("Pack para 20 Personas - 120€", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.5rem"),
                rx.text("• 40 Bocadillos ó 20 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                rx.text("• A elegir o combinar: 4 Pizzas ó 4 roscas.", color="black", margin_bottom="0.5rem"),
                rx.text("• 5 Botellas de refresco.", color="black", margin_bottom="1rem"),
                padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                width="100%"
            ),
        ),

        # Pack para 25 Personas
        rx.hstack( 
            rx.box(
                rx.image(src=("/pack_25_image.webp"), width="280px", height="auto"),
            ),            
            rx.box(
                rx.heading("Pack para 25 Personas - 150€", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.5rem"),
                rx.text("• 50 Bocadillos ó 25 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos", color="black", margin_bottom="0.5rem"),
                rx.text("• A elegir o combinar: 4 Pizzas ó 4 roscas + 2 Tortillas de patatas", color="black", margin_bottom="0.5rem"),
                rx.text("• 8 Botellas de refresco.", color="black", margin_bottom="1rem"),
                padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                width="100%"
            ),
        ),

        # Pack para 30 Personas
        rx.hstack( 
            rx.box(
                rx.image(src=("/pack_30.jpeg"), width="280px", height="auto"),
            ),            
            rx.box(
                rx.heading("Pack para 30 Personas - 180€", font_size="1.5rem", color="#8B5CF6", margin_bottom="0.5rem"),
                rx.text("• 60 Bocadillos ó 30 Sandwiches mixtos (o mitad y mitad)", color="black", margin_bottom="0.5rem"),
                rx.text("• Platos: patatas, palomitas, bollería/galletas y frutos secos.", color="black", margin_bottom="0.5rem"),
                rx.text("• A elegir o combinar: 5 Pizzas ó 5 roscas + 2 Tortillas de patatas.", color="black", margin_bottom="0.5rem"),
                rx.text("• 10 Botellas de refresco.", color="black", margin_bottom="1rem"),
                padding="1rem", border="2px solid #BE185D", border_radius="10px", margin_bottom="2rem",
                width="100%"
            ),
        ),

        # Extras Section
        rx.box(
            rx.heading("Extras", font_size="2rem", color="#BE185D", margin_bottom="1rem"),
            rx.text("• Pizzas o roscas extras: 6€.", margin_bottom="0.5rem"),
            rx.text("• Botellas de refresco extras: 3,50€.", color="black", margin_bottom="0.5rem"),
            rx.text("• Botella de agua extra: 2,50€.", color="black", margin_bottom="0.5rem"),
            rx.text("• Bizcocho de cafetería (normal, de chocolate, con o sin cobertura) para 8 a 10 pax: 10€.", color="black", margin_bottom="0.5rem"),
            rx.text("• Tarta de galletas de cafetería: 15€.", margin_bottom="0.5rem"),
            rx.text("• Tarta panadería: 18€ el Kg.", color="black", margin_bottom="0.5rem"),
            rx.text("• Palmera de chocolate: 25€ (Con relleno Kinder: 28€)", color="black", margin_bottom="1rem"),
            padding="1rem", border="2px solid #BE185D", border_radius="10px", color="black", background_color="#e2d5f4 "
        ),
        
        padding="1rem",
        background_color="#FDF2F8",
        border_radius="10px",
        align_items="center",
        display="flex",
        flex_direction="column",
    )