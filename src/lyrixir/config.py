import os
import tomllib

from . import paths


config_file_name = os.path.join(paths.config, 'lyrixir.toml')

configuration: dict = {
    'lyrics': {
        'scale': 'line',
        'alignment': 'center',
        'variation': 'bold',
    },
    'info': {
        'visible': ['artist', 'song'],
        'alignment': 'right',
        'variation': 'none',
    },
}

if os.path.exists(config_file_name):
    with open(config_file_name, 'rb') as file:
        user_configuration: dict = tomllib.load(file)
        for table in user_configuration:
            configuration[table].update(user_configuration[table])


list_file_name = os.path.join(paths.config, 'reference.list')


def read_reference_list() -> list[str]:
    if os.path.exists(list_file_name):
        with open(list_file_name, 'r') as file:
            return file.read().splitlines()
    else:
        return []


def add_reference_list(reference: str) -> None:
    os.makedirs(os.path.dirname(list_file_name), exist_ok = True)
    with open(list_file_name, 'a') as file:
        file.write(f'{reference}\n')
