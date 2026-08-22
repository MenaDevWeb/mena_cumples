import reflex as rx
from mena_cumples.styles.styles import FontSize, Color
from mena_cumples.states.form_state import FormBaseState

def radio_button_food(options: list[str]):
    return rx.radio(
        options,
        direction="column",
        size="3",
        color_scheme="purple",
        default_value=FormBaseState.selected_food_option,
        on_change=lambda new_value: FormBaseState.update_field("selected_food_option", new_value),
    )

def radio_button_bakery(options: list[str]):
    return rx.radio(
        options,
        direction="column",
        size="3",
        color_scheme="purple",
        style={
            "font_size": FontSize.INPUT,
            "line_height": "1.4",
            "color": Color.PURPLE_DARK,
        },
        on_change=FormBaseState.update_bakery_option,
    )


