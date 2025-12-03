import reflex as rx
from mena_cumples.states.form_state import FormBaseState

def radio_button_food(options: list[str]):
    return rx.radio(
        options,
        size="3",
        default_value=FormBaseState.selected_food_option,
        on_change=lambda val: FormBaseState.update_field("selected_food_option", val)
    )

def radio_button_bakery(options: list[str]):
    return rx.radio(
        options,
        style={"font_size":"20px"},
        default_value=FormBaseState.selected_bakery_option,
        on_change=FormBaseState.update_bakery_option,
        size="3"
    )


