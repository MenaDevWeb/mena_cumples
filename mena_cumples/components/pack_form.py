import reflex as rx
from mena_cumples.styles.styles import Size
from .radio_group_button import radio_button_food  
from .radio_group_button import radio_button_bakery
from mena_cumples.styles.styles import style
from mena_cumples.states.form_state import FormBaseState

def pack_form(
    state = FormBaseState,
    pack_type: str = "",
    image_url: str = "",
    name_title: str = "", 
    date_time: str = "",
    time_description: str = "",
    sandwiches_text: str = "",
    food_options: list[str] = [],  
    pack_description: str = "",
    tortilla_description: str = "",
    pizza_title: str = "",
    pizza_description: str = "",
    drink_title: str = "",
    drink_description: str = "",
    extra_title: str = "",
    extra_description: str = "" ,
    bakery_title: str = "",
    bakery_options: list[str] = [],
    observation_title: str = "",
    child_name_value: str = "",
    child_age_value: str = "",  
    birth_date_value: str = "",  
    birth_time_value: str = "",
    pizza_selected_value: dict = {}, 
    rosca_selected_value: dict = {},  
    drink_selected_value: dict = {},  # Cambiado a diccionario
    extra_selected: str = "",
    observation_selected_value: str = "",
    max_allowed: int = 3
) -> rx.Component:
    return rx.container(
        rx.card(
            rx.vstack(
                rx.alert_dialog.root(
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Límite excedido"),
                        rx.alert_dialog.description(
                            rx.cond(
                                FormBaseState.alert_type == "pizzas_roscas",
                                rx.text(FormBaseState.alert_message),
                                rx.text(FormBaseState.alert_message)
                            )
                        ),
                        rx.flex(
                            rx.alert_dialog.action(
                                rx.button("Entendido", on_click=FormBaseState.close_alert_dialog),
                            ),
                            spacing="3",
                        ),
                    ),
                    open=FormBaseState.show_alert,
                ),
                rx.image(
                    src=image_url,
                    width="30%",
                    height="auto",
                    border_radius="12px",
                    margin_bottom=Size.BIG.value,
                    margin_top=Size.MEDIUM.value
                ),
                rx.heading(pack_type),
                datos_personales(name_title, child_name_value, child_age_value, date_time, time_description, birth_date_value),
                seleccion_alimentos(sandwiches_text, food_options, pack_description, tortilla_description),
                seleccion_pizzas(pizza_title, pizza_description, pizza_selected_value, rosca_selected_value, max_allowed),
                seleccion_bebidas(drink_title, drink_description, drink_selected_value, max_allowed),  # Integrado
                extras_y_observaciones(extra_title, extra_description, extra_selected, bakery_title, bakery_options, observation_title, observation_selected_value),
                align="center",
                width="100%",
                
            ),
            align="center",
            bg="#a588af",
            size="5",
            padding="12px",
            margin_top="20px"
        ),
        justify="center",
        align="center",
        width="100%",
        margin=["0", "auto"],
        stack_children_full_width=True
    )

# Función para la sección de datos personales
def datos_personales(name_title, child_name_value, child_age_value, date_time, time_description, birth_date_value):
    return rx.vstack(
        rx.text(name_title, weight="bold", margin_top="20px"),
        rx.hstack(
            rx.input(
                placeholder="Nombre", 
                value=child_name_value,
                on_change=lambda new_value: FormBaseState.update_field("child_name", new_value),
                style={"width": "180px", "height": "40px", "font_size": "16px"},
            ),
            rx.input(
                placeholder="Edad", 
                value=child_age_value,
                on_change=lambda new_value: FormBaseState.update_field("child_age", new_value),
                style={"width": "100px", "height": "40px", "font_size": "16px"},
                type="number"
            ),
            spacing="4",
            wrap="wrap",
            width="100%",
        ),
        rx.spacer(height="50px"),
        rx.vstack(
            rx.text(date_time, weight="bold", margin_top="30px"),
            rx.text(time_description, style={"font_style": "italic"}),
            rx.hstack(
                rx.input(
                    placeholder="Fecha",
                    type="date",
                    value=birth_date_value,
                    on_change=lambda new_value: FormBaseState.update_field("birth_date", new_value),
                    style={"width": "180px", "height": "40px", "font_size":"16px"}
                ),
                rx.select(
                    ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30"],
                    name="birth_time",
                    placeholder="Hora", 
                    on_change=lambda new_value: FormBaseState.update_field("birth_time", new_value),  # Ajuste para que use `update_field`
                    size="3",
                    value=FormBaseState.birth_time,
                    style={"width": "180px", "height": "70px", "font_size":"16px"},
                ),
                spacing="4",
                wrap="wrap",
                width="100%",
            ),
        ),
    )

