import reflex as rx
import mena_cumples.components.pack_form as pack
from mena_cumples.states.form_state import FormBaseState
from ..routes import Routes


@rx.page(route=Routes.PACK_15_PAX.value, title="Pack 15 personas")
def pack_15() -> rx.Component:
    return rx.container(
        rx.vstack(
            pack.pack_form(
                pack_type="PACK DE 15 PERSONAS--90€",
                image_url="/pack_15_image.webp",
                name_title="*¿Nombre del niño o niña del cumpleaños y edad?",
                date_time="*¿Fecha y hora del cumpleaños?",
                time_description="Tenga en cuenta que el máximo son 2 horas y media.",
                sandwiches_text="*¿Desea bocadillos, sandwiches o mitad bocadillos y mitad sandwiches?",
                food_options=current_food_options,
                pack_description="Los packs de cumpleaños incluyen patatas, palomitas, bollería/galletas y frutos secos.",
                pizza_title="*¿De un total de 3 pizzas o 3 roscas a elegir, de que le gustaría las pizzas o roscas?",
                pizza_description="( ej: también puede elegir 2 pizza y 1 rosca...total de tres unidades)",
                drink_title="¿De un total de 4 refrescos que le gustaría pedir? ",
                drink_description="(tenga en cuenta que los cafés, bebidas alcohólicas etc. van aparte) ",
                extra_title="EXTRAS",
                extra_description="Pueden ser: Pizzas o roscas a 6€ , refrescos a 3,50€ y Platos de Chuches a 2 €",
                bakery_title="REPOSTERÍA",
                bakery_options=current_bakery_options,
                observation_title="OBSERVACIONES",
                child_name_value="",  
                birth_date_value="",  
                birth_time_value="",
                pizza_selected_value="",
                rosca_selected_value="",
                drink_selected_value="",
                extra_selected="",
                observation_selected_value="",             
            ),                               
        ),
        bg="#ece5f5",
        on_mount=lambda: FormBaseState.select_pack("Pack_15")  # Llamar a select_pack al montar el componente
    )

# opciones de radio button bocadillos
current_food_options = [
    "30 Bocadillos",
    "15 Sandwiches (30 mitades)",
    "Mitad bocadillos y mitad Sandwiches -- 15 y 8 uds."
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