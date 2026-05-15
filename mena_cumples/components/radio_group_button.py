import reflex as rx
from mena_cumples.styles.styles import FontSize
from mena_cumples.states.form_state import FormBaseState

def radio_button_food(options: list[str]):
    return rx.radio(
        options,
        direction="column",
        size="3",
        default_value=FormBaseState.selected_food_option,
        on_change=lambda new_value: FormBaseState.update_field("selected_food_option", new_value)
    )

def radio_button_bakery(options: list[str]):
    return rx.radio(
        options,
        direction="column",
        style={"font_size": FontSize.INPUT},
        on_change=FormBaseState.update_bakery_option,
        size="3"
    )


