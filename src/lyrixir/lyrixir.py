import sys


def main() -> None:
    arguments: list[str] = sys.argv[1:]
    if arguments:
        command: str = arguments[0]
        match command:
            case 'add': add()
            case 'remove': remove()
            case _: pass
    else:
        lyrixir()


def add() -> None:
    pass


def remove() -> None:
    pass


def lyrixir() -> None:
    pass
