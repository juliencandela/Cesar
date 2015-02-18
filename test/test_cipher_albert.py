import unittest
from CipherAlbert import CeasarCipher


__author__ = 'julien'


class TestCipher(unittest.TestCase):

    def test_cipher_simple_letter(self):
        encoder = CeasarCipher()
        text = "a"
        encoding_text = encoder.encrypt(text, 27)
        self.assertEqual(encoding_text, "b")

    def test_cipher_special_characters(self):
        encoder = CeasarCipher()
        text = "aÉb"
        encoding_text = encoder.encrypt(text, 1)
        self.assertEqual(encoding_text, "bÉc")

