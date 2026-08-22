
import reflex as rx
from .states.state import State # Cambiamos la importación
from .pages.contact_form_page import create_page_layout
from .pages.pack_selection_page import pack_selection
from .pages.pack_15_page import pack_15
from .pages.pack_20_page import pack_20
from .pages.pack_25_page import pack_25
from .pages.pack_30_page import pack_30
from .pages.packs_information_page import packs_information
from .styles.styles import style, Color, FontSize, BorderRadius, Shadow, Transition, Size
from .components.navbar import navbar
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
    """Create the overall page layout including header, main content, and footer."""
    return rx.box(
        rx.box(
            navbar(),
            class_name=Color.GRADIENT_NAVBAR,
            padding=Size.DEFAULT.value,
        ),
        create_main_content(),
        rx.box(
            footer(),
            class_name=Color.GRADIENT_NAVBAR,
            margin_top=Size.XL.value,
            padding_top=Size.MEDIUM.value,
            padding_bottom=Size.MEDIUM.value,
        ),
        background_color=Color.PINK_BG,
    )


def create_main_content():
    """Create the main content of the website including hero, services, and themes sections."""
    return rx.box(
        rx.box(
            create_main_heading(
                font_size=FontSize.XXXL,
                line_height="2.5rem",
                align="center",
                text="¿ Quieres celebrar un cumpleaños ?",
            ),
            create_description_text(
                text="Revisa las condiciones desplegables. Se aceptarán obligatoriamente al elegir tu pack y hacer el pedido.",
            ),
            create_conditions_section(),
            create_button(text="PREGUNTAR DISPONIBILIDAD"),
            create_deposit_text(
                text="A tener en cuenta de que el cumpleaños no está confirmado hasta que no se entregue el depósito de 50€.",
            ),
            text_align="center",
            class_name="fade-in-up",
        ),
        rx.box(
            create_feature_box(
                image_alt="Pastel-colored birthday cake with soft pink and purple decorations",
                image_src="/packs_info_image.webp",
                title="Nuestros Packs de cumples.",
                description="Información de los packs que ofrecemos.",
                href=Routes.PACKS_INFORMATION.value
            ),
            create_order_card(),
            gap=Size.MEDIUM.value,
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            margin_top=Size.XL.value,
            max_width="1000px",
            margin_x="auto",
            class_name="fade-in-up",
            style={"animation_delay": "0.2s"},
        ),
        rx.box(
            create_main_heading(
                font_size=FontSize.XXL,
                line_height="2.25rem",
                align="center",
                text="¡ FELICIDADES !",
            ),
            create_description_text(
                text="¡ Gracias por celebrar este día tan especial con nosotros !"
            ),
            margin_top=Size.XL.value,
            text_align="center",
            class_name="fade-in-up",
            style={"animation_delay": "0.4s"},
        ),
        width="100%",
        max_width="1200px",
        margin_top=Size.MEDIUM.value,
        margin_left="auto",
        margin_right="auto",
    )



