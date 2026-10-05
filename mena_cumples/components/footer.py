import reflex as rx
from mena_cumples.styles.styles import Color, FontSize, Transition


def footer():
    """Pie festivo: fondo morado profundo, 3 bloques en desktop."""
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="cake", color=Color.SUNNY, size=20),
                    rx.text(
                        "Cumples Mena Plaza",
                        color=Color.WHITE,
                        font_weight="800",
                        font_size=FontSize.DEFAULT,
                    ),
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    "© 2026 Developed by Gabriel Visiedo.",
                    color="rgba(255,255,255,0.7)",
                    font_size=FontSize.SMALL,
                ),
                rx.text(
                    "Hotel Mena Plaza · Nerja",
                    color="rgba(255,255,255,0.7)",
                    font_size=FontSize.SMALL,
                ),
                spacing="1",
                align_items="start",
            ),
            rx.hstack(
                create_linked_icon(
                    icon_src="/facebook.svg",
                    href="https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/",
                ),
                create_linked_icon(
                    icon_src="/instagram.svg",
                    href="https://www.instagram.com/menaplaza/?hl=es",
                ),
                create_linked_image(
                    src="/logo_hotel.webp",
                    alt="Logo Hotel Mena Plaza",
                    href="https://www.hotelmenaplaza.es/",
                ),
                create_linked_image(
                    src="/logo_garden.webp",
                    alt="Logo Mena Garden",
                    href="https://www.hotelmenaplaza.es/mena_garden/",
                ),
                spacing="3",
                align="center",
            ),
            width="100%",
            max_width="1200px",
            margin_left="auto",
            margin_right="auto",
            justify_content="space-between",
            align_items="center",
            flex_wrap="wrap",
            gap="1.25rem",
            padding_x="1.25rem",
            padding_y="1.5rem",
        ),
        width="100%",
        background_color=Color.NAVY,
        style={"border_top": f"4px solid {Color.SUNNY}"},
    )


def create_linked_icon(icon_src: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.image(
            src=icon_src,
            alt="Social icon",
            width="28px",
            height="auto",
            transition=Transition.DEFAULT,
            style={"filter": "brightness(0) invert(1)"},
            _hover={"opacity": 0.8, "transform": "scale(1.15)"},
        ),
        href=href,
    )


def create_linked_image(src: str, href: str, alt: str = "") -> rx.Component:
    return rx.el.a(
        rx.image(
            src=src,
            alt=alt,
            width="32px",
            height="auto",
            transition=Transition.DEFAULT,
            style={"filter": "brightness(0) invert(1)"},
            _hover={"opacity": 0.8, "transform": "scale(1.15)"},
        ),
        href=href,
    )
