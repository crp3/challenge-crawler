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

    '''
        This html page contains a pattern for pricing. 
        The price headline is a <span> tag and inside of it there is either a <b> tag or another <span> tag.
        This pattern gives us a tag-type separation ease, since if the price is a value, like $6000, it will be highlighted by a <b> tag.
        If it is a message, though, it will be inside a <span> tag, and hence it is just necessary to find a single one of this, since it doesn't contain any other tags alike.
    '''
    def _extract_price(self, item_div: Tag) -> str:
        price_headline = item_div.find('span')
        price_value = price_headline.find('b')
        price_message = price_headline.find('span')
            
        if price_value:
            return replace_commas(extract_tag_content(price_value))
        elif price_message:
            return extract_tag_content(price_message)
    
    '''
        To search for all the attributes of each card, like storage, cpu etc, it is necessary to fetch all of the <li> tags and extract its content.
        However, the content inside each item is a set of tags, which can be a simple string, or a text highlighted by a <b> tag. 
        So, to in order to extract it, it is necessary to process each of the item's content and append it to a list, to later concatenate on a string.
        Also, some of the items had separators, so a function to remove all the separator characters needed to be designed.
    '''
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

    '''
        This method is necessary to ensure all attributes contains the same type of information.
        The method above extracts the list's content and ensures it is a formatted string. 
        However, this list only contains a pattern for ordering (e.g. cpu comes after storage), but the quantity of items concerning each subject is not defined
        (e.g. you could have multiple lines about cpu).
        Hence, in order to define if an attribute is CPU or Storage (only two corner cases this page falls in), a couple of heuristic functions were created, [is_cpu, is_storage]
        Also, another corner case is that the card item contains seven attributes in the unordered_list, in that case, the first two attributes are storage-related and the second two are cpu-related
        Other than that, all other attributes fall on the same ordering and quantity as specified in the VultrMachine class model, so no extra processing is necessary. 
    '''
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

    '''
        The main function of this extractor consists on using a css selector to find the cards. 
        A CSS Selector is perfect when you want to be strict certain attributes on bs4.
        This was necessary because there is another <div> with the same class of the cards at the bottom of the page.
        This function does little than finding the unordered list and calling the specific function to extract the price, the other attributes and creating the machine object.
    '''
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
    