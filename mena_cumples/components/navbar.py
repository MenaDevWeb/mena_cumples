import reflex as rx

def navbar():
    """Create the website header with logo and navigation links."""
    return rx.flex(
        rx.image(
            src="/mena_cumples.png",
            width="200px",  # Prueba con un valor mayor, e.g., "60px", "70px", "80px"
            height="auto"    # Mantenemos 'auto' para que el ancho se ajuste proporcionalmente
            
            
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
    )