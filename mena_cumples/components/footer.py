import reflex as rx

def footer():
    """Create the website footer with copyright and social media links."""
    return rx.box(
        create_colored_text(
            text="© 2025 Developed by Gabriel Visiedo."
        ),
        rx.flex(
            create_social_link(icon_name="facebook", href="https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/"),
            create_social_link(icon_name="instagram", href="https://www.instagram.com/menaplaza/?hl=es"),
            display="flex",
            justify_content="center",
            margin_top="1rem",
            column_gap="1rem",
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
        margin_left="auto",
        margin_right="auto",
        text_align="center",
    )

def create_colored_text(text):
    """Create a paragraph with purple-colored text."""
    return rx.text(text, color="#7C3AED")


def create_social_link(icon_name,href):
    """Create a styled link with a Lucide icon for social media."""
    return rx.el.a(
        rx.icon(
            tag=icon_name,
            font_family="LucideIcons",
            font_size="1.5rem",
            color="#7C3AED",
        ),
        href=href,
        transition_duration="300ms",
        _hover={"color": "#5B21B6"},
    )  
