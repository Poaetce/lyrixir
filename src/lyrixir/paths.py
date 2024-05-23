import os
import platform

data: str
config: str

match platform.system():
    case 'Linux':
        data = f'{os.getenv('HOME')}/.local/share/lyrixir'
        config = f'{os.getenv('HOME')}/.config/lyrixir'

    case 'Windows':
        data = f'{os.getenv('APPDATA')}\\lyrixir-data'
        config = f'{os.getenv('APPDATA')}\\lyrixir'
