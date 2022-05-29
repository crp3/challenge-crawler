import unittest

from models.hostgator_machine import HostgatorMachine
from extractors.hostgator_extractor import HostgatorExtractor

class TestHostgatorExtractor(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.extractor = HostgatorExtractor('')

    def test_extract(cls):
        with open('test/extractors/hostgator_page.html', 'r') as vultr_file:
            cls.extractor.file = vultr_file
            machines = cls.extractor.extract()
            for machine in machines:
                cls.assertEqual(type(machine), HostgatorMachine)
