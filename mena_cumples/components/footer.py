import reflex as rx

def footer():
    """Create the website footer with copyright and social media links."""
    return rx.box(
        # Copyright text (centered by the parent box's text_align)
        create_colored_text(
            text="© 2025 Developed by Gabriel Visiedo."
        ),
        rx.flex(
            # All icons/logos are now direct children of this flex container
            create_social_link(
                icon_name="facebook",
                href="https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/"
            ),
            create_social_link(
                icon_name="instagram",
                href="https://www.instagram.com/menaplaza/?hl=es"
            ),
            create_linked_image(
                src="/logo_hotel.webp",
                alt="Logo Hotel Mena Plaza",
                href="https://www.hotelmenaplaza.es/"
            ),
            create_linked_image(
                src="/logo_garden.webp", # Assuming this should also be from assets root
                alt="Logo Mena Garden",
                href="https://www.hotelmenaplaza.es/mena_garden/"
            ),
            display="flex",
            justify_content="center", # Center all items
            align_items="center", # Vertically align items in this flex
            margin_top="1rem",
            wrap="wrap", # Allow wrapping on smaller screens
            gap="1rem", # Add gap between all items
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

def create_linked_image(src: str, href: str, alt: str = "") -> rx.Component:
    """Create a styled link with an image."""
    return rx.el.a(
        rx.image(
            src=src,
            alt=alt,
            width="25px", # Keep the size consistent with create_logo_image
            height="auto",
            transition="opacity 300ms ease-in-out", # Add transition for smooth effect
            _hover={"opacity": 0.8}, # Reduce opacity on hover
        ),
        href=href,
    )

def create_logo_image(src: str, alt: str) -> rx.Component:
    """Create a styled image component for a logo."""
    return rx.image(
        src=src,
        alt=alt,
        width="40px", # Example size, adjust as needed
        height="auto",
        # Add any other desired styles, e.g., margin, border_radius
    )