# Función para la selección de alimentos
def seleccion_alimentos(sandwiches_text, food_options, pack_description, tortilla_description):
    return rx.vstack(
        rx.text(sandwiches_text, weight="bold", margin_top="30px"),
        rx.flex(radio_button_food(food_options), margin_top="20px", margin_bottom="20px"),
        rx.text(pack_description, margin_top="20px", color_scheme="purple", size="4", weight="bold", style={"font_style": "italic"}),
        rx.text(tortilla_description, size="5", weight="bold", style={"font_style":"italic"}, margin_top="30px", color_scheme="purple")
    )

# Función para la selección de pizzas y roscas con inputs pequeños (1 dígito)
def seleccion_pizzas(pizza_title, pizza_description, pizza_selected_values, rosca_selected_values, max_allowed):
    pizza_types = ["margarita", "prosciutto", "salchicha", "pepperoni", "atún"]
    rosca_types = ["mixta", "atún", "lomo", "catalana"]

    # Ensure pizza_selected_values is a dictionary
    if not isinstance(pizza_selected_values, dict):
        pizza_selected_values = {pizza_type: 0 for pizza_type in pizza_types}

    # Ensure rosca_selected_values is a dictionary
    if not isinstance(rosca_selected_values, dict):
        rosca_selected_values = {rosca_type: 0 for rosca_type in rosca_types}

    pizza_inputs = [
        rx.hstack(
            rx.input(
                placeholder="0",
                value=str(pizza_selected_values.get(pizza_type, 0)),
                on_change=lambda new_value, pizza_type=pizza_type: FormBaseState.update_pizza_selected(pizza_type, new_value),
                max_length=1,
                type="number",
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},
            ),
            rx.text(pizza_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for pizza_type in pizza_types
    ]

    rosca_inputs = [
        rx.hstack(
            rx.input(
                placeholder=f"0",  # Placeholder for a single digit
                value=str(rosca_selected_values.get(rosca_type, 0)),
                on_change=lambda new_value, rosca_type=rosca_type: FormBaseState.update_rosca_selected(rosca_type, new_value),
                max_length=1,  # Restrict to 1 character (single digit)
                type="number",  # Ensure it's a number
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},  # Smaller width for single-digit input
            ),
            rx.text(rosca_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for rosca_type in rosca_types
    ]

    return rx.vstack(
        rx.text(pizza_title, weight="bold"),
        rx.text(pizza_description, style={"font_style": "italic", "font_size": "16px"}),
        rx.hstack(
            rx.vstack(
                rx.text("Pizzas", weight="bold"),
                *pizza_inputs,
                align_items="start",
                margin_right="20px"
            ),
            rx.vstack(
                rx.text("Roscas", weight="bold"),
                *rosca_inputs,
                align_items="start"
            ),
            justify_content="space-between"
        ),
        margin_top="20px"
    )

# Función para la selección de bebidas
def seleccion_bebidas(drink_title, drink_description, drink_selected_values, max_allowed):
    drink_types_col1 = ["Cola", "Cola Zero", "Cola Zero Zero", "Fanta Naranja", "Fanta Limón"]
    drink_types_col2 = ["Zumo de Piña", "Zumo de Melocotón", "Batido de Chocolate", "Batido de Fresa", "Botella de Agua"]

    # Ensure drink_selected_values is a dictionary
    if not isinstance(drink_selected_values, dict):
        drink_selected_values = {drink_type: 0 for drink_type in drink_types_col1 + drink_types_col2}

    drink_inputs_col1 = [
        rx.hstack(
            rx.input(
                placeholder="0",
                value=str(drink_selected_values.get(drink_type, 0)),
                on_change=lambda new_value, drink_type=drink_type: FormBaseState.update_drink_selected(drink_type, new_value),
                max_length=1,
                type="number",
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},
            ),
            rx.text(drink_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for drink_type in drink_types_col1
    ]

    drink_inputs_col2 = [
        rx.hstack(
            rx.input(
                placeholder="0",
                value=str(drink_selected_values.get(drink_type, 0)),
                on_change=lambda new_value, drink_type=drink_type: FormBaseState.update_drink_selected(drink_type, new_value),
                max_length=1,
                type="number",
                min=0,
                style={"width": "50px", "height": "40px", "font_size": "16px"},
            ),
            rx.text(drink_type, style={"font_size": "16px", "font_style": "italic"}),
            align_items="center",
            margin_bottom="10px"
        ) for drink_type in drink_types_col2
    ]

    return rx.vstack(
        rx.text(drink_title, weight="bold", margin_top="30px"),
        rx.text(drink_description, style={"font_style": "italic", "font_size": "16px"}),
        rx.hstack(
            rx.vstack(
                rx.text("Refrescos", weight="bold"),
                *drink_inputs_col1,
                align_items="start",
                margin_right="20px"
            ),
            rx.vstack(
                rx.text("Zumos, batidos, agua", weight="bold"),
                *drink_inputs_col2,
                align_items="start"
            ),
            justify_content="space-between"
        ),
        margin_top="20px"
    )


# Función para extras y observaciones
def extras_y_observaciones(extra_title, extra_description, extra_selected, bakery_title, bakery_options, observation_title, observation_selected_value):
    return rx.vstack(
        rx.text(extra_title, weight="bold", margin_top="30px"),
        rx.text(extra_description, style={"font_style":"italic"}),
        rx.spacer(margin_top="20px"),
        rx.input(
            placeholder="Extras", 
            value=extra_selected,
            on_change=lambda new_value: FormBaseState.update_field("extra_selected", new_value),
            style={"width": "85%", "height": "32px"},
        ),
        rx.text(bakery_title, weight="bold", margin_top="30px"),
        rx.flex(radio_button_bakery(bakery_options), margin_top="20px"),
        rx.text(observation_title, weight="bold", margin_top="30px"),
        rx.text_area(
            placeholder="Observaciones", 
            value=observation_selected_value,
            on_change=lambda new_value: FormBaseState.update_field("observation_selected", new_value),
            style={"width": "85%", "height": "80px"},
            margin_top="20px"
        )
    )

# Función para aceptar condiciones
def aceptar_condiciones():
    return rx.vstack(
        rx.checkbox(
            rx.text(
                "He leído y acepto las condiciones. (acepte para poder enviar el pedido)",
                color="black", font_size="14px", font_weight="bold", margin_bottom="20px"
            ),
            on_change=lambda new_value: FormBaseState.update_field("conditions_acepted", new_value),
            required=True
        ),
        spacing="2", margin_top="20px"
    )

# Función para seleccionar el pack
def select_pack_component():
    return rx.vstack(
        rx.select(
            [
                rx.option("Pack_15", value="Pack_15"),
                rx.option("Pack_20", value="Pack_20"),
                rx.option("Pack_25", value="Pack_25"),
                rx.option("Pack_30", value="Pack_30"),
            ],
            on_change=lambda value: FormBaseState.select_pack(value),
            placeholder="Selecciona un pack",
        ),
        rx.text(
            "Máximo permitido: {FormBaseState.max_allowed_pizza_rosca}",
            key="max_allowed_text",
        ),
    )