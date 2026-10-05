import reflex as rx
import mena_cumples.components.pack_form as pack
from mena_cumples.states.form_state import FormBaseState
from mena_cumples.components.navbar import navbar, mobile_drawer
from mena_cumples.components.footer import footer
from ..routes import Routes


@rx.page(route=Routes.PACK_MEDIODOIA.value, title="Pack Mediodía — 5,90€/niño")
def pack_mediodia() -> rx.Component:
    return rx.box(
        navbar(),
        mobile_drawer(),
        rx.container(
            rx.vstack(
            pack.pack_form_mediodia(
                image_url="/packs_image.webp",
                pack_description="Pack Mediodía — 5,90€ por niño",
                name_title="*¿Nombre del niño o niña del cumpleaños y edad?",
                date_time="*¿Fecha y hora del cumpleaños?",
                time_description="Horario Mediodía. Máximo 2 horas y media de celebración.",
                bakery_title="REPOSTERÍA",
                bakery_options=current_bakery_options,
                observation_title="OBSERVACIONES",
            ),
        ),
        on_mount=lambda: FormBaseState.init_pack_page("Pack_Mediodia"),
        padding_y="1.5rem",
        ),
        footer(),
        background_color="#FFF7FB",
        min_height="100vh",
        display="flex",
        flex_direction="column",
    )


current_bakery_options = [
    "Tarta de Galletas casera (natillas, chocolate y galletas)--15€--de 12 a 15 personas.",
    "Bizcocho ---10€-- de 8 a 10 personas.",
    "Tarta Panadería--personalizable a 18€ el kilo.",
    "Palmera gigante de Chocolate--25€.",
    "Palmera gigante de Chocolate y relleno de kinder--28€.",
    "LA TARTA LA TRAEMOS NOSOTROS.",
]
