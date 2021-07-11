import unittest
from searchbook import search_book


class Testsearchbook(unittest.TestCase):
    def test_typestr(self):
        result = search_book('ola')
        self.assertTrue(result, 'str')

    def test_typenumber(self):
        result = search_book(1313)
        self.assertTrue(result, 'number')
        
    def test_typesequence(self):
        result = search_book([13,13])
        self.assertTrue(result, 'sequence')

if __name__ == '__main__':
    unittest.main(verbosity=2)