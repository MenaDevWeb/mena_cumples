import reflex as rx
from enum import Enum

class Routes(Enum):
    INDEX = "/"
    PACKS_INFORMATION = "/packs_information"
    PACK_SELECTION = "/pack_selection"
    PACK_15_PAX = "/pack_15_pax"
    PACK_20_PAX = "/pack_20_pax"
    PACK_25_PAX = "/pack_25_pax"
    PACK_30_PAX = "/pack_30_pax"
    CONTACT_FORM_PAGE = "/contact_form_page"