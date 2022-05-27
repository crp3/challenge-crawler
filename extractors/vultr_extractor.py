import requests

from typing import List
from bs4.element import Tag
from bs4 import BeautifulSoup

from models.vultr_machine import VultrMachine
from utils.tag_utils import extract_tag_content
from utils.text_utils import is_cpu, is_storage, remove_separators, replace_commas, concat_attribute_information

class VultrExtractor:
    def __init__(self, url: str):
        self.url: str = url
        self.file = None

    def _download(self) -> None:
        self.file = requests.get(self.url).content

    def _extract_price(self, item_div: Tag) -> str:
        price_headline = item_div.find('span')
        price_value = price_headline.find('b')
        price_message = price_headline.find('span')
            
        if price_value:
            return replace_commas(extract_tag_content(price_value))
        elif price_message:
            return extract_tag_content(price_message)
    
    def _extract_unordered_list(self, div_unordered_list: List[Tag]) -> List[str]:
        attributes = []
        for list_item in div_unordered_list.find_all('li'):
            attribute_value_list = []
            for content in list_item.contents:
                if type(content) == Tag:
                    attribute_value_list.append(extract_tag_content(content))
                else:
                    attribute_value_list.append(remove_separators(content))
            attribute_string = ''.join(attribute_value_list)
            attributes.append(attribute_string)
        
        return attributes

    def _create_machine(self, price: str, attributes: List[str]) -> VultrMachine:
        if len(attributes) == 6:
            if is_storage(attributes[1]):
                return VultrMachine(
                    price,
                    concat_attribute_information(attributes[0], attributes[1]),
                    *attributes[2:]
                )
            if is_cpu(attributes[1]):
                return VultrMachine(
                    price,
                    attributes[0],
                    concat_attribute_information(attributes[1], attributes[2])
                    *attributes[3:]
                )
        elif len(attributes) == 7:
            return VultrMachine(
                price,
                concat_attribute_information(attributes[0], attributes[1]),
                concat_attribute_information(attributes[2], attributes[3]),
                *attributes[4:]
            )
        else:
            return VultrMachine(
                price,
                *attributes
            )

    def extract(self) -> List[VultrMachine]:
        if self.file is None:
            self._download()
        
        parsed_file = BeautifulSoup(self.file, features='html5lib')
        machines = []
        for card_item in parsed_file.select("div[class=col-lg-3]"):
            unordered_list = card_item.find('ul')
            
            price = self._extract_price(card_item)
            attributes = self._extract_unordered_list(unordered_list)

            machines.append(self._create_machine(price, attributes))

        return machines
    