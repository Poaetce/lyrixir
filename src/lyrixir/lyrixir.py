import sys


def main() -> None:
    arguments: list[str] = sys.argv[1:]
    if arguments:
        command: str = arguments[0]
        match command:
            case 'add': pass
            case 'remove': pass
            case _: pass
    else:
        pass
