import unittest
from Preprocess import Preprocess

__author__ = 'marie-helene'

class TestCipher(unittest.TestCase):

    def test_preprocess(self):
        url = "https://www.gutenberg.org/cache/epub/28210/pg28210.txt"
        preprocess_machine = Preprocess(url)
        imported_text = preprocess_machine.import_text()
        self.assertEqual(imported_text[0], "T")

