from enum import Enum

class Size(Enum):
    ZERO = "0px !important"
    XS = "0.5rem"
    SMALL = "1rem"
    DEFAULT = "1.5rem"
    MEDIUM = "2rem"
    LARGE = "3rem"
    XL = "4rem"
    XXL = "6rem"

class Color:
    PURPLE = "#7C3AED"
    PURPLE_LIGHT = "#8B5CF6"
    PURPLE_DARK = "#6D28D9"
    PURPLE_BG = "#A78BFA"
    PURPLE_RING = "#DDD6FE"
    PURPLE_RING_ALT = "#C4B5FD"

    PINK = "#BE185D"
    PINK_LIGHT = "#F9A8D4"
    PINK_BG = "#FDF2F8"

    PAGE_BG = "#EBE6EF"
    PAGE_BG_ALT = "#ece5f5"

    CARD_PINK = "#f5cade"
    CARD_PURPLE = "#dcd4ee"
    CARD_EXTRAS = "#fce7f3"
    CARD_EXTRAS_TOGGLE = "#fef3c7"
    CARD_PACK_INFO = "#e2d5f4"

    WHITE = "#ffffff"
    BLACK = "#000000"
    GRAY_TEXT = "#9CA3AF"
    GRAY_DISABLED = "#f0f0f0"
    GRAY_BORDER = "#d1d5db"
    WARNING = "#f59e0b"
    ERROR = "#dc2626"
    ERROR_BG = "#fef2f2"
    ORANGE = "#f97316"
    BG_OVERLAY = "rgba(0, 0, 0, 0.75)"

    GRADIENT_NAVBAR = "bg-gradient-to-r from-pink-200 to-pink-300 via-purple-200"
    GRADIENT_FORM = "bg-gradient-to-br from-pink-100 to-purple-100"

class FontSize:
    XS = "0.75rem"
    SMALL = "0.875rem"
    DEFAULT = "1rem"
    LARGE = "1.25rem"
    XL = "1.5rem"
    XXL = "1.875rem"
    XXXL = "2.25rem"
    TITLE = "3rem"
    INPUT = "16px"

class BorderRadius:
    SMALL = "0.5rem"
    MEDIUM = "1rem"
    CARD = "15px"
    FULL = "9999px"

class Shadow:
    CARD = "0px 4px 6px rgba(0, 0, 0, 0.1)"
    FORM = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"

class Transition:
    DEFAULT = "background-color 300ms ease-in-out"
    FAST = "all 150ms ease-in-out"
    INPUT = "background-color, border-color, color, fill, stroke, opacity, box-shadow, transform"
    INPUT_TIMING = "cubic-bezier(0.4, 0, 0.2, 1)"
    SHADOW = "box-shadow 0.3s ease-in-out"

style = {}
