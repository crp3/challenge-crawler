import requests
from bs4 import BeautifulSoup

class VultrExtractor:
    def __init__(self, url):
        self.url: str = url
        self.file = None

    def _download(self):
        self.file = requests.get(self.url).content

    def extract(self):
        if self.file is None:
            self._download()
        
        parsed_file = BeautifulSoup(self.file)
        print(parsed_file.prettify())
