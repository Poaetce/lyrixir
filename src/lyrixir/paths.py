import os
import platform

data: str
config: str

match platform.system():
    case 'Linux':
        data = '~/.local/share/lyrixir'
        config = '~/.config/lyrixir'
        
    case 'Windows':
        data = f'{os.getenv('APPDATA')}\\lyrixir-data'
        config = f'{os.getenv('APPDATA')}\\lyrixir'
