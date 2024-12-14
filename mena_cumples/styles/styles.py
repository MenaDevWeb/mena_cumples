from enum import Enum

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    
    # diccionario para estilos
style = {
    "font_size": "17px",  # Usar el valor de la enumeración
}