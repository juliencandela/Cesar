import requests
from cipher import cipher

__author__ = 'marie-helene'
from encoder import Encoder
from preprocess import Preprocess
from CipherAlbert import CeasarCipher


def preprocess_text(text):
    text = text.lower()
    # Remove all non letters
    text = ''.join(c for c in text if c.isalpha())
    # Replace accent character
    accent_to_ascii = {'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'ç': 'c', 'ù': 'u', 'ë': 'e', 'ö': 'o', 'ä': 'a', 'ï': 'i',
                       'ü': 'u'}
    new_text = ''
    for c in text:
        if c in accent_to_ascii:
            new_text += accent_to_ascii[c]
        else:
            new_text += c
    # Ignore all non ascii character at this point
    text = new_text.encode('ascii', 'ignore').decode('ascii')
    return text


key = "jesus"
url = "https://www.gutenberg.org/cache/epub/28210/pg28210.txt"
import_text = requests.get(url)
text = preprocess_text(import_text.text[500:200000])
encoded_text = cipher(text, key)


file = open("encoded_text_vigenere.txt", "w")
file.write(encoded_text)