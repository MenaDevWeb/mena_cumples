from enum import Enum

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "1em"
    MEDIUM = "2em"
    DEFAULT = "1em"
    LARGE = "3em"
    BIG = "2em"
    VERY_BIG = "4em"
    
    # diccionario para estilos
style = {
    "font_size": "17px",  # Usar el valor de la enumeración
}