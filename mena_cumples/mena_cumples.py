import reflex as rx
from .states.state import State  # Cambiamos la importación
from .pages.contact_form_page import create_page_layout
from .pages.pack_selection_page import pack_selection
from .pages.pack_15_page import pack_15
from .pages.pack_20_page import pack_20
from .pages.pack_25_page import pack_25
from .pages.pack_30_page import pack_30
from .pages.pack_mediodia_page import pack_mediodia
from .pages.packs_information_page import packs_information
from .styles.styles import style, Color, FontSize, BorderRadius, Shadow, Transition, Size
from .components.navbar import navbar, mobile_drawer
from .components.footer import footer
from .data.conditions import CONDITIONS
from .routes import Routes


@rx.page(route=Routes.INDEX.value, title="Cumpleaños Mena Plaza", on_load=State.handle_url_code)
def index() -> rx.Component:
    return rx.fragment(
        create_main_screen()
    )

def create_main_screen():
    """Create the main application component with styles and page layout."""
    return rx.fragment(
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
        html {
            font-size: 16px;
        }
        body {
            -webkit-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }
    """
        ),
        create_page_layout(),
    )


def create_page_layout():
    """Layout festivo: navbar sticky + hero + contenido + footer navy."""
    return rx.box(
        navbar(),
        mobile_drawer(),
        create_main_content(),
        footer(),
        background_color="#FFF7FB",
        min_height="100vh",
    )


def create_main_content():
    """Home festiva: hero + pasos + tarjetas + condiciones + depósito."""
    return rx.box(
        create_hero(),
        create_steps(),
        create_action_cards(),
        create_conditions_section(),
        create_deposit_text(text=""),
        create_finale(),
        width="100%",
        max_width="1200px",
        margin_left="auto",
        margin_right="auto",
        padding_x="1rem",
        padding_bottom="3rem",
    )


# ---------------------------------------------------------------------------
# HERO
# ---------------------------------------------------------------------------

def create_hero():
    return rx.box(
        # círculos decorativos
        rx.box(
            position="absolute",
            top="-60px",
            right="-60px",
            width="220px",
            height="220px",
            border_radius="9999px",
            background_color="rgba(249, 168, 212, 0.5)",
            style={"filter": "blur(10px)"},
        ),
        rx.box(
            position="absolute",
            bottom="-70px",
            left="-50px",
            width="200px",
            height="200px",
            border_radius="9999px",
            background_color="rgba(255, 201, 60, 0.45)",
            style={"filter": "blur(10px)"},
        ),
        rx.box(
            rx.box(
                # Columna texto
                rx.vstack(
                    rx.badge(
                        rx.hstack(
                            rx.icon(tag="party-popper", size=14),
                            rx.text("Hotel Mena Plaza · Nerja"),
                            spacing="1",
                            align="center",
                        ),
                        color_scheme="purple",
                        variant="soft",
                        radius="full",
                        size="2",
                    ),
                    rx.heading(
                        "¡Celebra un ",
                        rx.el.span(
                            "cumple inolvidable",
                            background_color=Color.SUNNY,
                            padding="0.1rem 0.6rem",
                            border_radius="0.75rem",
                            display="inline-block",
                            style={"transform": "rotate(-2deg)"},
                        ),
                        "!",
                        font_size=rx.breakpoints({"0px": "2.3rem", "768px": "4rem"}),
                        line_height="1.08",
                        color=Color.NAVY,
                        font_weight="900",
                    ),
                    rx.text(
                        "Packs de merienda de 15 a 30 personas con bocadillos, "
                        "pizzas, refrescos y extras de repostería. "
                        "Tú eliges el pack, nosotros lo preparamos todo.",
                        font_size=FontSize.LARGE,
                        line_height="1.7rem",
                        color=Color.PURPLE_DARK,
                    ),
                    rx.flex(
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="calendar-check", size=18),
                                rx.text("PREGUNTAR FECHA"),
                                spacing="2",
                                align="center",
                            ),
                            on_click=State.handle_ask_availability_click,
                            background_color=Color.PURPLE_DARK,
                            color=Color.WHITE,
                            font_weight="800",
                            size="3",
                            radius="full",
                            padding="1.4rem 1.8rem",
                            cursor="pointer",
                            box_shadow=Shadow.CARD,
                            _hover={"background_color": Color.PURPLE},
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon(tag="cake", size=18),
                                    rx.text("Ver packs"),
                                    spacing="2",
                                    align="center",
                                ),
                                background_color=Color.WHITE,
                                color=Color.PURPLE_DARK,
                                font_weight="800",
                                size="3",
                                radius="full",
                                padding="1.4rem 1.8rem",
                                cursor="pointer",
                                variant="outline",
                                style={"border": f"2px solid {Color.PURPLE_DARK}"},
                                _hover={"background_color": Color.PINK_BG},
                            ),
                            href=Routes.PACKS_INFORMATION.value,
                            text_decoration="none",
                        ),
                        gap="0.75rem",
                        wrap="wrap",
                    ),
                    rx.hstack(
                        _hero_trust_item("users", "Packs 15-30 peques"),
                        _hero_trust_item("map-pin", "Cafetería Mena Plaza"),
                        _hero_trust_item("message-circle", "Fácil por WhatsApp"),
                        spacing="4",
                        wrap="wrap",
                        margin_top="0.5rem",
                    ),
                    spacing="4",
                    align_items="start",
                ),
                # Columna imagen
                rx.box(
                    rx.image(
                        src="/packs_info_image.webp",
                        alt="Mesa de cumpleaños con tarta en tonos rosa y morado",
                        border_radius="1.5rem",
                        width="100%",
                        height="auto",
                        object_fit="cover",
                        box_shadow=Shadow.CARD_HOVER,
                        style={"transform": "rotate(2deg)"},
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="ticket", color=Color.WHITE, size=20),
                            rx.vstack(
                                rx.text(
                                    "Código por WhatsApp",
                                    color=Color.WHITE,
                                    font_weight="800",
                                    font_size=FontSize.SMALL,
                                ),
                                rx.text(
                                    "para hacer tu pedido",
                                    color="rgba(255,255,255,0.85)",
                                    font_size=FontSize.XS,
                                ),
                                spacing="0",
                                align_items="start",
                            ),
                            spacing="2",
                            align="center",
                        ),
                        position="absolute",
                        bottom="1rem",
                        left="1rem",
                        background_color=Color.PURPLE_DARK,
                        padding="0.7rem 1rem",
                        border_radius="1rem",
                        box_shadow=Shadow.CARD,
                        class_name="float-badge",
                        style={"animation": "floatY 3s ease-in-out infinite"},
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon(tag="sparkles", color=Color.NAVY, size=18),
                            rx.text(
                                "¡FELICIDADES!",
                                font_weight="900",
                                color=Color.NAVY,
                                font_size=FontSize.SMALL,
                            ),
                            spacing="1",
                            align="center",
                        ),
                        position="absolute",
                        top="1rem",
                        right="0.5rem",
                        background_color=Color.SUNNY,
                        padding="0.5rem 0.9rem",
                        border_radius="9999px",
                        box_shadow=Shadow.CARD,
                        style={"transform": "rotate(4deg)"},
                    ),
                    position="relative",
                    width="100%",
                    max_width="480px",
                ),
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "900px": "1.05fr 0.95fr",
                    }
                ),
                gap="2rem",
                align_items="center",
                position="relative",
                z_index="1",
            ),
            class_name=Color.GRADIENT_HERO,
            border_radius="1.75rem",
            padding=rx.breakpoints({"0px": "1.5rem", "768px": "2.5rem"}),
            margin_top="1rem",
            position="relative",
            overflow="hidden",
            box_shadow=Shadow.CARD,
        ),
        position="relative",
        margin_top="1rem",
    )


def _hero_trust_item(icon: str, text: str):
    return rx.hstack(
        rx.box(
            rx.icon(tag=icon, size=15, color=Color.PURPLE_DARK),
            background_color=Color.WHITE,
            padding="0.4rem",
            border_radius="9999px",
            box_shadow=Shadow.SOFT,
        ),
        rx.text(
            text,
            font_size=FontSize.SMALL,
            font_weight="700",
            color=Color.PURPLE_DARK,
        ),
        spacing="2",
        align="center",
    )


# ---------------------------------------------------------------------------
# PASOS
# ---------------------------------------------------------------------------

def create_steps():
    return rx.box(
        rx.heading(
            "¿Cómo funciona?",
            text_align="center",
            color=Color.NAVY,
            font_weight="900",
            font_size=rx.breakpoints({"0px": "1.6rem", "768px": "2.25rem"}),
            margin_top="2.5rem",
        ),
        rx.text(
            "En 3 pasos tienes tu fiesta lista. Sin líos.",
            text_align="center",
            color=Color.PURPLE_DARK,
            font_size=FontSize.LARGE,
            margin_bottom="1.25rem",
        ),
        rx.box(
            _step_card(
                number="1",
                bg=Color.PINK_LIGHT,
                icon="calendar-check",
                title="Pregunta fecha",
                desc="Cuéntanos el día, la hora y cuántos sois.",
            ),
            _step_card(
                number="2",
                bg=Color.SUNNY,
                icon="message-circle",
                title="Recibe tu código",
                desc="Te lo enviamos por WhatsApp para tu pedido.",
            ),
            _step_card(
                number="3",
                bg="#C4B5FD",
                icon="cake",
                title="Haz tu pedido",
                desc="Introduce el código abajo y elige tu pack.",
            ),
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
            gap="1rem",
        ),
        class_name="fade-in-up",
    )


def _step_card(number: str, bg: str, icon: str, title: str, desc: str):
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(
                    number,
                    font_weight="900",
                    font_size=FontSize.XL,
                    color=Color.NAVY,
                ),
                background_color=bg,
                width="2.5rem",
                height="2.5rem",
                border_radius="9999px",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            rx.box(
                rx.icon(tag=icon, size=22, color=Color.PURPLE_DARK),
                background_color=Color.WHITE,
                padding="0.55rem",
                border_radius="1rem",
                box_shadow=Shadow.SOFT,
            ),
            justify="between",
            width="100%",
            align="center",
        ),
        rx.text(title, font_weight="800", font_size=FontSize.LARGE, color=Color.NAVY),
        rx.text(desc, color=Color.PURPLE_DARK, font_size=FontSize.DEFAULT),
        background_color=Color.WHITE,
        border_radius="1.25rem",
        padding="1.25rem",
        box_shadow=Shadow.CARD,
        display="flex",
        flex_direction="column",
        gap="0.6rem",
        class_name="card-hover",
    )


# ---------------------------------------------------------------------------
# TARJETA ÚNICA DE DECISIÓN (tengo código / no tengo código)
# ---------------------------------------------------------------------------

def create_action_cards():
    """Un solo bloque de decisión en vez de dos tarjetas gemelas.
    Izquierda: ya tengo código (paso 3). Derecha: aún no (paso 1)."""
    return rx.box(
        rx.heading(
            "¿Empezamos?",
            font_size=FontSize.XXL,
            color=Color.NAVY,
            font_weight="900",
            text_align="center",
        ),
        rx.text(
            "Elige tu camino: con código vas directo al pedido, sin código preguntas fecha primero.",
            color=Color.PURPLE_DARK,
            text_align="center",
            margin_top="0.25rem",
            margin_bottom="1.25rem",
        ),
        rx.box(
            # Camino A: ya tengo código
            rx.vstack(
                rx.badge(
                    rx.hstack(
                        rx.icon(tag="ticket", size=13),
                        rx.text("Ya tengo código"),
                        spacing="1",
                        align="center",
                    ),
                    color_scheme="amber",
                    variant="soft",
                    radius="full",
                    align_self="start",
                ),
                rx.heading(
                    "Haz tu pedido",
                    font_size=FontSize.XL,
                    color=Color.NAVY,
                    font_weight="800",
                    text_align="left",
                ),
                rx.el.input(
                    on_change=State.set_order_code,
                    value=State.order_code,
                    type="text",
                    placeholder="Código (ej: CUM-7XD4)",
                    width="100%",
                    padding="0.75rem 1rem",
                    border_radius="1rem",
                    font_size=FontSize.INPUT,
                    color=Color.BLACK,
                    background_color="#FDF2F8",
                    border_width="2px",
                    border_style="solid",
                    border_color=Color.PURPLE_RING,
                    height="3rem",
                    style={"text_transform": "uppercase"},
                ),
                rx.button(
                    rx.hstack(
                        rx.icon(tag="party-popper", size=18),
                        rx.text("HACER PEDIDO"),
                        spacing="2",
                        align="center",
                        justify="center",
                    ),
                    on_click=State.submit_order_code,
                    class_name="bg-gradient-to-r from-fuchsia-500 via-purple-500 to-indigo-500",
                    color=Color.WHITE,
                    font_weight="800",
                    width="100%",
                    size="3",
                    padding="1.1rem 1rem",
                    border_radius="9999px",
                    cursor="pointer",
                    transition=Transition.DEFAULT,
                    _hover={"filter": "brightness(1.08)"},
                ),
                spacing="3",
                align_items="stretch",
                flex="1",
                min_width="0",
            ),
            # Divisor con "o"
            rx.box(
                rx.box(
                    rx.text("o", font_weight="800", color=Color.PURPLE_DARK, font_size=FontSize.SMALL),
                    background_color=Color.PINK_BG,
                    width="2.2rem",
                    height="2.2rem",
                    border_radius="9999px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                padding_y="0.5rem",
            ),
            # Camino B: aún no tengo código
            rx.vstack(
                rx.badge(
                    rx.hstack(
                        rx.icon(tag="calendar-check", size=13),
                        rx.text("Paso 1"),
                        spacing="1",
                        align="center",
                    ),
                    color_scheme="purple",
                    variant="soft",
                    radius="full",
                    align_self="start",
                ),
                rx.heading(
                    "¿Aún no tienes código?",
                    font_size=FontSize.XL,
                    color=Color.NAVY,
                    font_weight="800",
                    text_align="left",
                ),
                rx.text(
                    "Pregunta disponibilidad y te lo enviamos por WhatsApp.",
                    color=Color.PURPLE_DARK,
                ),
                rx.button(
                    rx.hstack(
                        rx.icon(tag="message-circle", size=18),
                        rx.text("PREGUNTAR FECHA"),
                        spacing="2",
                        align="center",
                        justify="center",
                    ),
                    on_click=State.handle_ask_availability_click,
                    background_color=Color.PURPLE_DARK,
                    color=Color.WHITE,
                    font_weight="800",
                    width="100%",
                    size="3",
                    padding="1.1rem 1rem",
                    border_radius="9999px",
                    cursor="pointer",
                    transition=Transition.DEFAULT,
                    _hover={"background_color": Color.PURPLE},
                ),
                spacing="3",
                align_items="stretch",
                flex="1",
                min_width="0",
            ),
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "1fr auto 1fr",
                }
            ),
            gap="1.25rem",
            align_items="center",
        ),
        padding="1.5rem",
        box_shadow=Shadow.CARD,
        border_radius="1.5rem",
        background_color=Color.WHITE,
        margin_top="2rem",
        class_name="fade-in-up",
        style={"animation_delay": "0.15s"},
    )


# ---------------------------------------------------------------------------
# CONDICIONES + DEPÓSITO + FINAL
# ---------------------------------------------------------------------------

def create_conditions_section():
    """Sección informativa colapsable - no bloquea el flujo.

    Las condiciones se aceptan obligatoriamente en el modal de
    pack_selection (pack_selection_page.py) y no aquí. En la home
    solo informamos, para que el cliente no pueda decir que no se le avisó,
    pero sin fricción para preguntar disponibilidad o hacer pedido.
    """
    return rx.box(
        rx.el.details(
            rx.el.summary(
                rx.hstack(
                    rx.hstack(
                        rx.box(
                            rx.icon(tag="scroll-text", size=20, color=Color.PURPLE_DARK),
                            background_color=Color.WHITE,
                            padding="0.5rem",
                            border_radius="0.75rem",
                        ),
                        rx.vstack(
                            rx.heading(
                                "Condiciones de la fiesta",
                                font_size=FontSize.LARGE,
                                color=Color.NAVY,
                                font_weight="800",
                                as_="h3",
                            ),
                            rx.text(
                                "Léelas aquí · se aceptan al pedir",
                                font_size=FontSize.SMALL,
                                color=Color.PURPLE_DARK,
                                font_weight="600",
                            ),
                            spacing="0",
                            align_items="start",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    rx.badge("Ver detalle", color_scheme="purple", variant="soft", radius="full"),
                    justify="between",
                    align="center",
                    width="100%",
                ),
                style={"cursor": "pointer", "list_style": "none"},
            ),
            rx.list(
                *[
                    create_list_item_with_icon(text=cond)
                    for cond in CONDITIONS
                ],
                gap="0.75rem",
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(2, minmax(0, 1fr))",
                    }
                ),
                margin_top="1rem",
            ),
            rx.text(
                "Las condiciones se aceptarán obligatoriamente al elegir tu pack. "
                "Al continuar, confirmas que las has leído.",
                font_size=FontSize.SMALL,
                color=Color.PURPLE_DARK,
                font_weight="600",
                margin_top="1rem",
                font_style="italic",
            ),
            rx.text(
                "Se recomienda navegador Chrome o Firefox. Safari de iPhone puede dar problemas.",
                font_weight="bold",
                color=Color.PURPLE,
                font_size=FontSize.SMALL,
                margin_top="0.5rem",
            ),
            style={"border": "none"},
            open=False,
        ),
        background_color=Color.CARD_PINK,
        margin_top="2rem",
        margin_bottom="1rem",
        padding="1.25rem",
        border_radius="1.25rem",
        box_shadow=Shadow.SOFT,
    )


def create_deposit_text(text):
    # Aviso importante con estética festiva (ámbar ticket), no rojo error.
    # Mantiene el mensaje legal intacto, pero integrado en la home.
    _ = text
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon(tag="wallet", color=Color.NAVY, size=24),
                background_color=Color.SUNNY,
                padding="0.7rem",
                border_radius="1rem",
                flex_shrink="0",
                box_shadow=Shadow.SOFT,
            ),
            rx.vstack(
                rx.badge(
                    rx.hstack(
                        rx.icon(tag="info", size=13),
                        rx.text("Importante · reserva"),
                        spacing="1",
                        align="center",
                    ),
                    color_scheme="amber",
                    variant="soft",
                    radius="full",
                    align_self="start",
                ),
                rx.text(
                    "El cumpleaños ",
                    rx.el.span(
                        "NO está confirmado",
                        font_weight="900",
                        background_color=Color.NAVY,
                        color=Color.WHITE,
                        padding="0.1rem 0.5rem",
                        border_radius="0.5rem",
                        white_space="nowrap",
                    ),
                    " hasta entregar el depósito de ",
                    rx.el.span(
                        "50€",
                        font_weight="900",
                        background_color=Color.WHITE,
                        color=Color.NAVY,
                        padding="0.1rem 0.6rem",
                        border_radius="9999px",
                        style={"border": f"2px solid {Color.NAVY}"},
                        white_space="nowrap",
                    ),
                    ".",
                    color=Color.NAVY,
                    font_size=FontSize.LARGE,
                    line_height="1.9rem",
                    font_weight="600",
                ),
                spacing="2",
                align_items="start",
                flex="1",
                min_width="0",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        background_color=Color.SUNNY_BG,
        border_radius="1.25rem",
        padding="1.25rem",
        margin_top="1rem",
        width="100%",
        box_shadow=Shadow.CARD,
        style={
            "border": "2px dashed #EAB308",
        },
        class_name="scale-in",
        overflow="hidden",
    )


def create_finale():
    return rx.box(
        rx.hstack(
            rx.icon(tag="sparkles", color=Color.SUNNY, size=22),
            rx.heading(
                "¡FELICIDADES!",
                color=Color.WHITE,
                font_weight="900",
                font_size=rx.breakpoints({"0px": "1.5rem", "768px": "2.25rem"}),
            ),
            rx.icon(tag="sparkles", color=Color.SUNNY, size=22),
            spacing="3",
            align="center",
            justify="center",
        ),
        rx.text(
            "¡Gracias por celebrar este día tan especial con nosotros!",
            color="rgba(255,255,255,0.9)",
            text_align="center",
            margin_top="0.5rem",
        ),
        background_color=Color.NAVY,
        border_radius="1.5rem",
        padding="2rem 1.5rem",
        margin_top="2rem",
        text_align="center",
        class_name="fade-in-up",
        style={"animation_delay": "0.25s"},
    )


# ---------------------------------------------------------------------------
# Helpers legacy (se mantienen firmas por compatibilidad)
# ---------------------------------------------------------------------------

def create_list_item(item_text):
    """Create a list item with a styled link."""
    return rx.el.li(create_link(text=item_text))


def create_link(text):
    return rx.el.a(
        text,
        href="#",
        _hover={"color": Color.PURPLE_LIGHT},
        color=Color.PURPLE,
    )


def create_list_item_with_icon(text):
    return rx.el.li(
        rx.box(
            rx.icon(tag="check", color=Color.WHITE, size=14),
            background_color=Color.MINT,
            padding="0.25rem",
            border_radius="9999px",
            flex_shrink="0",
        ),
        rx.el.span(text, color=Color.NAVY, font_weight="500"),
        display="flex",
        align_items="flex-start",
        gap="0.6rem",
        background_color=Color.WHITE,
        padding="0.7rem 0.9rem",
        border_radius="0.9rem",
    )


def create_main_heading(font_size, line_height, text, align):
    return rx.heading(
        text,
        align=align,
        margin_top=Size.DEFAULT.value,
        font_weight="700",
        margin_bottom=Size.SMALL.value,
        font_size=font_size,
        line_height=line_height,
        color=Color.PURPLE,
        as_="h2",
    )


def create_conditions_footer():
    # Deprecated: ya no se usa en Home. Se mantiene por compatibilidad
    # pero la home actual usa bloque informativo colapsable.
    # El gate real está en pack_selection_page.conditions_modal.
    return rx.vstack(
        rx.text(
            "Se recomienda navegador Chrome o Firefox. Safari de iPhone puede dar problemas.",
            font_weight="bold",
            color=Color.PURPLE,
        ),
        spacing="2",
        margin_top="1rem",
        align="center",
    )


def create_description_text(text):
    return rx.text(
        text,
        margin_bottom=Size.MEDIUM.value,
        color=Color.PURPLE_DARK,
        font_size=FontSize.LARGE,
        line_height="1.75rem",
    )


def create_button(text):
    # Home ya no bloquea - el gate real es el modal de packs
    return rx.button(
        text,
        on_click=State.handle_ask_availability_click,
        background_color=Color.PURPLE_BG,
        color=Color.WHITE,
        font_weight="700",
        size="3",
        padding="2.5rem 2rem",
        border_radius=BorderRadius.FULL,
        transition=Transition.DEFAULT,
        _hover={"background_color": Color.PURPLE_LIGHT},
    )


def create_colored_span(text):
    return rx.el.span(text, color=Color.PURPLE)

def create_check_icon():
    return rx.icon(
        tag="check",
        color=Color.PURPLE,
        margin_right="0.5rem",
    )


app = rx.App(style=style)
