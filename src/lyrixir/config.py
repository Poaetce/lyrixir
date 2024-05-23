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
        'visible': ['artist', 'song',],
        'alignment': 'right',
        'variation': 'none',
    },
}

config_file = os.path.join(paths.config, 'lyrixir.toml')

if os.path.exists(config_file):
    with open(config_file, 'rb') as file:
        user_configuration: dict = tomllib.load(file)
        for table in user_configuration:
            configuration[table].update(user_configuration[table])
