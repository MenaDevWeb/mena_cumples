import reflex as rx
from mena_cumples.components.navbar import navbar
from mena_cumples.components.footer import footer
from mena_cumples.styles.styles import Size, Color, FontSize


@rx.page(route="/packs_information")
def packs_information():
    return rx.box(
        rx.box(
            navbar(),
            class_name=Color.GRADIENT_NAVBAR,
            padding_y=Size.XS.value,
            padding_x=Size.SMALL.value,
            width="100%",
        ),
        rx.box(
            rx.vstack(
                rx.box(
                    rx.image(
                        src="/packs_image.webp",
                        width="400px",
                        margin_bottom=Size.MEDIUM.value,
                    ),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ),
                _create_pack_info_row(
                    "/pack_15_image.webp",
                    "Pack para 15 Personas",
                    "110€",
                    [
                        "30 Bocadillos ó 15 Sandwiches mixtos (o mitad y mitad)",
                        "Platos: patatas, palomitas, bollería/galletas y frutos secos.",
                        "A elegir o combinar: 3 Pizzas ó 3 roscas.",
                        "4 Botellas de refresco.",
                    ],
                ),
                _create_pack_info_row(
                    "/pack_20_image.webp",
                    "Pack para 20 Personas",
                    "140€",
                    [
                        "40 Bocadillos ó 20 Sandwiches mixtos (o mitad y mitad)",
                        "Platos: patatas, palomitas, bollería/galletas y frutos secos.",
                        "A elegir o combinar: 4 Pizzas ó 4 roscas.",
                        "5 Botellas de refresco.",
                    ],
                ),
                _create_pack_info_row(
                    "/pack_25_image.webp",
                    "Pack para 25 Personas",
                    "170€",
                    [
                        "50 Bocadillos ó 25 Sandwiches mixtos (o mitad y mitad)",
                        "Platos: patatas, palomitas, bollería/galletas y frutos secos.",
                        "A elegir o combinar: 4 Pizzas ó 4 roscas + 2 Tortillas de patatas",
                        "8 Botellas de refresco.",
                    ],
                ),
                _create_pack_info_row(
                    "/pack_30_image.jpeg",
                    "Pack para 30 Personas",
                    "200€",
                    [
                        "60 Bocadillos ó 30 Sandwiches mixtos (o mitad y mitad)",
                        "Platos: patatas, palomitas, bollería/galletas y frutos secos.",
                        "A elegir o combinar: 5 Pizzas ó 5 roscas + 2 Tortillas de patatas.",
                        "10 Botellas de refresco.",
                    ],
                ),
                rx.box(
                    rx.heading("Extras", font_size=FontSize.XXL, color=Color.PINK, margin_bottom=Size.SMALL.value),
                    rx.text("• Pizzas o roscas extras: 7,50€.", margin_bottom="0.5rem", color=Color.BLACK),
                    rx.text("• Plato de chuches: 2€ cada uno.", margin_bottom="0.5rem"),
                    rx.text("• Botellas de refresco extras: 4€.", margin_bottom="0.5rem", color=Color.BLACK),
                    rx.text("• Botella de agua extra: 2,50€.", margin_bottom="0.5rem", color=Color.BLACK),
                    rx.text("• Bizcocho de cafetería (normal, de chocolate, con o sin cobertura) para 8 a 10 pax: 10€.", margin_bottom="0.5rem", color=Color.BLACK),
                    rx.text("• Tarta de galletas de cafetería: 15€.", margin_bottom="0.5rem"),
                    rx.text("• Tarta panadería: 18€ el Kg.", margin_bottom="0.5rem", color=Color.BLACK),
                    rx.text("• Palmera de chocolate: 25€ (Con relleno Kinder: 28€)", margin_bottom="1rem", color=Color.BLACK),
                    padding=Size.SMALL.value,
                    border=f"2px solid {Color.PINK}",
                    border_radius="10px",
                    color=Color.BLACK,
                    background_color=Color.CARD_PACK_INFO,
                    max_width="800px",
                    width="100%",
                    margin_bottom=Size.LARGE.value,
                ),
                spacing="7",
                align_items="center",
                width="100%",
                max_width="900px",
                padding_x=Size.SMALL.value,
            ),
            width="100%",
            flex_grow="1",
            display="flex",
            flex_direction="column",
            align_items="center",
            padding_y=Size.LARGE.value,
        ),
        rx.box(
            footer(),
            class_name=Color.GRADIENT_NAVBAR,
            padding_y=Size.MEDIUM.value,
            width="100%",
            margin_top="auto",
        ),
        min_height="100vh",
        width="100%",
        display="flex",
        flex_direction="column",
        background_color=Color.PAGE_BG,
    )


def _create_pack_info_row(image_src: str, title: str, price: str, items: list[str]):
    return rx.hstack(
        rx.box(
            rx.image(src=image_src, width="280px", height="auto"),
        ),
        rx.box(
            rx.heading(title, font_size=FontSize.XL, color=Color.PURPLE_LIGHT, margin_bottom="0.3rem"),
            rx.text(price, weight="bold", color=Color.PURPLE_LIGHT, font_size=FontSize.XL, margin_bottom="0.8rem"),
            *[rx.text(f"• {item}", margin_bottom="0.5rem", color=Color.BLACK) for item in items],
            padding=Size.SMALL.value,
            border=f"2px solid {Color.PINK}",
            border_radius="10px",
            margin_bottom=Size.MEDIUM.value,
            width="100%",
        ),
        max_width="800px",
        width="100%",
        spacing="5",
    )