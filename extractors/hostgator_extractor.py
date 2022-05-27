import requests
from typing import List
from bs4 import BeautifulSoup, Tag

from models.hostgator_machine import HostgatorMachine

class HostgatorExtractor:
    def __init__(self, url: str):
        self.url = url
        self.file = None

    def _download(self) -> None:
        self.file = requests.get(self.url).content

    def _extract_attributes(self, card_item: Tag) -> List[str]:
        unordered_list = card_item.find('ul')
        attributes = []
        for item in unordered_list.find_all('li'):
            attributes.append(item.contents[0])
        return attributes

    def _extract_price(self, card_item: Tag) -> List[str]:
        price_tag = card_item.find('p', {'class': 'pricing-card-price'})
        return ''.join([content for content in price_tag.contents if content not in [' ', '*']])

    def _create_machine(self, price: str, attributes: List[str]) -> HostgatorMachine:
        return HostgatorMachine(
            *attributes,
            price
        )

    def extract(self) -> List[HostgatorMachine]:
        if self.file is None:
            self._download()

        parsed_file = BeautifulSoup(self.file, features='html5lib')
        machines = []
        for card_item in parsed_file.find_all('div', {'class': 'pricing-card'}):
            attributes = self._extract_attributes(card_item)
            price = self._extract_price(card_item)
            machines.append(self._create_machine(price, attributes))
        
        return machines
