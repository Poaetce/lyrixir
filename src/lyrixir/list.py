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


def main(arguments: list[str]) -> None:
    references: list[str]

    if arguments:
        references = []
        for reference in config.read_reference_list():
            artist: str = reference.split('/')[0]
            if artist in arguments:
                references.append(reference)

    else:
        references = config.read_reference_list()

    list_songs(references)
