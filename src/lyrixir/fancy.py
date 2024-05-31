import os
import functools

RESET: str = '\x1b[0m'


class Alignment():
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
        alignment: int = Alignment.LEFT,
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


def prepare_print(alignment: str, color: str, styles: list[str]) -> functools.partial:
    print_alignment: int = Alignment.LEFT
    match alignment:
        case 'left': print_alignment = Alignment.LEFT
        case 'center': print_alignment = Alignment.CENTER
        case 'right': print_alignment = Alignment.RIGHT

    print_color: int = Color.BLACK
    match color:
        case 'black': print_color = Color.BLACK
        case 'red': print_color = Color.RED
        case 'green': print_color = Color.GREEN
        case 'yellow': print_color = Color.YELLOW
        case 'blue': print_color = Color.BLUE
        case 'magenta': print_color = Color.MAGENTA
        case 'cyan': print_color = Color.CYAN
        case 'light gray': print_color = Color.LIGHT_GRAY
        case 'default': print_color = Color.DEFAULT
        case 'dark gray': print_color = Color.DARK_GRAY
        case 'light red': print_color = Color.LIGHT_RED
        case 'light green': print_color = Color.LIGHT_GREEN
        case 'light yellow': print_color = Color.LIGHT_YELLOW
        case 'light blue': print_color = Color.LIGHT_BLUE
        case 'light magenta': print_color = Color.LIGHT_MAGENTA
        case 'light cyan': print_color = Color.LIGHT_CYAN

    print_styles: list[int] = []
    for style in styles:
        match style:
            case 'bold': print_styles.append(Style.BOLD)
            case 'italic': print_styles.append(Style.ITALIC)
            case 'underline': print_styles.append(Style.UNDERLINE)
            case 'strikethrough': print_styles.append(Style.STRIKETHROUGH)

    return functools.partial(
        fancy_print,
        alignment = print_alignment,
        color = print_color,
        styles = print_styles,
    )


print_error: functools.partial = functools.partial(
    fancy_print,
    color = Color.RED,
    styles = [Style.BOLD],
)
print_success: functools.partial = functools.partial(
    fancy_print,
    color = Color.GREEN,
    styles = [Style.BOLD],
)
print_neutral: functools.partial = functools.partial(
    fancy_print,
    color = Color.BLACK,
    styles = [Style.BOLD],
)
