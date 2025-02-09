import reflex as rx
import mena_cumples.components.pack_form as pack
from mena_cumples.states.form_state import FormBaseState


@rx.page(route="/pack_30_pax", title="Pack 30 personas")
def pack_30() -> rx.Component:
    return rx.container(
        rx.vstack(
            pack.pack_form(
                state=FormBaseState.select_pack("Pack_30"),
                image_url="/pack_30.jpeg",               
                pack_type="PACK DE 30 PERSONAS -- 180€",
                
                # Nombre y fecha del cumpleaños
                name_title="*¿Nombre del niño o niña del cumpleaños y edad?",
                date_time="*¿Fecha y hora del cumpleaños?",
                time_description="Tenga en cuenta que el máximo son 2 horas y media.",
                
                # Opciones de comida
                sandwiches_text="*¿Desea bocadillos, sandwiches o mitad bocadillos y mitad sandwiches?",
                food_options=current_food_options,
                pack_description="Los packs de cumpleaños incluyen patatas, palomitas, bollería/galletas y frutos secos.",
                tortilla_description="+ 2 TORTILLAS INCLUIDAS.",
                
                # Pizzas y roscas
                pizza_title="*¿De un total de 5 pizzas o 5 roscas a elegir, de qué le gustaría las pizzas o roscas?",
                pizza_description="(Ejemplo: también puede elegir 3 pizzas y 2 roscas... total de 5 unidades)",
                
                # Bebidas
                drink_title="¿De un total de 10 refrescos, qué le gustaría pedir?",
                drink_description="(Tenga en cuenta que los cafés, bebidas alcohólicas, etc., van aparte)", 
                
                # Extras
                extra_title="EXTRAS",
                extra_description="Pueden ser:- Pizzas o roscas a 6€ - Refrescos a 3,50€ - Plato de gominolas variadas a 2€ cada uno.",
                
                # Repostería
                bakery_title="REPOSTERÍA",
                bakery_options=current_bakery_options,
                
                # Observaciones
                observation_title="OBSERVACIONES",
                
                # Valores predeterminados
                child_name_value="",  
                birth_date_value="",  
                birth_time_value="",
                pizza_selected_value="",
                rosca_selected_value="",
                drink_selected_value="",
                extra_selected="",
                observation_selected_value="",  
            ),            
            rx.text(),
            rx.flex(  
                rx.button(
                    "ENVIAR",
                    rx.image(src = "/whatsapp_ico.ico", width ="20px", height = "20px"),
                    width="200px",                                    
                    align="center",
                    color_scheme="jade",
                    margin_bottom = "20px",
                    on_click = FormBaseState.send_whatsapp_message,
                ), 
                
                
                width="100%",
                margin_top="20px",
                justify="center",
                margin_bottom="40px"
            ),                        
                
            align="center",
            width="100%",         
        ),

        width="100%",
        align="center",
        bg="#ece5f5",
        on_mount=lambda: FormBaseState.select_pack("Pack_30")  # Llamar a select_pack al montar el componente        
    )

# opciones de radio button bocadillos
current_food_options = [
    "60 Bocadillos",
    "30 Sandwiches (60 mitades)",
    "Mitad bocadillos y mitad Sandwiches -- 30 y 15 uds."
]

# opciones de radio button tartas
current_bakery_options = [
    "Tarta de Galletas casera (natillas, chocolate y galletas)--15€--de 12 a 15 personas.",
    "Bizcocho ---10€-- de 8 a 10 personas.",
    "Tarta Panadería--personalizable a 18€ el kilo.",
    "Palmera gigante de Chocolate--25€.",
    "Palmera gigante de Chocolate y relleno de kinder--28€.",
    "LA TARTA LA TRAEMOS NOSOTROS."
]

def extra_description_component():
    return rx.flex(
        rx.text("Pizzas o roscas a 6€"),
        rx.text("Refrescos a 3,50€"),
        rx.text("Plato de gominolas variadas a 2€ cada uno"),
        direction="column",
        spacing="1"
    )