import reflex as rx
from mena_cumples.styles.styles import Size, Color, FontSize, BorderRadius, Shadow, Transition
from mena_cumples.states.state import State
from mena_cumples.states.form_state import FormBaseState
from mena_cumples.components.navbar import navbar, mobile_drawer
from mena_cumples.components.footer import footer
from mena_cumples.data.conditions import CONDITIONS
from ..routes import Routes


@rx.page(route=Routes.PACK_SELECTION.value)
def pack_selection() -> rx.Component:
    return rx.fragment(
        rx.box(
            navbar(),
            mobile_drawer(),
            rx.box(
                _selection_hero(),
                _code_banner(),
                pack_options_grid(),
                width="100%",
                max_width="1200px",
                margin_left="auto",
                margin_right="auto",
                padding_x="1rem",
                padding_top="1rem",
                padding_bottom="3rem",
                display="flex",
                flex_direction="column",
                gap="1.75rem",
                align_items="center",
            ),
            footer(),
            min_height="100vh",
            width="100%",
            display="flex",
            flex_direction="column",
            background_color="#FFF7FB",
            on_mount=FormBaseState.ensure_order_access,
        ),
        conditions_modal(),
    )


def _selection_hero():
    return rx.box(
        rx.box(
            position="absolute",
            top="-50px",
            right="-40px",
            width="170px",
            height="170px",
            border_radius="9999px",
            background_color="rgba(249, 168, 212, 0.5)",
            style={"filter": "blur(10px)"},
        ),
        rx.box(
            rx.vstack(
                rx.badge(
                    rx.hstack(
                        rx.icon(tag="package", size=14),
                        rx.text("Paso 2 de 3 · Elige pack"),
                        spacing="1",
                        align="center",
                    ),
                    color_scheme="purple",
                    variant="soft",
                    radius="full",
                    size="2",
                ),
                rx.heading(
                    "Elige tu pack",
                    font_size=rx.breakpoints({"0px": "2.3rem", "768px": "4rem"}),
                    line_height="1.08",
                    color=Color.NAVY,
                    font_weight="900",
                    text_align="center",
                ),
                rx.text(
                    "Tarde con pizzas y refrescos, o mediodía con menú. "
                    "Mismo precio, distinta carta.",
                    font_size=FontSize.LARGE,
                    color=Color.PURPLE_DARK,
                    text_align="center",
                ),
                spacing="3",
                align_items="center",
                flex="1",
            ),
            rx.image(
                src="/pedido_ic.png",
                alt="Haz tu pedido",
                width="150px",
                height="auto",
                flex_shrink="0",
                style={"animation": "floatY 3s ease-in-out infinite"},
            ),
            display="flex",
            flex_direction=rx.breakpoints({"0px": "column", "768px": "row"}),
            gap="1.25rem",
            align_items="center",
            justify_content="center",
            position="relative",
            z_index="1",
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


def _code_banner():
    return rx.cond(
        FormBaseState.code_locked,
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(tag="ticket", color=Color.NAVY, size=20),
                    background_color=Color.SUNNY,
                    padding="0.5rem",
                    border_radius="0.75rem",
                    flex_shrink="0",
                ),
                rx.text(
                    "Reserva con código ",
                    rx.el.span(
                        FormBaseState.reservation_code,
                        font_weight="900",
                        background_color=Color.NAVY,
                        color=Color.WHITE,
                        padding="0.1rem 0.5rem",
                        border_radius="0.5rem",
                    ),
                    " cargada. Elige tu pack para continuar.",
                    color=Color.NAVY,
                    font_weight="600",
                ),
                spacing="3",
                align="center",
            ),
            background_color=Color.SUNNY_BG,
            border_radius="1rem",
            padding="0.9rem 1.1rem",
            width="100%",
            style={"border": "2px dashed #EAB308"},
        ),
        rx.fragment(),
    )


