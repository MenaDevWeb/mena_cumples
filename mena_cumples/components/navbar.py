import reflex as rx

def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(      
            rx.image(
                src="/favicon.ico", 
                width="100px", 
                height="100%", 
                padding="20px",
                align="center"   
            ), 
            rx.heading(
                "CUMPLEAÑOS MENA PLAZA",
                height="auto",
                size="8",
                padding="10px",
                box_sizing="border-box",  
                align="center"
            ),
            align="center"
        ),
        width="100%",
        bg = "#DAD0E7", 
        justify_content="center", 
        align_items="center",
        align="center"
    )