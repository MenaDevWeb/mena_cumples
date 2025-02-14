import reflex as rx
from mena_cumples.states.form_state import FormBaseState

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
            create_header(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200",
            padding="1rem",
        ),
        create_main_content(),
        rx.box(
            create_footer(),
            class_name="bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200",
            margin_top="4rem",
            padding_top="2rem",
            padding_bottom="2rem",
        ),
        background_color="#FDF2F8",
    )


def create_header():
    """Create the website header with logo and navigation links."""
    return rx.flex(
        rx.image(
            src="/cumpleMena.png",
            height="auto",
            width="200px"
            
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        align_items="center",
        justify_content="space-between",
        margin_left="auto",
        margin_right="auto",
    )


def create_main_content():
    """Create the main content of the website including hero, services, and themes sections."""
    return rx.box(
        rx.box(
            create_main_heading(
                font_size="2.25rem",
                line_height="2.5rem",
                align="center",
                text="¿ Quieres celebrar un cumpleaños ?",
            ),
            create_description_text(
                text="Debe aceptar las condiciones antes de consultar disponibilidad o realizar su pedido.",                
            ),
            create_conditions_section(),

            create_button(
                text="PREGUNTAR DISPONIBILIDAD",
                
            ),
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
                href="/packs_information"
            ),
            create_feature_box(
                image_alt="seleccion del pack",
                image_src="/pedidos_image.webp",
                title="¡ Haz tu pedido !",
                description="Debe aceptar condiciones y seleccione pack.",
                href="/pack_selection",
                conditions_acepted=FormBaseState.conditions_acepted  # Pasamos el estado de condiciones aceptadas
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            margin_top="4rem",
            max_width="1000px",  # Ajusta este valor según tus necesidades
            margin_x="auto",  # Esto centrará el contenido
        ),
        rx.box(
            create_main_heading(
                font_size="1.875rem",
                line_height="2.25rem",
                align="center",
                text="¡ FELICIDADES !",
            ),
            create_description_text(
                text="¡ Gracias por celebrar este día tan especial con nosotros !"
            ),
            margin_top="4rem",
            text_align="center",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_top="2rem",
        margin_left="auto",
        margin_right="auto",
    )


def create_footer():
    """Create the website footer with copyright and social media links."""
    return rx.box(
        create_colored_text(
            text="© 2024 Developed by Gabriel Visiedo."
        ),
        rx.flex(
            create_social_link(icon_name="facebook", href="https://www.facebook.com/p/Hotel-Mena-Plaza-Nerja-100079174651992/"),
            create_social_link(icon_name="instagram", href="https://www.instagram.com/menaplaza/?hl=es"),
            display="flex",
            justify_content="center",
            margin_top="1rem",
            column_gap="1rem",
        ),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        margin_left="auto",
        margin_right="auto",
        text_align="center",
    )


def create_conditions_section():
    """Create the 'Condiciones:' section with feature list."""
    return rx.box(
        create_main_heading(
            font_size="1.875rem",
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
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        ),
        create_conditions_footer(),

        background_color="#EDE9FE",
        margin_top="2rem",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
    )


def create_list_item(item_text):
    """Create a list item with a styled link."""
    return rx.el.li(create_link(text=item_text))


def create_link(text):
    """Create a styled link element with hover effect."""
    return rx.el.a(
        text,
        href="#",
        _hover={"color": "#5B21B6"},
        color="#7C3AED",
    )


def create_list_item_with_icon(text):
    """Create a list item with a check icon and colored text."""
    return rx.el.li(
        create_check_icon(),
        create_colored_span(text=text),
        display="flex",
        align_items="center",
    )


def create_main_heading(font_size, line_height, text, align):
    """Create a styled main heading (h2) with custom font size and line height."""
    return rx.heading(
        text,
        align=align,
        margin_top="1.5rem",
        font_weight="700",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        color="#7C3AED",
        as_="h2",
    )


def create_conditions_footer():
    return rx.vstack(
        rx.checkbox(
            rx.text(
                "He leído y acepto las condiciones. (acepte para poder preguntar por disponibilidad)",
                color="#e926a8", font_size="18px", font_weight="bold", margin_bottom="20px"
            ),
            on_change=lambda new_value: FormBaseState.update_field("conditions_acepted", new_value),
            required=True,
            color_scheme="violet"
        ),
        rx.text(
            "Se recomienda navegador Chrome o Firefox. Safari de iphone puede dar problemas.",
            font_weight="bold",
            color="#7C3AED"               
                
        ),

        spacing="2", 
        margin_top="40px",
        align="center",
        margin_bottom="2rem"
    )


def create_description_text(text):
    """Create a styled description text with specific formatting."""
    return rx.text(
        text,
        margin_bottom="2rem",
        color="#6D28D9",
        font_size="1.25rem",
        line_height="1.75rem",
    )

def create_deposit_text(text):
    return rx.text(
        text,
        margin_top="2rem",
        color="red",
        font_size="1.25rem",
        line_height="1.75rem",
        font_weight="bold"
    )

def create_button(text):
    """Create a styled button with hover effect and transition properties."""
    return rx.cond(
        FormBaseState.conditions_acepted,
        rx.button(
            text,
            on_click=FormBaseState.handle_button_click,
            background_color="#A78BFA",
            color="#ffffff",
            font_weight="700",
            size="3",
            padding="2.5rem 2rem",
            border_radius="9999px",
            transition="background-color 300ms ease-in-out",
            _hover={"background_color": "#8B5CF6"},
        ),
        rx.button(
            text,
            background_color="#ebe2f8",  # A muted color for the disabled state
            color="#9CA3AF",  # A muted text color
            font_weight="700",
            padding="2.5rem 2rem",
            border_radius="9999px",
            cursor="not-allowed",
            opacity=0.6,
        ),
    )


def create_feature_box(image_src, image_alt, title, description, href, conditions_acepted=True):
    """Create a styled feature box with image, heading, and description, optionally disabled based on conditions."""
    
    # Condición para activar o desactivar la tarjeta según si se han aceptado las condiciones
    return rx.cond(
        conditions_acepted,
        rx.link(
            rx.box(
                rx.image(src=image_src, alt=image_alt, border_radius="0.5rem"),
                create_main_heading(
                    font_size="1.5rem",
                    line_height="2rem",
                    align="center",
                    text=title,
                ),
                create_description_text(description),
                padding="2rem",
                box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
                border_radius="0.5rem",
                background_color="white",
                _hover={"text_decoration": "none"},  # Efecto de hover solo si está habilitado
            ),
            href=href,
        ),
        # Versión desactivada si no se aceptan las condiciones
        rx.box(
            rx.image(src=image_src, alt=image_alt, border_radius="0.5rem", opacity=0.6),
            create_main_heading(
                font_size="1.5rem",
                line_height="2rem",
                align="center",
                text=title,
            ),
            create_description_text(description),
            padding="2rem",
            box_shadow="0px 4px 6px rgba(0, 0, 0, 0.1)",
            border_radius="0.5rem",
            background_color="#f0f0f0",  # Color más apagado para la versión desactivada
            cursor="not-allowed",
            opacity=0.6,  # Opacidad reducida para resaltar que está desactivada
        )
    )


def create_colored_span(text):
    """Create a span element with purple-colored text."""
    return rx.el.span(text, color="#7C3AED")


def create_colored_text(text):
    """Create a paragraph with purple-colored text."""
    return rx.text(text, color="#7C3AED")


def create_check_icon():
    """Create a check icon with purple color."""
    return rx.icon(
        tag="check",
        color="#7C3AED",
        margin_right="0.5rem",
    )


def create_social_link(icon_name,href):
    """Create a styled link with a Lucide icon for social media."""
    return rx.el.a(
        rx.icon(
            tag=icon_name,
            font_family="LucideIcons",
            font_size="1.5rem",
            color="#7C3AED",
        ),
        href=href,
        transition_duration="300ms",
        _hover={"color": "#5B21B6"},
    )