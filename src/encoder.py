import string

__author__ = 'marie-helene'

class Encoder:

    def __init__(self, key=""):
        self.key = key
        self.alphabet = list(string.ascii_lowercase)

    def cipher(self, text):
        cipher_text = ""
        for indice in range(len(text)):
            letter = text[indice]
            if letter in self.alphabet:
                indice_in_alphabet = self.alphabet.index(letter)
                letter_in_key = self.key[indice % len(self.key)]
                cipher_text += self.alphabet[indice_in_alphabet + self.alphabet.index(letter_in_key)]
            else:
                cipher_text += letter
        return cipher_text



