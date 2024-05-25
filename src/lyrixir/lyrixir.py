import sys

from . import add


def main() -> None:
    arguments: list[str] = sys.argv[1:]
    if arguments:
        command: str = arguments[0]
        match command:
            case 'add': add.main(arguments[1:])
            case 'remove': pass
            case _: pass
    else:
        pass
