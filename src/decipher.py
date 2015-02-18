__author__ = 'jenselme'

from string import ascii_letters
from math import ceil


expected_IC = {'fr': 0.0746}
SMALL_CAPS_LETTERS = set(ascii_letters.lower())


def decipher_vigenaire(text):
    key_length = get_key_length(text)
    #return key_length
    print(key_length)
    return ceil((expected_IC['fr'] - 0.0385) / (compute_IC(text) - 0.0385))
    key_length = 5
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


def get_key_length(text):
    # Method: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Friedman_test
    # or http://www.artofproblemsolving.com/blog/27160
    # We try different value for the possible key length
    ICs = []
    for number_of_columns in range(2, 26):
        # Transform text into a matrix with i rows and then compute the IC on the columns
        matrix = get_text_matrix(text, number_of_columns)
        subtexts = []
        for i in range(number_of_columns):
            subtexts.append('')
            for j in range(len(matrix)):
                # The last line can have less columns
                try:
                    subtexts[i] += matrix[i][j]
                except IndexError:
                    continue
        subtexts_ICs = [compute_IC(subtext) for subtext in subtexts]
        ICs.append(sum(subtexts_ICs) / len(subtexts_ICs))
    # The key length is the index of the ICs with the best IC + 1 (index start at 0, key length at 1)
    print(ICs)
    return ICs.index(max(ICs)) + 1


def get_text_matrix(text, number_of_columns):
    matrix = []
    for i in range(0, len(text), number_of_columns):
        matrix.append(text[i:i + number_of_columns])
    return matrix


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
