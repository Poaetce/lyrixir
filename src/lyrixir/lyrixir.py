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
            current_song: song.Song | None = song.get_song(song_reference)

            if current_song:
                current_song.save()
                config.add_reference_list(song_reference)

                fancy.fancy_print(
                    f"saved {current_song.title} by {current_song.artist}",
                    color = fancy.Color.GREEN,
                    styles = [fancy.Style.BOLD],
                )
            else:
                fancy.fancy_print(
                    f"reference {song_reference} unavailable",
                    color = fancy.Color.RED,
                    styles = [fancy.Style.BOLD],
                )

    else:
        fancy.fancy_print(
            "no song reference entered",
            color = fancy.Color.RED,
            styles = [fancy.Style.BOLD],
        )


def remove() -> None:
    pass


def lyrixir() -> None:
    pass
