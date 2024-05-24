import os
import tomllib

from . import paths

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

file_name = os.path.join(paths.config, 'lyrixir.toml')

if os.path.exists(file_name):
    with open(file_name, 'rb') as file:
        user_configuration: dict = tomllib.load(file)
        for table in user_configuration:
            configuration[table].update(user_configuration[table])