def conditions_modal() -> rx.Component:
    """Modal de condiciones obligatorio antes de seleccionar pack.

    Solo se muestra si el cliente no las ha aceptado aún (llega con el
    enlace directo que ya trae el código). No se puede cerrar sin aceptar.
    """
    return rx.dialog.root(
        rx.dialog.content(
            rx.hstack(
                rx.box(
                    rx.icon(tag="scroll-text", size=22, color=Color.WHITE),
                    background_color=Color.PURPLE_DARK,
                    padding="0.6rem",
                    border_radius="0.9rem",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Condiciones del cumpleaños",
                        color=Color.NAVY,
                        font_weight="800",
                    ),
                    rx.text(
                        "Acéptalas para continuar con tu pedido.",
                        color=Color.PURPLE_DARK,
                        font_size=FontSize.SMALL,
                    ),
                    spacing="0",
                    align_items="start",
                ),
                spacing="3",
                align="center",
                margin_bottom="1rem",
            ),
            rx.box(
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
                            rx.text(
                                cond,
                                font_size=FontSize.SMALL,
                                color=Color.NAVY,
                            ),
                            spacing="2",
                            align_items="flex-start",
                        )
                        for cond in CONDITIONS
                    ],
                    spacing="2",
                    align_items="stretch",
                    width="100%",
                ),
                max_height="50vh",
                overflow_y="auto",
                padding="1rem",
                margin_bottom="1rem",
                background_color=Color.PINK_BG,
                border_radius="1rem",
            ),
            rx.box(
                rx.checkbox(
                    rx.text(
                        "He leído y acepto las condiciones.",
                        color=Color.PURPLE_DARK,
                        font_weight="700",
                    ),
                    checked=State.conditions_checked,
                    on_change=State.set_conditions_checked,
                    color_scheme="purple",
                ),
                padding="0.8rem 1rem",
                border_radius="0.9rem",
                margin_bottom="1rem",
                style={"border": f"2px solid {Color.PURPLE_RING}"},
            ),
            rx.button(
                rx.hstack(
                    rx.icon(tag="party-popper", size=18),
                    rx.text("Aceptar y continuar"),
                    spacing="2",
                    align="center",
                    justify="center",
                ),
                on_click=State.accept_conditions,
                disabled=~State.conditions_checked,
                class_name="bg-gradient-to-r from-fuchsia-500 via-purple-500 to-indigo-500",
                color=Color.WHITE,
                font_weight="800",
                border_radius="9999px",
                width="100%",
                size="3",
                padding="1.1rem 1rem",
                cursor="pointer",
                _disabled={"opacity": 0.5, "cursor": "not-allowed"},
                _hover={"filter": "brightness(1.08)"},
            ),
            rx.text(
                rx.link(
                    "Volver al inicio",
                    href=Routes.INDEX.value,
                    color=Color.PURPLE_DARK,
                    font_weight="600",
                ),
                align="center",
                margin_top="0.75rem",
                font_size=FontSize.SMALL,
            ),
            background_color=Color.WHITE,
            padding="1.5rem",
            border_radius="1.5rem",
            max_width="36rem",
            width="100%",
        ),
        open=~State.conditions_acepted,
        modal=True,
    )


