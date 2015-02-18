#!/usr/bin/env python3

__author__ = 'jenselme'

from argparse import ArgumentParser
import requests

from decipher import decipher


def cipher(text):
    pass


def main(args):
    text = get_file(args.file_name, args.is_url)
    if args.decipher:
        print(decipher(text))
    else:
        print(cipher(text))


def get_file(file_name, is_url):
    if is_url:
        return requests.get(file_name).text
    else:
        return open(file_name, "r", encoding="utf-8").read()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_name", metavar="file_name")
    parser.add_argument("-d", "--decipher", dest="decipher", action="store_true")
    parser.add_argument("-c", "--cipher", dest="cipher", action="store_true")
    parser.add_argument("-u", "--url", dest="is_url", action="store_true")
    args = parser.parse_args()
    main(args)