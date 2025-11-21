import reflex as rx
from mena_cumples.styles.styles import Size
from .radio_group_button import radio_button_food  
from .radio_group_button import radio_button_bakery
from mena_cumples.styles.styles import style
from mena_cumples.states.form_state import FormBaseState

def pack_form(
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
    drink_selected_value: dict = {},  
    extra_selected: str = "",
    observation_selected_value: str = "",
    max_allowed: int = 3
) -> rx.Component:
    return rx.fragment(
        # Modal de alerta solo cuando show_alert está activo (AHORA FUERA DEL FORM)
        rx.cond(
            FormBaseState.show_alert,
            rx.el.div(
                rx.el.div(
                    rx.el.h2("Límite Excedido", class_name="text-xl font-bold text-red-600 mb-3"),
                    rx.el.p(FormBaseState.alert_message, class_name="text-sm text-gray-700"),
                    rx.el.div(
                        rx.el.button(
                            "Entendido", 
                            on_click=FormBaseState.reset_alert,
                            type="button",  # Sigue siendo bueno tener type="button" aquí
                            class_name="mt-5 px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        ),
                        class_name="flex justify-end pt-3"
                    ),
                    class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-md mx-auto"
                ),
                class_name="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-4"
            )
        ),
        rx.el.form(
            rx.el.div(
                # Card: Encabezado e Información del Pack
                rx.el.div(
                    rx.cond(
                        image_url != "",
                        rx.el.img(src=image_url, class_name="w-full h-auto rounded-md mb-4 max-h-60 object-cover"),
                        rx.el.div()
                    ),
                    rx.heading(pack_type,size="8",align="center", width="100%", margin_top="20px"),
                    rx.text(pack_description, margin_top="2em", color_scheme="purple", size="4", weight="bold", style={"font_style": "italic"}),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#f5cade"}
                ),
                # Card: Datos del Cumpleañero/a
                rx.el.div(
                    datos_personales(name_title, child_name_value, child_age_value, date_time, time_description, birth_date_value),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#dcd4ee"}
                ),
                # Card: Opciones de Comida
                rx.el.div(
                    seleccion_alimentos(sandwiches_text, food_options, tortilla_description),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#dcd4ee"}
                ),
                # Card: Pizzas y Roscas
                rx.el.div(
                    seleccion_pizzas(pizza_title, pizza_description, pizza_selected_value, rosca_selected_value, max_allowed),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#dcd4ee"}
                ),
                # Card: Bebidas
                rx.el.div(
                    seleccion_bebidas(drink_title, drink_description, drink_selected_value, max_allowed),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#dcd4ee"}
                ),
                # Card: Extras y Observaciones
                rx.el.div(
                    extras_y_observaciones(extra_title, extra_description, extra_selected, bakery_title,bakery_options, observation_title, observation_selected_value),
                    class_name="p-4 rounded-lg shadow mb-4",
                    style={"backgroundColor": "#dcd4ee"}
                ),
                # Botón de envío
                rx.el.button(
                    "ENVIAR",
                    rx.el.img(
                        src="/whatsapp_ico.ico",
                        width="24px",  # Icono ligeramente más grande
                        height="24px",
                        class_name="ml-3"  # Espacio entre el texto y el icono
                    ),
                    # on_click=FormBaseState.send_whatsapp_message, # Eliminado para evitar doble llamada
                    type="submit", # Asegura que este botón envíe el formulario
                    class_name=(
                        "mt-8 mb-6 px-8 py-3 text-lg "
                        "bg-green-600 hover:bg-green-700 text-white "
                        "font-semibold rounded-lg shadow-md "
                        "flex items-center justify-center "
                        "transition-all duration-150 ease-in-out " # Cambiado a transition-all
                        "focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-75 "
                        "min-w-[220px] hover:shadow-lg "
                        "disabled:bg-gray-400 disabled:text-gray-600 disabled:cursor-not-allowed disabled:shadow-none" # Estilos para deshabilitado
                    ),
                    width="100%",
                    disabled=~FormBaseState.can_send,
                ),
                
                width="100%",
                align="center", # Este div padre centrará el botón            
            ),
            on_submit=FormBaseState.send_whatsapp_message, # El formulario maneja el envío
            reset_on_submit=True,
            class_name="max-w-3xl mx-auto my-8 p-4 md:p-6 bg-gray-100 rounded-xl shadow-2xl"
        )
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
                    ["16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00"],
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
def seleccion_alimentos(sandwiches_text, food_options, tortilla_description):
    return rx.vstack(
        rx.text(sandwiches_text, weight="bold", margin_top="30px"),
        rx.hstack(
            rx.checkbox(
                checked=FormBaseState.butter_on_sandwiches,
                on_change=lambda new_value: FormBaseState.update_field("butter_on_sandwiches", new_value),
                size="3"
            ),
            rx.text(
                "Marcar si desea que los bocadillos lleven mantequilla",
                style={
                    "font_size": "16px", 
                    "font_style": "italic",
                    "color": "#dc2626",
                    "font_weight": "600"
                }
            ),
            align_items="center",
            spacing="3",
            margin_top="15px",
            margin_bottom="10px"
        ),
        rx.flex(radio_button_food(food_options), margin_top="20px", margin_bottom="20px"),
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
            style={"width": "100%", "height": "50px"},
        ),
        rx.text(bakery_title, weight="bold", margin_top="30px"),
        rx.flex(radio_button_bakery(bakery_options), margin_top="20px"),
        rx.text(observation_title, weight="bold", margin_top="30px"),
        rx.text_area(
            placeholder="Observaciones", 
            value=observation_selected_value,
            on_change=lambda new_value: FormBaseState.update_field("observation_selected", new_value),
            style={"width": "100%", "height": "80px"},
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