def _create_pack_card(title: str, price: int, num_people: int, image_src: str, on_click_action: str | None = None, delay: str = "0s") -> rx.Component:
    # Si el código de reserva viene del enlace de WhatsApp, se arrastra al
    # formulario del pack para que el cliente no tenga que volver a teclearlo.
    href = on_click_action if on_click_action else "#"
    if on_click_action:
        href = rx.cond(
            FormBaseState.code_locked,
            f"{on_click_action}?codigo={FormBaseState.reservation_code}",
            on_click_action,
        )
    select_button = rx.link(
        rx.button(
            rx.hstack(
                rx.text("Seleccionar"),
                rx.icon(tag="arrow-right", size=16),
                spacing="2",
                align="center",
                justify="center",
            ),
            class_name="bg-gradient-to-r from-fuchsia-500 via-purple-500 to-indigo-500",
            color=Color.WHITE,
            font_weight="800",
            width="100%",
            size="3",
            radius="full",
            padding="0.9rem 1rem",
            cursor="pointer",
            _hover={"filter": "brightness(1.08)"},
        ),
        href=href,
        is_external=False,
        width="100%",
        margin_top="0.75rem",
        style={"text_decoration": "none"},
    ) if on_click_action else rx.button(
        rx.text("Seleccionar"),
        width="100%",
        margin_top="0.75rem",
        disabled=True,
    )

    return rx.box(
        rx.box(
            rx.image(
                src=image_src,
                alt=f"Pack para {num_people} personas",
                width="100%",
                height="180px",
                object_fit="cover",
                border_radius="1rem",
            ),
            rx.badge(
                f"{price}€",
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
        ),
        rx.heading(
            f"Pack para {num_people} personas",
            font_size=FontSize.LARGE,
            color=Color.NAVY,
            font_weight="800",
            text_align="center",
            margin_top="0.9rem",
        ),
        rx.text(
            f"{price}€",
            font_weight="900",
            font_size=FontSize.XXL,
            color=Color.PURPLE_DARK,
            text_align="center",
        ),
        select_button,
        padding="1rem",
        background_color=Color.WHITE,
        border_radius="1.25rem",
        box_shadow=Shadow.CARD,
        width="100%",
        class_name="card-hover fade-in-up",
        style={"animation_delay": delay},
    )



def _tipo_cumple_selector() -> rx.Component:
    """Selector Cumple Mediodía vs Tarde — mismo pack/precio, distinta carta/horario."""
    return rx.box(
        rx.vstack(
            rx.text(
                "Elige tipo de cumple",
                weight="bold",
                size="5",
                color=Color.PURPLE_DARK,
                align="center",
            ),
            rx.text(
                "Mismo precio. Mediodía usa menú con bebida (13:00-15:00). Tarde usa pizzas/roscas (16:00-19:00).",
                size="2",
                color=Color.PURPLE,
                align="center",
                style={"font_style": "italic"},
            ),
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.icon(tag="sun", size=18),
                        rx.text("Cumple Mediodía"),
                        rx.text("13:00-15:00", size="1", color=Color.PURPLE_DARK),
                        spacing="2",
                        align="center",
                    ),
                    on_click=lambda: FormBaseState.set_cumple_tipo("Cumple Mediodía"),
                    variant=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Mediodía",
                        "solid",
                        "outline",
                    ),
                    color_scheme=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Mediodía",
                        "amber",
                        "gray",
                    ),
                    size="3",
                    style={"flex": "1"},
                ),
                rx.button(
                    rx.hstack(
                        rx.icon(tag="moon", size=18),
                        rx.text("Cumple Tarde"),
                        rx.text("16:00-19:00", size="1", color=Color.PURPLE_DARK),
                        spacing="2",
                        align="center",
                    ),
                    on_click=lambda: FormBaseState.set_cumple_tipo("Cumple Tarde"),
                    variant=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Tarde",
                        "solid",
                        "outline",
                    ),
                    color_scheme=rx.cond(
                        FormBaseState.cumple_tipo == "Cumple Tarde",
                        "cyan",
                        "gray",
                    ),
                    size="3",
                    style={"flex": "1"},
                ),
                spacing="4",
                width="100%",
                margin_top="0.75rem",
            ),
            rx.box(
                rx.cond(
                    FormBaseState.cumple_tipo == "Cumple Mediodía",
                    rx.hstack(
                        rx.icon(tag="info", size=16, color="#b45309"),
                        rx.text(
                            "Has elegido Cumple Mediodía. El formulario mostrará menú (4 opciones) con cantidad + nota por producto.",
                            size="2",
                            color="#92400e",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.hstack(
                        rx.icon(tag="info", size=16, color="#0891b2"),
                        rx.text(
                            "Has elegido Cumple Tarde. El formulario mostrará bocadillos, pizzas/roscas y bebidas.",
                            size="2",
                            color="#0e7490",
                        ),
                        spacing="2",
                        align="center",
                    ),
                ),
                margin_top="0.5rem",
                padding="0.6rem 0.8rem",
                background_color=rx.cond(
                    FormBaseState.cumple_tipo == "Cumple Mediodía",
                    "#fffbeb",
                    "#ecfeff",
                ),
                border_radius="0.5rem",
                width="100%",
            ),
            spacing="2",
            width="100%",
        ),
        padding="1rem",
        background_color=Color.WHITE,
        border_radius=BorderRadius.MEDIUM,
        border=f"1px solid {Color.GRAY_BORDER}",
        box_shadow=Shadow.CARD,
        max_width="800px",
        width="100%",
        margin_bottom="1rem",
    )


