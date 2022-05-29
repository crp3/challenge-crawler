import requests
from typing import List
from bs4 import BeautifulSoup, Tag

from utils.tag_utils import extract_tag_content
from models.hostgator_machine import HostgatorMachine

class HostgatorExtractor:
    def __init__(self, url: str):
        self.url = url
        self.file = None

    def _download(self) -> None:
        self.file = requests.get(self.url).content

    '''
        This method receives the tag containing all the card information, extracts the <ul> tag,
        and, in a straight-forward fashion, extracts all the tag content inside the <li> tags.
    '''
    def _extract_attributes(self, card_item: Tag) -> List[str]:
        unordered_list = card_item.find('ul')
        attributes = []
        for list_item in unordered_list.find_all('li'):
            attributes.append(extract_tag_content(list_item))
        return attributes
    '''
        This function finds the pricing inside the card_item. 
        Since the contents of the Tag are an array-like structure, containing also undesired characters,
        It is necessary to filter the content in case it falls on those undesired characters. 
        The result is a simple string-array join, in order to avoid string concatenation and unnecessary complexity
    '''
    def _extract_price(self, card_item: Tag) -> List[str]:
        price_tag = card_item.find('p', {'class': 'pricing-card-price'})
        return ''.join([content for content in price_tag.contents if content not in [' ', '*']])

    '''
        This function just encapsulates the creation of the machine object.
    '''
    def _create_machine(self, price: str, attributes: List[str]) -> HostgatorMachine:
        return HostgatorMachine(
            *attributes,
            price
        )

    '''
        This method extracts all the <div> tags with 'class' equal to 'pricing-card'.
        This strictly selects the cards it is intended to, so no so other filter is necessary.
        For each card, the function extracts the price and attributes by calling those functions separately.
    '''
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
