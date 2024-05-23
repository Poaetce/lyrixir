class Song:
    def __init__(self, reference: str, artist: str, title: str, lyrics: str) -> None:
        self.reference: str = reference
        self.artist: str = artist
        self.title: str = title
        self.lyrics: str = lyrics

    def form(self) -> str:
        return f'{self.artist}\0{self.title}\0{self.lyrics}'

    def compress(self) -> bytes:
        import zlib

        return zlib.compress(self.form().encode())


def get_song(reference: str) -> Song | None:
    import requests
    import bs4

    url: str = f'https://www.azlyrics.com/lyrics/{reference}.html'

    response: requests.Response = requests.get(url)

    if response.status_code != 200:
        return None

    page: bs4.BeautifulSoup = bs4.BeautifulSoup(response.content, 'html.parser')

    lyrics: str = page.find('div', attrs = {'class': None, 'id': None}).get_text().strip()
    artist: str = page.find('b').get_text().rsplit(' ', 1)[0]
    title: str = page.find_all('b')[1].get_text().strip('"')

    return Song(reference, artist, title, lyrics)
