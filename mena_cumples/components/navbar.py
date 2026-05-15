import reflex as rx
from mena_cumples.styles.styles import Color

def navbar():
    """Create the website header with logo and navigation links."""
    return rx.flex(
        rx.image(
            src="/mena_cumples.png",
            width="200px",
            height="auto",
        ),
        width="100%",
        max_width="1200px",
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
    )