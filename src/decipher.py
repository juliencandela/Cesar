__author__ = 'jenselme'

from string import ascii_letters


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


def decipher(text):
    if not text:
        return ''
    text = text.lower()
    key = get_shift(text)
    clear_text = ''
    for letter in text:
        clear_text += unshift_letter(letter, key)

    return clear_text
