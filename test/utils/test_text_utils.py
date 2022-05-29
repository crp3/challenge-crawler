import unittest

from utils.text_utils import concat_attribute_information, is_cpu, is_storage, multiple_replace, remove_separators, replace_commas

class TestTextUtils(unittest.TestCase):
    def test_multiple_replace(self):
        mapper = {
            'a': 'b',
            'c': 'd'
        }
        text = 'a c a c'
        expected = 'b d b d'

        assert expected == multiple_replace(mapper, text)
    
    def test_remove_separators(self):
        text = '\n aaa \t'
        expected = ' aaa '
        assert expected == remove_separators(text)

    def test_concat_attribute_information(self):
        attribute_one = 'foo'
        attribute_two = 'bar'
        expected = 'foo + bar'
        assert expected == concat_attribute_information(attribute_one, attribute_two)

    def test_replace_commas(self):
        text = 'a,b,c'
        expected = 'a.b.c'
        assert expected == replace_commas(text)

    def test_is_cpu_true(self):
        assert is_cpu('any string with Intel')

    def test_is_cpu_false(self):
        assert not is_cpu('any string without it')
    
    def test_is_storage_true(self):
        assert is_storage('Some TB')

    def test_is_storage_false(self):
        assert not is_storage('None')
