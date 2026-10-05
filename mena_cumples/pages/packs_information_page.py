import reflex as rx
from mena_cumples.components.navbar import navbar, mobile_drawer
from mena_cumples.components.footer import footer
from mena_cumples.styles.styles import Size, Color, FontSize, Shadow, BorderRadius, Transition
from mena_cumples.routes import Routes


@rx.page(route="/packs_information")
def packs_information():
    return rx.box(
        navbar(),
        mobile_drawer(),
        rx.box(
            _packs_hero(),
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
                accent=Color.PINK_LIGHT,
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
                accent="#C4B5FD",
                flip=True,
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
                accent=Color.SUNNY,
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
                accent="#7DD3FC",
                flip=True,
            ),
            _create_extras_card(),
            _packs_cta(),
            align_items="center",
            width="100%",
            max_width="1100px",
            margin_left="auto",
            margin_right="auto",
            padding_x="1rem",
            padding_top="1rem",
            padding_bottom="3rem",
            display="flex",
            flex_direction="column",
            gap="2.5rem",
        ),
        footer(),
        min_height="100vh",
        width="100%",
        background_color="#FFF7FB",
    )


def _packs_hero():
    return rx.box(
        rx.box(
            position="absolute",
            top="-50px",
            right="-50px",
            width="180px",
            height="180px",
            border_radius="9999px",
            background_color="rgba(249, 168, 212, 0.5)",
            style={"filter": "blur(10px)"},
        ),
        rx.box(
            rx.vstack(
                rx.badge(
                    rx.hstack(
                        rx.icon(tag="cake", size=14),
                        rx.text("Merienda en cafetería"),
                        spacing="1",
                        align="center",
                    ),
                    color_scheme="purple",
                    variant="soft",
                    radius="full",
                    size="2",
                ),
                rx.heading(
                    "Nuestros packs",
                    font_size=rx.breakpoints({"0px": "2.3rem", "768px": "4rem"}),
                    line_height="1.08",
                    color=Color.NAVY,
                    font_weight="900",
                    text_align="center",
                ),
                rx.text(
                    "De 15 a 30 personas, con bocadillos, pizzas, refrescos "
                    "y extras de repostería. Elige el que encaje con tu fiesta.",
                    font_size=FontSize.LARGE,
                    color=Color.PURPLE_DARK,
                    text_align="center",
                ),
                rx.hstack(
                    _hero_chip("users", "15-30 personas"),
                    _hero_chip("pizza", "Pizzas y roscas"),
                    _hero_chip("candy", "Extras dulces"),
                    spacing="2",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="3",
                align_items="center",
            ),
            position="relative",
            z_index="1",
            padding_y="0.5rem",
        ),
        class_name=Color.GRADIENT_HERO,
        border_radius="1.75rem",
        padding="2rem 1.5rem",
        margin_top="1rem",
        position="relative",
        overflow="hidden",
        box_shadow=Shadow.CARD,
        width="100%",
    )


def _hero_chip(icon: str, text: str):
    return rx.hstack(
        rx.icon(tag=icon, size=14, color=Color.PURPLE_DARK),
        rx.text(text, font_size=FontSize.SMALL, font_weight="700", color=Color.PURPLE_DARK),
        spacing="1",
        align="center",
        background_color=Color.WHITE,
        padding="0.4rem 0.8rem",
        border_radius="9999px",
        box_shadow=Shadow.SOFT,
    )


def _create_pack_info_row(image_src: str, title: str, price: str, items: list[str],
                          accent: str = Color.PINK_LIGHT, flip: bool = False):
    image_block = rx.box(
        rx.image(
            src=image_src,
            alt=title,
            border_radius="1rem",
            width="100%",
            height="220px",
            object_fit="cover",
        ),
        rx.badge(
            price,
            color_scheme="amber",
            variant="solid",
            radius="full",
            size="3",
            position="absolute",
            bottom="0.75rem",
            left="0.75rem",
            style={"font_weight": "900", "font_size": "1.25rem", "padding": "0.3rem 1rem"},
        ),
        position="relative",
        width="100%",
    )
    content_block = rx.vstack(
        rx.hstack(
            rx.box(width="0.6rem", height="1.6rem", border_radius="9999px", background_color=accent),
            rx.heading(title, font_size=FontSize.XL, color=Color.NAVY, font_weight="800"),
            spacing="2",
            align="center",
        ),
        rx.vstack(
            *[
                rx.hstack(
                    rx.box(
                        rx.icon(tag="check", color=Color.WHITE, size=13),
                        background_color=Color.MINT,
                        padding="0.2rem",
                        border_radius="9999px",
                        flex_shrink="0",
                    ),
                    rx.text(item, color=Color.NAVY),
                    spacing="2",
                    align="start",
                )
                for item in items
            ],
            spacing="2",
            align_items="start",
            width="100%",
        ),
        spacing="3",
        align_items="start",
        width="100%",
    )
    blocks = [content_block, image_block] if flip else [image_block, content_block]
    return rx.box(
        *blocks,
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "0.9fr 1.1fr",
            }
        ),
        gap="1.25rem",
        align_items="center",
        background_color=Color.WHITE,
        border_radius="1.25rem",
        padding="1.25rem",
        box_shadow=Shadow.CARD,
        width="100%",
        class_name="card-hover",
    )


