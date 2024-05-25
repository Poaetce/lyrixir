from . import config
from . import fancy
from . import song


def main(arguments: list[str]) -> None:
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
