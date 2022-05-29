import requests

class Extractor:
    def __init__(self, url):
        self.url: str = url
        self.file = None

    def _download(self) -> None:
        self.file = requests.get(self.url).content
