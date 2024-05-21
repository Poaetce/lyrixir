class Song:
    def __init__(self, artist: str, song: str, lyrics: str) -> None:
        self.artist: str = artist
        self.song: str = song
        self.lyrics: str = lyrics


def get_song(reference: str) -> Song | None:
    import requests
    import bs4

    url: str = f'https://www.azlyrics.com/lyrics/{reference}.html'
    
    response: requests.Response = requests.get(url)

    if response.status_code != 200:
        return

    page: bs4.BeautifulSoup = bs4.BeautifulSoup(response.content, 'html.parser')

    lyrics: str = page.find('div', attrs = {'class': None, 'id': None}).get_text().strip()
    artist: str = page.find('b').get_text().rsplit(' ', 1)[0]
    song: str = page.find_all('b')[1].get_text().strip('"')

    return Song(artist, song, lyrics)
