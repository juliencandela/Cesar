import requests

__author__ = 'marie-helene'


class Preprocess:

    def __init__(self, text=""):
        self.text = text

    def import_text(self, url):
        import_text = requests.get(url)
        self.text =import_text.text[10000:50000].lower()




