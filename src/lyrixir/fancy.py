import enum

RESET: str = '\x1b[0m' 


class Alignment(enum.Enum):
    LEFT: int = 1
    CENTER: int = 2
    RIGHT: int = 3


class Color(enum.Enum):
    BLACK: int = 30
    RED: int = 31
    GREEN: int = 32
    YELLOW: int = 33
    BLUE: int = 34
    MAGENTA: int = 35
    CYAN: int = 36
    LIGHT_GRAY: int = 37
    DEFAULT: int = 39
    DARK_GRAY: int = 90
    LIGHT_RED: int = 91
    LIGHT_GREEN: int = 92
    LIGHT_YELLOW: int = 93
    LIGHT_BLUE: int = 94
    LIGHT_MAGENTA: int = 95
    LIGHT_CYAN: int = 96


class Style(enum.Enum):
    BOLD: int = 1
    ITALIC: int = 3
    UNDERLINE: int = 4
    STRIKETHROUGH: int = 9
