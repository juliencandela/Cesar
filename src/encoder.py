import string

__author__ = 'marie-helene'

class Encoder:

    def __init__(self, key=0):
        self.key = key
        self.alphabet = list(string.ascii_lowercase)

    def cipher(self, text):
        cipher_text = ""
        for letter in text:
            if letter in self.alphabet:
                indice = self.alphabet.index(letter)
                cipher_text += self.alphabet[indice+self.key % len(self.alphabet)]
            else:
                cipher_text += letter
        return cipher_text
