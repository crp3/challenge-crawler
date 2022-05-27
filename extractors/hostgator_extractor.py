import requests

from bs4 import BeautifulSoup

class HostgatorExtractor:
    def __init__(self, url: str):
        self.url = url
        self.file = None

    def _download(self) -> None:
        self.file = requests.get(self.url).content

    def extract(self):
        if self.file is None:
            self._download()

        parsed_file = BeautifulSoup(self.file, features='html5lib')
        print(parsed_file)