def _create_mediodia_pack_card(pack: dict, index: int) -> rx.Component:
    """Card para Cumple Mediodía — mismo precio que tarde pero con menú + nota por producto."""
    # href con tipo=mediodia para que init_pack_page preseleccione Cumple Mediodía
    base_href = pack["on_click"]
    href_tarde = rx.cond(
        FormBaseState.code_locked,
        f"{base_href}?codigo={FormBaseState.reservation_code}",
        base_href,
    )
    href_mediodia = rx.cond(
        FormBaseState.code_locked,
        f"{base_href}?codigo={FormBaseState.reservation_code}&tipo=mediodia",
        f"{base_href}?tipo=mediodia",
    )
    # Usamos href_mediodia para esta variante
    button = rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="sun", size=16),
                rx.text("Mediodía"),
                spacing="1",
                align="center",
            ),
            variant="solid",
            color_scheme="amber",
            width="100%",
        ),
        href=href_mediodia,
        is_external=False,
        width="90%",
        margin_top=Size.SMALL.value,
        margin_bottom=Size.SMALL.value,
        style={"text_decoration": "none"},
    )
    return rx.card(
        rx.vstack(
            rx.box(
                rx.image(
                    src="/packs_image.webp",
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_radius="10px 10px 0 0",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="sun", size=14, color="white"),
                        rx.text("MEDIODÍA", size="1", weight="bold", color="white"),
                        rx.text("13:00-15:00", size="1", color="white"),
                        spacing="1",
                        align="center",
                    ),
                    position="absolute",
                    top="10px",
                    left="10px",
                    background_color="#f59e0b",
                    padding="0.3rem 0.6rem",
                    border_radius="9999px",
                ),
                position="relative",
                width="100%",
            ),
            rx.text(
                f"PACK DE {pack['num_people']} PERSONAS",
                weight="bold",
                align="center",
                size="5",
                margin_top="0.5rem",
            ),
            rx.text(
                "Menú a elegir + bebida incluida",
                size="2",
                color="#92400e",
                align="center",
                style={"font_style": "italic"},
            ),
            rx.vstack(
                rx.text(f"{pack['price']}€", weight="bold", size="6", color="#f59e0b"),
                spacing="1",
                align="center",
                padding_y="0.5rem",
            ),
            button,
            spacing="2",
            align="center",
            width="100%",
        ),
        variant="surface",
        border_radius=BorderRadius.CARD,
        width="100%",
        box_shadow=Shadow.CARD,
        transition=Transition.CARD,
        class_name="card-hover",
        style={"animation_delay": f"{index * 0.15}s", "border": "2px solid #fde68a"},
    )


def _create_mediodia_single_card() -> rx.Component:
    """1 pack único Mediodía — mismo tamaño que packs Tarde, con menú + nota."""
    mediodia_href = rx.cond(
        FormBaseState.code_locked,
        f"{Routes.PACK_MEDIODOIA.value}?codigo={FormBaseState.reservation_code}&tipo=mediodia",
        f"{Routes.PACK_MEDIODOIA.value}?tipo=mediodia",
    )
    return rx.box(
        rx.box(
            rx.image(
                src="/packs_image.webp",
                alt="Pack Mediodía con menú y bebida",
                width="100%",
                height="180px",
                object_fit="cover",
                border_radius="1rem",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="sun", size=13),
                    rx.text("MEDIODÍA · 13:00-15:00"),
                    spacing="1",
                    align="center",
                ),
                color_scheme="amber",
                variant="solid",
                radius="full",
                position="absolute",
                top="0.75rem",
                left="0.75rem",
            ),
            position="relative",
        ),
        rx.heading(
            "Pack Mediodía",
            font_size=FontSize.LARGE,
            color=Color.NAVY,
            font_weight="800",
            text_align="center",
            margin_top="0.9rem",
        ),
        rx.text(
            "Menú a elegir + bebida incluida",
            font_size=FontSize.SMALL,
            color="#92400e",
            text_align="center",
            font_style="italic",
        ),
        rx.heading(
            "5,90€",
            font_size=FontSize.XXL,
            color="#b45309",
            font_weight="900",
            text_align="center",
        ),
        rx.text(
            "por niño · 4 menús con nota por producto",
            font_size=FontSize.SMALL,
            color=Color.PURPLE_DARK,
            text_align="center",
        ),
        rx.link(
            rx.button(
                rx.hstack(
                    rx.icon(tag="sun", size=16),
                    rx.text("Seleccionar"),
                    spacing="2",
                    align="center",
                    justify="center",
                ),
                background_color="#b45309",
                color=Color.WHITE,
                font_weight="800",
                width="100%",
                size="3",
                radius="full",
                padding="0.9rem 1rem",
                cursor="pointer",
                _hover={"background_color": "#92400e"},
            ),
            href=mediodia_href,
            is_external=False,
            width="100%",
            margin_top="0.75rem",
            style={"text_decoration": "none"},
        ),
        padding="1rem",
        background_color=Color.WHITE,
        border_radius="1.25rem",
        box_shadow=Shadow.CARD,
        width="100%",
        style={"border": "2px solid #fde68a"},
        class_name="card-hover fade-in-up",
    )


