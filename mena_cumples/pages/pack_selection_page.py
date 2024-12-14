import reflex as rx
from mena_cumples.views.index_view.header.header import header
from mena_cumples.views.index_view.body.body import body
from mena_cumples.views.index_view.footer.footer import footer


rx.page(route="/pack_selection")
def pack_selection() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.vstack(
                header(),
                body(),
                footer(),
                width="100%",
            ),
            align="center",
            width="100%",
        ),
        bg="#EBE6EF",
        min_height="100vh",  # Asegura que el fondo ocupe al menos toda la altura de la ventana
        width="100vw",       # Asegura que el fondo ocupe toda la anchura de la ventana
        display="flex",      # Asegura que el contenido se centre verticalmente
        justify_content="center",  # Centra el contenido horizontalmente
        align_items="center",      # Centra el contenido verticalmente
    )