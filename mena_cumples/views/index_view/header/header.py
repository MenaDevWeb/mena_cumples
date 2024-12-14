import reflex as rx
from mena_cumples.styles.styles import Size


def header() -> rx.Component:
    
    return rx.flex(  
        rx.vstack(
            rx.image(
                src="/birth.png", 
                width="300px", 
                height="auto",
                align="center",
                margin_top="20px"
            ),        
        ),
        align= "center",
        width = "100%",
        justify_content="center"    
    )