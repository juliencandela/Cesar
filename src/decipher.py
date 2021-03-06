__author__ = 'jenselme'

from string import ascii_letters
from math import ceil


expected_IC = {'fr': 0.0746}
SMALL_CAPS_LETTERS = set(ascii_letters.lower())


def decipher_vigenaire(text):
    key_length = ceil((expected_IC['fr'] - 0.0385) / (compute_IC(text) - 0.0385))
    subtexts = ['' for i in range(key_length)]
    for index, letter in enumerate(text):
        subtexts[index % key_length] += letter
    deciphered_subtexts = [decipher(subtext) for subtext in subtexts]
    clear_text = ''
    for index in range(len(deciphered_subtexts[0])):
        for subtext in deciphered_subtexts:
            try:
                clear_text += subtext[index]
            except IndexError:
                return clear_text
    return clear_text


def compute_IC(text):
    freq = letter_freq(text)
    n = get_number_small_caps_letter(text)
    IC = 0
    for letter in SMALL_CAPS_LETTERS:
        n_q = freq.get(letter, 0)
        IC += n_q * (n_q - 1)
    IC /= (n * (n - 1))
    return IC



def letter_freq(text):
    text = text.lower()
    freq = {}
    for letter in text:
        if letter in ascii_letters:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

    return freq


def get_number_small_caps_letter(text):
    n = 0
    for letter in text:
        if letter in SMALL_CAPS_LETTERS:
            n += 1
    return n


def get_more_frequent_letter(text):
    freq = letter_freq(text)
    more_frequent_letter = ''
    more_frequent_letter_freq = 0
    for letter, frequence in freq.items():
        if frequence > more_frequent_letter_freq:
            more_frequent_letter = letter
            more_frequent_letter_freq = frequence

    return more_frequent_letter


def unshift_letter(letter, key):
    if letter in ascii_letters:
        letter = letter.lower()
        letter_code = ord(letter)
        unshift_letter_code = correct_letter_code(letter_code + key)
        return chr(unshift_letter_code)
    else:
        return letter


def correct_letter_code(code):
    """If code is outside ord('a')-ord('z'), we correct it
    """
    if code > ord('z'.lower()):
        return code - 26
    elif code < ord('a'.lower()):
        return code + 26
    else:
        return code


def get_shift(text):
    text = text.lower()
    more_frequent_letter = get_more_frequent_letter(text)
    more_frequent_letter_code = ord(more_frequent_letter)
    return ord('e'.lower()) - more_frequent_letter_code


def decipher(text, key=None):
    if not text:
        return ''
    if key is None:
        key = get_shift(text)
    print(key)
    text = text.lower()
    clear_text = ''
    for letter in text:
        clear_text += unshift_letter(letter, key)

    return clear_text


def decipher_manual(text):
    phrase = text.split(".")[0]
    for i in range(0, 26):
        clear_phrase = decipher(phrase, key=i)
        print('key {}: {}'.format(i, clear_phrase))
    key = int(input('Enter correct key: '))
    return decipher(text, key=key)
