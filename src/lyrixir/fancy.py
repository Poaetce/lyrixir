import enum

RESET: str = '\x1b[0m' 


class Alignment(enum.Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3


class Color(enum.Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    LIGHT_GRAY = 37
    DEFAULT = 39
    DARK_GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96


class Style(enum.Enum):
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    STRIKETHROUGH = 9
