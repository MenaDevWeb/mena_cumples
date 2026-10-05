import reflex as rx
from mena_cumples.styles.styles import Color, FontSize, Transition, Shadow, BorderRadius
from mena_cumples.routes import Routes
from mena_cumples.states.state import State


def _nav_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        font_size=FontSize.SMALL,
        font_weight="700",
        color=Color.PURPLE_DARK,
        text_decoration="none",
        padding="0.5rem 1rem",
        border_radius="9999px",
        transition=Transition.SMOOTH,
        _hover={
            "background_color": "rgba(124, 58, 237, 0.1)",
            "color": Color.PURPLE,
        },
    )


def _mobile_nav_link(text: str, href: str) -> rx.Component:
    """Enlace del menú móvil: ocupa el ancho y cierra el drawer al navegar."""
    return rx.link(
        text,
        href=href,
        on_click=State.close_menu,
        font_size=FontSize.LARGE,
        font_weight="700",
        color=Color.PURPLE_DARK,
        text_decoration="none",
        padding="0.9rem 1.2rem",
        border_radius="1rem",
        width="100%",
        background_color=Color.PINK_BG,
        transition=Transition.SMOOTH,
        _hover={
            "background_color": "rgba(124, 58, 237, 0.15)",
            "color": Color.PURPLE,
        },
    )


def navbar():
    """Cabecera festiva: sticky, translúcida, con CTA de disponibilidad."""
    return rx.box(
        rx.flex(
            rx.link(
                rx.hstack(
                    rx.image(
                        src="/cumples_ic_clean.png",
                        height="4.5rem",
                        width="auto",
                        max_width="320px",
                        object_fit="contain",
                        style={"filter": "drop-shadow(0 2px 6px rgba(124,58,237,0.25))"},
                    ),
                    spacing="3",
                    align="center",
                ),
                href=Routes.INDEX.value,
                text_decoration="none",
            ),
            # Navegación de escritorio
            rx.desktop_only(
                rx.hstack(
                    _nav_link("Inicio", Routes.INDEX.value),
                    _nav_link("Packs", Routes.PACKS_INFORMATION.value),
                    rx.button(
                        rx.hstack(
                            rx.icon(tag="message-circle", size=16),
                            rx.text("Preguntar fecha"),
                            spacing="2",
                            align="center",
                        ),
                        on_click=State.handle_ask_availability_click,
                        background_color=Color.PURPLE_DARK,
                        color=Color.WHITE,
                        font_weight="800",
                        size="2",
                        radius="full",
                        padding="0.2rem 0.4rem",
                        cursor="pointer",
                        _hover={"background_color": Color.PURPLE},
                    ),
                    spacing="2",
                    align="center",
                ),
            ),
            # Botón hamburguesa solo en móvil
            rx.mobile_only(
                rx.icon_button(
                    rx.icon(tag="menu"),
                    on_click=State.toggle_menu,
                    variant="soft",
                    color_scheme="purple",
                    size="3",
                    radius="full",
                ),
            ),
            width="100%",
            max_width="1200px",
            margin_left="auto",
            margin_right="auto",
            padding_x="1rem",
            padding_y="0.6rem",
            align_items="center",
            justify_content="space-between",
        ),
        position="sticky",
        top="0",
        z_index="50",
        background_color="rgba(255, 255, 255, 0.85)",
        style={
            "backdrop_filter": "blur(12px)",
            "-webkit-backdrop-filter": "blur(12px)",
            "border_bottom": "1px solid rgba(124, 58, 237, 0.12)",
            "box_shadow": Shadow.NAVBAR,
        },
    )


def mobile_drawer():
    """Drawer lateral con el menú de navegación para móvil.
    Se controla con State.menu_open."""
    return rx.drawer.root(
        rx.drawer.trigger(),
        rx.drawer.portal(
            rx.drawer.overlay(),
            rx.drawer.content(
                rx.hstack(
                    rx.hstack(
                        rx.icon(
                            tag="cake",
                            color=Color.PURPLE_DARK,
                            size=22,
                        ),
                        rx.drawer.title(
                            "Menú fiesta",
                            color=Color.PURPLE_DARK,
                            font_weight="800",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.icon_button(
                        rx.icon(tag="x"),
                        on_click=State.close_menu,
                        variant="ghost",
                        color_scheme="purple",
                        size="2",
                    ),
                    justify_content="space-between",
                    align_items="center",
                    width="100%",
                    margin_bottom="1rem",
                ),
                rx.vstack(
                    _mobile_nav_link("Inicio", Routes.INDEX.value),
                    _mobile_nav_link("Packs", Routes.PACKS_INFORMATION.value),
                    rx.button(
                        "Preguntar disponibilidad",
                        on_click=State.handle_ask_availability_click,
                        background_color=Color.PURPLE_DARK,
                        color=Color.WHITE,
                        font_weight="800",
                        size="3",
                        radius="full",
                        width="100%",
                        margin_top="0.5rem",
                    ),
                    spacing="2",
                    width="100%",
                    align_items="stretch",
                ),
                rx.text(
                    "Hotel Mena Plaza · Nerja",
                    font_size=FontSize.SMALL,
                    color=Color.GRAY_TEXT,
                    text_align="center",
                    margin_top="1.5rem",
                ),
                background_color=Color.WHITE,
                padding="1.5rem",
                width="85vw",
                max_width="340px",
                height="100%",
                border_radius=f"0 {BorderRadius.MEDIUM} {BorderRadius.MEDIUM} 0",
            ),
        ),
        open=State.menu_open,
        on_open_change=State.toggle_menu,
        direction="left",
    )
