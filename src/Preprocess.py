import requests

__author__ = 'marie-helene'


class Preprocess:

    def __init__(self, url=""):
        self.url = url

    def import_text(self):
        importtext = requests.get(self.url)
        return importtext.text