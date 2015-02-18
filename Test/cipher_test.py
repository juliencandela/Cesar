import unittest
from encoder import Encoder


__author__ = 'julien'


class TestCipher(unittest.TestCase):

    def test_cipher_simple_letter(self):
        encoder = Encoder(1)
        text = "A"
        encoding_text = encoder.cipher(text)
        self.assertEqual(encoding_text, "B")

    def test_cipher_space(self):
        encoder = Encoder(1)
        text = "A B"
        encoding_text = encoder.cipher(text)
        self.assertEqual(encoding_text, "B C")