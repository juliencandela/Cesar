__author__ = 'jenselme'

from string import ascii_letters

def cipher(text, key):
    cipher_text = ""
    alphabet = list(ascii_letters)
    for letter in text:
        if letter in ascii_letters:
            indice = alphabet.index(letter)
            cipher_text += alphabet[(indice + key) % len(alphabet)]
        else:
            cipher_text += letter
    return cipher_text.lower()