__author__ = 'jenselme'

class CeasarCipher:
    def __init__(self):
        self.alphabet = list("abcdefghijklmnopqrstuvwxyz")
        self.taille_alphabet = len(self.alphabet)

    def encrypt(self, text, cle):
        text_crypte = ""
        for letter in text:
            if self.alphabet.__contains__(letter):
                text_crypte += self._decalage_lettre(letter, cle)
            else:
                text_crypte += letter
        return text_crypte

    def _decalage_lettre(self, lettre, decalage):
        index = self.alphabet.index(lettre)
        index_decale = (index + decalage) % self.taille_alphabet
        return self.alphabet[index_decale]