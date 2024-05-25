import sys

from . import fancy
from . import song
from . import config


def main() -> None:
    arguments: list[str] = sys.argv[1:]
    if arguments:
        command: str = arguments[0]
        match command:
            case 'add': add(arguments[1:])
            case 'remove': remove()
            case _: pass
    else:
        lyrixir()


def add(arguments: list[str]) -> None:
    if arguments:
        song_references: list[str] = arguments[-1].split(',')

        for song_reference in song_references:
            reference_list: list[str] = config.read_reference_list()

            if song_reference in reference_list:
                fancy.print_success(f"{song_reference} is already added")
            else:
                current_song: song.Song | None = song.get_song(song_reference)

                if current_song:
                    current_song.save()
                    config.add_reference_list(song_reference)

                    fancy.print_success(f"added {current_song.title} by {current_song.artist}")
                else:
                    fancy.print_error(f"{song_reference} is unavailable")

    else:
        fancy.print_error("no song reference entered")


def remove() -> None:
    pass


def lyrixir() -> None:
    pass
