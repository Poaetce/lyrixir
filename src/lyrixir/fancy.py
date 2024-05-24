import enum
import os

RESET: str = '\x1b[0m'


class Alignment(enum.Enum):
    LEFT: int = 1
    CENTER: int = 2
    RIGHT: int = 3


class Color():
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


class Style():
    BOLD: int = 1
    ITALIC: int = 3
    UNDERLINE: int = 4
    STRIKETHROUGH: int = 9


def fancy_string(string: str, color: int, styles: list[int]) -> str:
    escape_code: str = f'\x1b[{color}{''.join(f';{style}' for style in styles)}m'

    return f'{escape_code}{string}{RESET}'


def fancy_print(
        string: str,
        alignment: Alignment = Alignment.LEFT,
        color: int = Color.BLACK,
        styles: list[int] = [],
    ) -> None:
    terminal_width: int = os.get_terminal_size().columns

    for line in string.splitlines():
        fancy_line: str = fancy_string(line, color, styles)

        match alignment:
            case Alignment.LEFT:
                print(f'{fancy_line : <{terminal_width}}')
            case Alignment.CENTER:
                print(f'{fancy_line : ^{terminal_width}}')
            case Alignment.RIGHT:
                print(f'{fancy_line : >{terminal_width}}')