def _create_extras_card():
    extras = [
        "Pizzas o roscas extras: 7,50€.",
        "Plato de chuches: 2€ cada uno.",
        "Botellas de refresco extras: 4€.",
        "Botella de agua extra: 2,50€.",
        "Bizcocho de cafetería (normal, de chocolate, con o sin cobertura) para 8 a 10 pax: 10€.",
        "Tarta de galletas de cafetería: 15€.",
        "Tarta panadería: 18€ el Kg.",
        "Palmera de chocolate: 25€ (Con relleno Kinder: 28€)",
    ]
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(tag="sparkles", size=20, color=Color.NAVY),
                background_color=Color.SUNNY,
                padding="0.5rem",
                border_radius="0.75rem",
            ),
            rx.heading("Extras para tu fiesta", font_size=FontSize.XL, color=Color.NAVY, font_weight="800"),
            spacing="3",
            align="center",
        ),
        rx.box(
            *[
                rx.hstack(
                    rx.box(
                        rx.icon(tag="plus", color=Color.WHITE, size=13),
                        background_color=Color.PURPLE,
                        padding="0.2rem",
                        border_radius="9999px",
                        flex_shrink="0",
                    ),
                    rx.text(item, color=Color.NAVY),
                    spacing="2",
                    align="start",
                )
                for item in extras
            ],
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            gap="0.75rem",
            margin_top="1rem",
        ),
        rx.box(
            rx.hstack(
                rx.icon(tag="info", size=16, color=Color.NAVY),
                rx.text(
                    "En Pack Mediodía solo se pueden añadir como extras chuches y repostería.",
                    font_weight="700",
                    color=Color.NAVY,
                    font_size=FontSize.SMALL,
                ),
                spacing="2",
                align="center",
            ),
            background_color=Color.SUNNY_BG,
            border_radius="0.9rem",
            padding="0.8rem 1rem",
            margin_top="1rem",
            style={"border": "2px dashed #EAB308"},
        ),
        background_color=Color.WHITE,
        border_radius="1.25rem",
        padding="1.25rem",
        box_shadow=Shadow.CARD,
        width="100%",
    )


def _packs_cta():
    return rx.box(
        rx.heading(
            "¿Ya sabes cuál quieres?",
            color=Color.WHITE,
            font_weight="900",
            font_size=rx.breakpoints({"0px": "1.5rem", "768px": "2.25rem"}),
            text_align="center",
        ),
        rx.text(
            "Pregunta disponibilidad primero — el cumple no queda confirmado hasta entregar el depósito de 50€.",
            color="rgba(255,255,255,0.9)",
            text_align="center",
            margin_top="0.5rem",
        ),
        rx.flex(
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="calendar-check", size=18),
                        rx.text("Preguntar disponibilidad"),
                        spacing="2",
                        align="center",
                    ),
                    background_color=Color.SUNNY,
                    color=Color.NAVY,
                    font_weight="800",
                    size="3",
                    radius="full",
                    padding="1.2rem 1.6rem",
                    cursor="pointer",
                    _hover={"filter": "brightness(1.05)"},
                ),
                href=Routes.CONTACT_FORM_PAGE.value,
                text_decoration="none",
            ),
            rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="arrow-left", size=18),
                        rx.text("Volver al inicio"),
                        spacing="2",
                        align="center",
                    ),
                    background_color="transparent",
                    color=Color.WHITE,
                    font_weight="800",
                    size="3",
                    radius="full",
                    padding="1.2rem 1.6rem",
                    cursor="pointer",
                    variant="outline",
                    style={"border": "2px solid rgba(255,255,255,0.6)"},
                    _hover={"background_color": "rgba(255,255,255,0.12)"},
                ),
                href=Routes.INDEX.value,
                text_decoration="none",
            ),
            gap="0.75rem",
            wrap="wrap",
            justify="center",
            margin_top="1.25rem",
        ),
        background_color=Color.NAVY,
        border_radius="1.5rem",
        padding="2rem 1.5rem",
        width="100%",
        text_align="center",
        class_name="fade-in-up",
    )
