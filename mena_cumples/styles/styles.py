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
    # Sombras suaves con múltiples capas para profundidad moderno
    CARD = "0 2px 4px rgba(124, 58, 237, 0.06), 0 8px 16px rgba(124, 58, 237, 0.08)"
    CARD_HOVER = "0 4px 8px rgba(124, 58, 237, 0.10), 0 16px 32px rgba(124, 58, 237, 0.14)"
    FORM = "0 10px 15px -3px rgba(124, 58, 237, 0.1), 0 4px 6px -2px rgba(190, 24, 93, 0.05)"
    NAVBAR = "0 1px 3px rgba(124, 58, 237, 0.08), 0 1px 2px rgba(190, 24, 93, 0.04)"
    SOFT = "0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -1px rgba(0, 0, 0, 0.04)"
    GLOW_PINK = "0 0 20px rgba(249, 168, 212, 0.5)"
    GLOW_PURPLE = "0 0 20px rgba(167, 139, 250, 0.5)"
    # Mantener compatibilidad con usos antiguos
    # (card/form se redefinen arriba)

class Transition:
    DEFAULT = "background-color 300ms ease-in-out"
    FAST = "all 150ms ease-in-out"
    SMOOTH = "all 350ms cubic-bezier(0.4, 0, 0.2, 1)"
    INPUT = "background-color, border-color, color, fill, stroke, opacity, box-shadow, transform"
    INPUT_TIMING = "cubic-bezier(0.4, 0, 0.2, 1)"
    SHADOW = "box-shadow 0.3s ease-in-out"
    CARD = "transform 300ms cubic-bezier(0.4, 0, 0.2, 1), box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)"

# Estilos globales modernizados
style = {
    # Fallback global (html 16px se fija via rx.el.style en mena_cumples.py para evitar nesting incorrecto)
    "font_family": "Inter, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
    # Animaciones globales inyectadas como CSS
    "@keyframes fadeInUp": {
        "from": {"opacity": "0", "transform": "translateY(20px)"},
        "to": {"opacity": "1", "transform": "translateY(0)"},
    },
    "@keyframes fadeIn": {
        "from": {"opacity": "0"},
        "to": {"opacity": "1"},
    },
    "@keyframes scaleIn": {
        "from": {"opacity": "0", "transform": "scale(0.95)"},
        "to": {"opacity": "1", "transform": "scale(1)"},
    },
    "@keyframes floatY": {
        "0%, 100%": {"transform": "translateY(0)"},
        "50%": {"transform": "translateY(-6px)"},
    },
    # Clases utilitarias para animaciones
    ".fade-in-up": {
        "animation": "fadeInUp 0.6s ease-out forwards",
    },
    ".fade-in": {
        "animation": "fadeIn 0.5s ease-out forwards",
    },
    ".scale-in": {
        "animation": "scaleIn 0.4s ease-out forwards",
    },
    ".card-hover": {
        "transition": "transform 300ms cubic-bezier(0.4, 0, 0.2, 1), box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)",
    },
    ".card-hover:hover": {
        "transform": "translateY(-4px)",
        "box_shadow": "0 4px 8px rgba(124, 58, 237, 0.10), 0 16px 32px rgba(124, 58, 237, 0.14)",
    },
    # Scrollbar moderno
    "::webkit-scrollbar": {
        "width": "8px",
    },
    "::webkit-scrollbar-track": {
        "background": "#FDF2F8",
    },
    "::webkit-scrollbar-thumb": {
        "background": "#D8B4FE",
        "border_radius": "9999px",
    },
    "::webkit-scrollbar-thumb:hover": {
        "background": "#A78BFA",
    },
}
