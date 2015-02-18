from decipher import (
    letter_freq,
    unshift_letter,
    get_more_frequent_letter,
    get_shift,
    decipher,
)


def test_letter_freq():
    text = 'Bonjour, je suis en cours'
    freq = letter_freq(text)
    assert freq['u'] == 3
    assert freq['b'] == 1
    assert 'a' not in freq



def test_get_more_frequent_letter():
    text = 'Bonjour'
    assert get_more_frequent_letter(text) == 'o'


def test_unshift_letter():
    new_letter = unshift_letter('e', 0)
    assert new_letter == 'e'


def test_unshift_letter_key():
    new_letter = unshift_letter('e', 3)
    assert new_letter == 'h'


def test_get_shift():
    text = 'eeeeea'
    assert get_shift(text) == 0


def test_get_shift_ae():
    text = 'aaaaaae'
    assert get_shift(text) == 4


def test_decipher_uncipher_text():
    text = 'element'
    assert decipher(text) == text.lower()


def test_decipher():
    text = 'fmfnfou'
    assert decipher(text) == 'element'.lower()

def test_decipher_space():
    text = 'fmfnfou fmfnfou'
    assert decipher(text) == 'element element'.lower()


def test_decipher_special_chars():
    text = 'fmfnfou-fmfnfouééé &&& ààà @@@@ ++ fmfnfou fmfnfou'
    assert decipher(text) == 'element-elementÉÉÉ &&& ààà @@@@ ++ element element'.lower()


def test_decipher_alphabet_lower_bound():
    text = 'fmfnfoua'
    assert decipher(text) == 'elementz'.lower()


def test_decipher_alphabet_lower_bound():
    text = 'dkdldmsz'
    assert decipher(text) == 'elementa'.lower()


def test_decipher_no_text():
    assert decipher('') == ''