def pack_options_grid() -> rx.Component:
    """Crea el grid de cards para los packs — Tarde y Mediodía con mismo precio."""
    return rx.box(
        # --- Cumple Tarde (16:00-19:00) ---
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(tag="moon", size=18, color=Color.WHITE),
                    background_color=Color.PURPLE_DARK,
                    padding="0.45rem",
                    border_radius="0.75rem",
                ),
                rx.heading(
                    "Cumple Tarde",
                    size="6",
                    color=Color.NAVY,
                    font_weight="800",
                ),
                rx.badge(
                    "16:00-19:00 · Pizzas y refrescos",
                    color_scheme="purple",
                    variant="soft",
                    radius="full",
                ),
                spacing="3",
                align="center",
                justify="center",
                wrap="wrap",
                width="100%",
            ),
            rx.box(
                *[
                    _create_pack_card(
                        title=pack["title"],
                        price=pack["price"],
                        num_people=pack["num_people"],
                        image_src=pack["image_src"],
                        on_click_action=pack["on_click"],
                        delay=f"{i * 0.15}s",
                    )
                    for i, pack in enumerate(PACK_OPTIONS_DATA)
                ],
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "640px": "repeat(2, minmax(0, 1fr))",
                        "1024px": "repeat(4, minmax(0, 1fr))",
                    }
                ),
                gap="1.5rem",
                width="100%",
                margin_top="1.25rem",
            ),
            width="100%",
        ),
        rx.divider(width="100%", style={"border_color": Color.PURPLE_RING}),
        # --- Cumple Mediodía (13:00-15:00) ---
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon(tag="sun", size=18, color=Color.WHITE),
                    background_color="#f59e0b",
                    padding="0.45rem",
                    border_radius="0.75rem",
                ),
                rx.heading(
                    "Cumple Mediodía",
                    size="6",
                    color=Color.NAVY,
                    font_weight="800",
                ),
                rx.badge(
                    "13:00-15:00 · Menú + bebida",
                    color_scheme="amber",
                    variant="soft",
                    radius="full",
                ),
                spacing="3",
                align="center",
                justify="center",
                wrap="wrap",
                width="100%",
            ),
            rx.text(
                "Mismo precio que Tarde. Cada menú incluye patatas + 1 bebida. Como extras solo chuches y repostería.",
                font_size=FontSize.SMALL,
                color="#92400e",
                text_align="center",
                margin_top="0.5rem",
            ),
            rx.box(
                _create_mediodia_single_card(),
                max_width="340px",
                width="100%",
                margin_left="auto",
                margin_right="auto",
                margin_top="1.25rem",
            ),
            width="100%",
        ),
        display="flex",
        flex_direction="column",
        gap="2rem",
        width="100%",
        align_items="center",
    )

# Datos de los packs
PACK_OPTIONS_DATA = [
    {
        "title": "PACK DE 110€---PARA 15 PERSONAS",
        "price": 110,
        "num_people": 15,
        "image_src": "/pack_15_image.webp",
        "on_click": Routes.PACK_15_PAX.value,
    },
    {
        "title": "PACK DE 140€---PARA 20 PERSONAS",
        "price": 140,
        "num_people": 20,
        "image_src": "/pack_20_image.webp",
        "on_click":Routes.PACK_20_PAX.value,
    },
    {
        "title": "PACK DE 170€---PARA 25 PERSONAS",
        "price": 170,
        "num_people": 25,
        "image_src": "/pack_25_image.webp",
        "on_click": Routes.PACK_25_PAX.value,
    },
    {
        "title": "PACK DE 200€---PARA 30 PERSONAS",
        "price": 200,
        "num_people": 30,
        "image_src": "/pack_30_image.jpeg",
        "on_click": Routes.PACK_30_PAX.value,
    },
]
