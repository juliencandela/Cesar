#!/usr/bin/env python3

__author__ = 'jenselme'

from argparse import ArgumentParser
import requests

from decipher import decipher, decipher_manual
from encoder import Encoder


def main(args):
    text = get_file(args.file_name, args.is_url)
    if args.decipher:
        return decipher(text)
    elif args.manual:
        return decipher_manual(text)
    elif args.key > -1:
        return decipher(text, key=args.key)
    else:
        cipher = Encoder(key=args.cipher)
        return cipher.cipher(text)


def get_file(file_name, is_url):
    if is_url:
        return requests.get(file_name).text
    else:
        return open(file_name, "r", encoding="utf-8").read()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_name", metavar="file_name")
    parser.add_argument("-d", "--decipher", dest="decipher", action="store_true")
    parser.add_argument("-c", "--cipher", dest="cipher", default=-1, type=int)
    parser.add_argument("-u", "--url", dest="is_url", action="store_true")
    parser.add_argument("-m", "--manual", dest="manual", action="store_true")
    parser.add_argument("-k", "--key", dest="key", default=-1, type=int)
    parser.add_argument("-v", "--vigenaire", dest="vigenaire", action="store_true")
    args = parser.parse_args()
    print(main(args))