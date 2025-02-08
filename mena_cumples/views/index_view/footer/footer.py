import reflex as rx
from mena_cumples.styles.styles import Size

def footer() -> rx.Component:

    return rx.flex(
            rx.hstack(            
                rx.text(
                    "© Developed by Gabriel Visiedo with ",
                    align="center",
                    size="2"
                    
                ),                                 
                rx.image(
                        src="https://reflex.dev/logos/light/reflex.svg",
                        height="10px",
                        on_click=
                            rx.redirect(
                                "https://reflex.dev/",is_external=True
                            ),                
                    ),
            align="center"
            
            ),
        width = "100%",
        align= "center",
        margin_top = Size.VERY_BIG.value,
        margin_bottom="12px",
        justify_content = "center"      
        
    )