def create_conditions_section():
    """Sección informativa colapsable - no bloquea el flujo.

    Las condiciones se aceptan obligatoriamente en el modal de
    pack_selection (pack_selection_page.py:69) y no aquí. En la home
    solo informamos, para que el cliente no pueda decir que no se le avisó,
    pero sin fricción para preguntar disponibilidad o hacer pedido.
    """
    return rx.box(
        rx.el.details(
            rx.el.summary(
                rx.hstack(
                    rx.heading(
                        "¡ CONDICIONES !",
                        font_size=FontSize.XL,
                        line_height="2rem",
                        color=Color.PURPLE,
                        font_weight="700",
                        as_="h3",
                    ),
                    rx.text(
                        "Ver detalle (se aceptarán al pedir)",
                        font_size=FontSize.SMALL,
                        color=Color.PURPLE_DARK,
                        font_weight="600",
                    ),
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
                gap=Size.SMALL.value,
                display="grid",
                grid_template_columns=rx.breakpoints(
                    {
                        "0px": "repeat(1, minmax(0, 1fr))",
                        "768px": "repeat(2, minmax(0, 1fr))",
                    }
                ),
                margin_top=Size.SMALL.value,
            ),
            rx.box(
                rx.text(
                    "Las condiciones se aceptarán obligatoriamente al elegir tu pack. "
                    "Al continuar, confirmas que las has leído.",
                    font_size=FontSize.SMALL,
                    color=Color.PURPLE_DARK,
                    font_weight="600",
                    margin_top=Size.SMALL.value,
                    font_style="italic",
                ),
                rx.text(
                    "Se recomienda navegador Chrome o Firefox. Safari de iPhone puede dar problemas.",
                    font_weight="bold",
                    color=Color.PURPLE,
                    font_size=FontSize.SMALL,
                    margin_top="0.5rem",
                ),
            ),
            style={"border": "none"},
        ),
        background_color=Color.CARD_PINK,
        margin_top=Size.MEDIUM.value,
        margin_bottom=Size.MEDIUM.value,
        padding=Size.DEFAULT.value,
        border_radius=BorderRadius.MEDIUM,
    )


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
        create_check_icon(),
        create_colored_span(text=text),
        display="flex",
        align_items="center",
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


def create_order_card():
    """Tarjeta de acceso al pedido - siempre activa.

    El gate de condiciones ya no está en Home. La aceptación
    obligatoria vive en pack_selection.conditions_modal.
    """
    return rx.box(
        rx.image(
            src="/pedidos_image.webp",
            alt="seleccion del pack",
            border_radius=BorderRadius.SMALL,
        ),
        create_main_heading(
            font_size=FontSize.XL,
            line_height="2rem",
            align="center",
            text="¡ Haz tu pedido !",
        ),
        create_description_text(
            "Introduce el código de reserva que recibiste por WhatsApp para elegir tu pack."
        ),
        rx.input(
            on_change=State.set_order_code,
            value=State.order_code,
            type="text",
            placeholder="Código de reserva (ej: CUM-7XD4)",
            width="100%",
            padding=Size.SMALL.value,
            border_radius=BorderRadius.SMALL,
            margin_bottom=Size.SMALL.value,
            font_size=FontSize.INPUT,
            color=Color.BLACK,
            background_color=Color.WHITE,
            border=f"1px solid {Color.GRAY_BORDER}",
            height="3rem",
            line_height="1.25rem",
            text_transform="uppercase",
        ),
        rx.button(
            "HACER PEDIDO",
            on_click=State.submit_order_code,
            background_color=Color.PURPLE_BG,
            color=Color.WHITE,
            font_weight="700",
            width="100%",
            size="3",
            padding="1.25rem 1rem",
            border_radius=BorderRadius.FULL,
            transition=Transition.DEFAULT,
            _hover={"background_color": Color.PURPLE_LIGHT},
        ),
        padding=Size.MEDIUM.value,
        box_shadow=Shadow.CARD,
        border_radius=BorderRadius.SMALL,
        background_color=Color.WHITE,
    )


def create_description_text(text):
    return rx.text(
        text,
        margin_bottom=Size.MEDIUM.value,
        color=Color.PURPLE_DARK,
        font_size=FontSize.LARGE,
        line_height="1.75rem",
    )

def create_deposit_text(text):
    # Banner alto contraste - fix overlap del pill 50€ con línea superior
    _ = text
    return rx.box(
        rx.flex(
            rx.icon(tag="triangle-alert", color=Color.ERROR, size=28, flex_shrink="0"),
            rx.text(
                "A tener en cuenta: el cumpleaños ",
                rx.el.span(
                    "NO está confirmado",
                    font_weight="900",
                    text_decoration="underline",
                    text_decoration_thickness="2px",
                ),
                " hasta entregar el depósito de ",
                rx.el.span(
                    "50€",
                    font_weight="900",
                    font_size=FontSize.LARGE,
                    background_color=Color.ERROR,
                    color=Color.WHITE,
                    padding="0.1rem 0.45rem",
                    border_radius="9999px",
                    display="inline-block",
                    line_height="1",
                    vertical_align="middle",
                    white_space="nowrap",
                    margin_left="0.2rem",
                ),
                ".",
                color=Color.ERROR,
                font_size=FontSize.LARGE,
                line_height="2rem",
                font_weight="700",
                text_align="left",
                flex="1",
                min_width="0",
            ),
            direction="row",
            align="center",
            justify="center",
            gap="0.75rem",
            wrap="nowrap",
            width="100%",
        ),
        background_color=Color.ERROR_BG,
        border=f"2px solid {Color.ERROR}",
        border_left=f"6px solid {Color.ERROR}",
        border_radius=BorderRadius.MEDIUM,
        padding="1rem 1.25rem",
        margin_top=Size.MEDIUM.value,
        box_shadow="0 4px 12px rgba(220, 38, 38, 0.15)",
        width="100%",
        max_width="850px",
        margin_x="auto",
        class_name="scale-in",
        overflow="hidden",
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


def create_feature_box(image_src, image_alt, title, description, href, conditions_acepted=True):
    # Home informativo, siempre activo. El bloqueo real es en packs.
    _ = conditions_acepted  # compat param
    return rx.link(
        rx.box(
            rx.image(src=image_src, alt=image_alt, border_radius=BorderRadius.SMALL),
            create_main_heading(
                font_size=FontSize.XL,
                line_height="2rem",
                align="center",
                text=title,
            ),
            create_description_text(description),
            padding=Size.MEDIUM.value,
            box_shadow=Shadow.CARD,
            border_radius=BorderRadius.SMALL,
            background_color=Color.WHITE,
            _hover={"text_decoration": "none"},
        ),
        href=href,
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
