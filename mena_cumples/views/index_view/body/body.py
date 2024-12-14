import reflex as rx
from mena_cumples.styles.styles import Size
from mena_cumples.states.state import State

def body() -> rx.Component:
        return rx.center (
            rx.card(
                rx.text(
                    "PACK DE 90€---PARA 15 PERSONAS",
                    margin_top = Size.LARGE.value,
                    weight="bold"
                ),
            rx.button(
                rx.text("Selecciona"),
                variant = "surface",
                color_scheme = "plum",
                width = "100%",
                margin_top = Size.SMALL.value,
                on_click=lambda: State.navigate_to_15                    
                ), 
            rx.text(
                "PACK DE 120€---PARA 20 PERSONAS",
                margin_top = Size.LARGE.value,
                weight="bold"
                ),
            rx.button(
                rx.text("Selecciona"),
                variant = "surface",
                color_scheme = "plum",
                width = "100%",
                margin_top = Size.SMALL.value,
                on_click=lambda: State.navigate_to_20
            ),
            rx.text(
                "PACK DE 150€---PARA 25 PERSONAS",
                margin_top = Size.LARGE.value,
                weight="bold"
                ),
            rx.button(
                rx.text("Selecciona"),
                variant = "surface",
                color_scheme = "plum",
                width = "100%",
                margin_top = Size.SMALL.value,
                on_click=lambda: State.navigate_to_25
            ),
            rx.text(
                "PACK DE 180€---PARA 30 PERSONAS",
                margin_top = Size.LARGE.value,
                weight="bold"
                ),
            rx.button(
                rx.text("Selecciona"),
                variant = "surface",
                color_scheme = "plum",
                width = "100%",
                margin_top = Size.SMALL.value,
                on_click=lambda: State.navigate_to_30
            ),
            rx.text(
                "PACK DE 5,95€---POR NIÑO",
                margin_top = Size.LARGE.value,
                weight="bold",
                align="center",
                ),
            rx.button(
                rx.text("Selecciona"),
                variant = "surface",
                color_scheme = "plum",
                width = "100%",
                margin_top = Size.SMALL.value,
                #on_click=lambda: State.navigate_to_595
            ),
        variant = "surface",
        border_radius = "20px 20px",
        size= "5",
        margin_top = Size.LARGE.value
            
        ),  
        width = "100%",
    )