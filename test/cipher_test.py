import unittest
from encoder import Encoder
from cipher import cipher

__author__ = 'julien'


class TestCipher(unittest.TestCase):

    def test_cipher_simple_letter(self):
        encoder = Encoder(27)
        text = "a"
        encoding_text = encoder.cipher(text)
        self.assertEqual(encoding_text, "b")

    def test_cipher_special_characters(self):
        encoder = Encoder(1)
        text = "aÉb"
        encoding_text = encoder.cipher(text)
        self.assertEqual(encoding_text, "bÉc")

    def test_cipher_cipher(self):
        text = "a"
        encoded_text = cipher(text, 27)
        self.assertEqual(encoded_text, "b")