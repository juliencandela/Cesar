__author__ = 'jenselme'

from string import ascii_letters

def cipher(text, key):
    cipher_text = ""
    alphabet = list(ascii_letters)
    for indice in range(len(text)):
        letter = text[indice]
        if letter in ascii_letters:
            indice_in_alphabet = alphabet.index(letter)
            letter_in_key = key[indice % len(key)]
            cipher_text += alphabet[indice_in_alphabet + alphabet.index(letter_in_key)]
        else:
            cipher_text += letter
    return cipher_text.lower()