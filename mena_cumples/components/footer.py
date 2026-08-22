import reflex as rx
from mena_cumples.styles.styles import Color, FontSize, Transition


def footer():
    """Create the website footer with copyright and social media links."""
    return rx.box(
        rx.flex(
            create_colored_text(
                text="© 2026 Developed by Gabriel Visiedo."
            ),
            rx.flex(
                create_linked_icon(
                    icon_src="/facebook.svg",
                    href="https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/"
                ),
                create_linked_icon(
                    icon_src="/instagram.svg",
                    href="https://www.instagram.com/menaplaza/?hl=es"
                ),
                create_linked_image(
                    src="/logo_hotel.webp",
                    alt="Logo Hotel Mena Plaza",
                    href="https://www.hotelmenaplaza.es/"
                ),
                create_linked_image(
                    src="/logo_garden.webp",
                    alt="Logo Mena Garden",
                    href="https://www.hotelmenaplaza.es/mena_garden/"
                ),
                gap="1rem",
                align_items="center",
            ),
            width="100%",
            max_width="1200px",
            margin_left="auto",
            margin_right="auto",
            display="flex",
            justify_content="space-between",
            align_items="center",
            flex_wrap="wrap",
            gap="1rem",
            padding_x="1rem",
        ),
        width="100%",
    )


def create_colored_text(text):
    return rx.text(text, color=Color.PURPLE, font_size=FontSize.SMALL)


def create_linked_icon(icon_src: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.image(
            src=icon_src,
            alt="Social icon",
            width="25px",
            height="auto",
            transition=Transition.DEFAULT,
            _hover={"opacity": 0.8, "transform": "scale(1.1)"},
        ),
        href=href,
    )


def create_linked_image(src: str, href: str, alt: str = "") -> rx.Component:
    return rx.el.a(
        rx.image(
            src=src,
            alt=alt,
            width="25px",
            height="auto",
            transition=Transition.DEFAULT,
            _hover={"opacity": 0.8, "transform": "scale(1.1)"},
        ),
        href=href,
    )


def create_logo_image(src: str, alt: str) -> rx.Component:
    return rx.image(
        src=src,
        alt=alt,
        width="40px",
        height="auto",
    )
