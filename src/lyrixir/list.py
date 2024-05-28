from . import config
from . import fancy
from . import songs


def print_song_information(reference: str) -> None:
    song: songs.Song | None = songs.open_song(reference)
    if song:
        fancy.print_neutral(f"{song.title} - {song.artist}")


def list_songs(references: list[str]) -> None:
    for reference in references:
        print_song_information(reference)


def main() -> None:
    references: list[str] = config.read_reference_list()

    list_songs(references)
