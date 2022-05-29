import unittest

from models.vultr_machine import VultrMachine
from extractors.vultr_extractor import VultrExtractor

class TestVultrExtractor(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.extractor = VultrExtractor('')
    
    def test_extract(cls):
        with open('test/extractors/vultr_page.html', 'r') as vultr_file:
            cls.extractor.file = vultr_file
            machines = cls.extractor.extract()
            for machine in machines:
                cls.assertEqual(type(machine), VultrMachine)
