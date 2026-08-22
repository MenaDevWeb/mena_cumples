import reflex as rx
from mena_cumples.styles.styles import Color, FontSize, Transition
from mena_cumples.routes import Routes
from mena_cumples.states.state import State


def _nav_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        font_size=FontSize.SMALL,
        font_weight="600",
        color=Color.PURPLE_DARK,
        text_decoration="none",
        padding="0.4rem 0.8rem",
        border_radius="8px",
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
        font_size=FontSize.DEFAULT,
        font_weight="600",
        color=Color.PURPLE_DARK,
        text_decoration="none",
        padding="0.75rem 1rem",
        border_radius="8px",
        width="100%",
        transition=Transition.SMOOTH,
        _hover={
            "background_color": "rgba(124, 58, 237, 0.1)",
            "color": Color.PURPLE,
        },
    )


def navbar():
    """Cabecera con logo y navegación. En móvil muestra un botón hamburguesa
    que abre un drawer lateral con los enlaces."""
    return rx.flex(
        rx.image(
            src="/mena_cumples.png",
            width="200px",
            height="auto",
        ),
        # Navegación de escritorio
        rx.desktop_only(
            rx.flex(
                _nav_link("Inicio", Routes.INDEX.value),
                _nav_link("Packs", Routes.PACKS_INFORMATION.value),
                gap="0.5rem",
                align_items="center",
            ),
        ),
        # Botón hamburguesa solo en móvil
        rx.mobile_only(
            rx.icon_button(
                rx.icon(tag="menu"),
                on_click=State.toggle_menu,
                variant="ghost",
                color_scheme="purple",
                size="3",
            ),
        ),
        width="100%",
        max_width="1200px",
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
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
                    rx.drawer.title(
                        "Menú",
                        color=Color.PURPLE_DARK,
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
                    spacing="2",
                    width="100%",
                    align_items="stretch",
                ),
                background_color=Color.WHITE,
                padding="1.5rem",
                width="80vw",
                max_width="320px",
                height="100%",
            ),
        ),
        open=State.menu_open,
        on_open_change=State.toggle_menu,
        direction="left",
    )
