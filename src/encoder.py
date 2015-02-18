import string

__author__ = 'marie-helene'

class Encoder :

    def __init__(self, key=0):
        self.key = key
        self.alphabet = list(string.ascii_uppercase)

    def cipher(self, text):
        cipher_text = ""
        for letter in text:
            indice = self.alphabet.index(letter)
            cipher_text += self.alphabet[indice+self.key % len(self.alphabet)]
        return cipher_text
