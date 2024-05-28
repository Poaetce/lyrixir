import sys


def main() -> None:
    arguments: list[str] = sys.argv[1:]
    if arguments:
        command: str = arguments[0]
        match command:
            case 'add':
                from . import lyrixir_add
                lyrixir_add.main(arguments[1:])

            case 'list':
                from . import lyrixir_list
                lyrixir_list.main(arguments[1:])

            case 'remove':
                pass

            case _:
                pass

    else:
        from . import lyrixir
        lyrixir.main()


if __name__ == '__main__':
    main()
