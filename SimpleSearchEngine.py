from bs4 import BeautifulSoup
import requests

class SimpleSearchEngine:
    def __init__(self):
        self.index = Trie()

    def index_page(self, url, content):
        soup = BeautifulSoup(content, 'html.parser')
        text_content = soup.get_text().lower()
        words = text_content.split()
        for word in words:
            self.index.insert(word, url)

    def search(self, query):
        return self.index.search(query)
