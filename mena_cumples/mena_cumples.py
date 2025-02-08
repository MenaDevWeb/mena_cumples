
import reflex as rx

from .pages.main_page import create_main_screen
from .pages.contact_form_page import create_page_layout
from .pages.pack_selection_page import pack_selection
from .pages.pack_15_page import pack_15
from .pages.pack_20_page import pack_20
from .pages.pack_25_page import pack_25
from .pages.pack_30_page import pack_30
from .pages.packs_information_page import packs_information
from .styles.styles import style



@rx.page(route="/", title="Cumpleaños Mena Plaza")
def index() -> rx.Component:
    return rx.fragment(
        create_main_screen()
    )  


app = rx.App(style=style)
app.add_page(index)
app.add_page(create_main_screen)
app.add_page(create_page_layout,route="/contact_form_page")
app.add_page(pack_selection, route="/pack_selection" )
app.add_page(packs_information, route="/pack_information")
app.add_page(pack_15, route="/pack_15_pax")
app.add_page(pack_20, route="/pack_20_pax")
app.add_page(pack_25, route="/pack_25_pax")
app.add_page(pack_30, route="/pack_30_pax")

