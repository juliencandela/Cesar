import unittest
from encoder import Encoder


__author__ = 'julien'


class TestCipher(unittest.TestCase):

    def test_cipher(self):
        encoder = Encoder(1)
        text = "A"
        encoding_text = encoder.cipher(text)
        self.assertEqual(encoding_text, "B")