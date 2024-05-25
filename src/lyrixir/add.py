from . import config
from . import fancy
from . import songs


def add_song(reference: str) -> None:
    song: songs.Song | None = songs.get_song(reference)

    if song:
        song.save()
        config.add_reference_list(reference)

        fancy.print_success(f"added {song.title} by {song.artist}")
    else:
        fancy.print_error(f"{reference} is unavailable")


def add_songs(references: list[str]) -> None:
    reference_list: list[str] = config.read_reference_list()

    for song_reference in references:
        if song_reference in reference_list:
            fancy.print_success(f"{song_reference} is already added")
        else:
            add_song(song_reference)


def main(arguments: list[str]) -> None:
    if arguments:
        song_references: list[str] = arguments[-1].split(',')

        add_songs(song_references)
    else:
        fancy.print_error("no song reference entered")
