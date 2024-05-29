import random

from . import config
from . import fancy
from . import songs


def print_section(section: str, content: str) -> None:
    fancy.prepare_print(
        config.configuration[section]['alignment'],
        config.configuration[section]['color'],
        config.configuration[section]['styles'],
    )(content)


def print_song(song: songs.Song) -> None:
    chunks: str

    match config.configuration['lyrics']['scale']:
        case 'line':
            chunks = [line for line in song.lyrics.splitlines() if line]
        case 'stanza':
            chunks = song.lyrics.split('/n/n')
        case 'song':
            chunks = [song.lyrics]

    lyrics: str = random.choice(chunks)
    print_section('lyrics', lyrics)

    for element in config.configuration['info']['visible']:
        information: str
        match element:
            case 'artist': information = song.artist
            case 'title': information = song.title

        print_section('info', information)


def pick_song() -> songs.Song | None:
    reference_list: list[str] = config.read_reference_list()

    random_reference: str = random.choice(reference_list)

    return songs.open_song(random_reference)


def main() -> None:
    song: song.Song | None = pick_song()

    while not song:
        song = pick_song()

    print_song(song)
