import requests
from cipher import cipher

__author__ = 'marie-helene'
from encoder import Encoder
from preprocess import Preprocess
from CipherAlbert import CeasarCipher



key = "jesus"
url = "https://www.gutenberg.org/cache/epub/28210/pg28210.txt"
import_text = requests.get(url)
text = import_text.text[10000:20000].lower()
encoded_text = cipher(text, key)


file = open("encoded_text_vigenere.txt", "w")
file.write(encoded_text)


