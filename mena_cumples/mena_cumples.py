
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
from .routes import Routes


@rx.page(route=Routes.INDEX.value, title="Cumpleaños Mena Plaza")
def index() -> rx.Component:
    return rx.fragment(
        create_main_screen()
    )

def create_main_screen():
    """Create the main application component with styles and page layout."""
    return rx.fragment(
        rx.el.link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
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
                text="Debe aceptar las condiciones antes de consultar disponibilidad o realizar su pedido.",
            ),
            create_conditions_section(),
            create_button(text="PREGUNTAR DISPONIBILIDAD"),
            create_deposit_text(
                text="A tener en cuenta de que el cumpleaños no está confirmado hasta que no se entregue el depósito de 50€.",
            ),
            text_align="center",
        ),
        rx.box(
            create_feature_box(
                image_alt="Pastel-colored birthday cake with soft pink and purple decorations",
                image_src="/packs_info_image.webp",
                title="Nuestros Packs de cumples.",
                description="Información de los packs que ofrecemos.",
                href=Routes.PACKS_INFORMATION.value
            ),
            create_feature_box(
                image_alt="seleccion del pack",
                image_src="/pedidos_image.webp",
                title="¡ Haz tu pedido !",
                description="Debe aceptar condiciones y seleccione pack.",
                href=Routes.PACK_SELECTION.value,
                conditions_acepted=State.conditions_acepted  # Usamos state
            ),
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
        ),
        width="100%",
        max_width="1200px",
        margin_top=Size.MEDIUM.value,
        margin_left="auto",
        margin_right="auto",
    )



def create_conditions_section():
    """Create the 'Condiciones:' section with feature list."""
    return rx.box(
        create_main_heading(
            font_size=FontSize.XXL,
            line_height="2.25rem",
            align="left",
            text="¡ CONDICIONES !",
        ),
        rx.list(
            create_list_item_with_icon(
                text= "Está prohibida bebida o comida de fuera del establecimiento."
            ),
            create_list_item_with_icon(
                text= "La edad máxima para elegir los packs de cumples es de 12 años."
            ),
            create_list_item_with_icon(
                text= "Las mesas y sillas se montarán dependiendo del pack que elija."
            ),
            create_list_item_with_icon(
                text= "La duración máxima del cumpleaños es de 2 horas y media."
            ),
            create_list_item_with_icon(
                text= "Las chucherías se permiten en cucuruchos (mesas de chuches no)"
            ),
            create_list_item_with_icon(
                text= "Los 50€ de fianza son no reembolsables en caso de cancelación."   
            ),
            create_list_item_with_icon(
                text= "La celebración puede empezar a más tardar a las 19:30h (18:30h desde noviembre)."
            ),
            create_list_item_with_icon(
                text= "No colocamos mesas auxiliares aparte, solamente será la mesa del cumpleaños."
            ),
            create_list_item_with_icon(
                text= "La decoración depende del espacio ¡No se puede decorar la pared del supermercado!"
            ),
            create_list_item_with_icon(
                text= "La fecha que elijas no podrá cambiarse más adelante."
            ),
            create_list_item_with_icon(
                text="Puedes modificar el pack, según disponibilidad, pero no cambiar a un pack menor."
            ),
            create_list_item_with_icon(
                text = "Para reservar, primero confirmar nº de personas y hora."
            ),            
            gap=Size.SMALL.value,
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        ),
        create_conditions_footer(),

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
    return rx.vstack(
        rx.checkbox(
            rx.text(
                "He leído y acepto las condiciones. (acepte para poder preguntar por disponibilidad)",
                color=Color.PINK, font_size="18px", font_weight="bold", margin_bottom="20px"
            ),
            on_change=State.set_conditions_acepted,
            required=True,
            color_scheme="purple",
            size='3'
        ),
        rx.text(
            "Se recomienda navegador Chrome o Firefox. Safari de iphone puede dar problemas.",
            font_weight="bold",
            color=Color.PURPLE,
        ),
        spacing="2",
        margin_top="40px",
        align="center",
        margin_bottom=Size.MEDIUM.value,
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
    return rx.text(
        text,
        margin_top=Size.MEDIUM.value,
        color=Color.ERROR,
        font_size=FontSize.LARGE,
        line_height="1.75rem",
        font_weight="bold"
    )

def create_button(text):
    return rx.cond(
        State.conditions_acepted,
        rx.button(
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
        ),
        rx.button(
            text,
            background_color="#ebe2f8",
            color=Color.GRAY_TEXT,
            font_weight="700",
            padding="2.5rem 2rem",
            border_radius=BorderRadius.FULL,
            cursor="not-allowed",
            opacity=0.6,
        ),
    )


def create_feature_box(image_src, image_alt, title, description, href, conditions_acepted=True):
    return rx.cond(
        conditions_acepted,
        rx.link(
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
        ),
        rx.box(
            rx.image(src=image_src, alt=image_alt, border_radius=BorderRadius.SMALL, opacity=0.6),
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
            background_color=Color.GRAY_DISABLED,
            cursor="not-allowed",
            opacity=0.6,
        )
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
