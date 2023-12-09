# search_engine.py
from trie import Trie
import requests
from bs4 import BeautifulSoup

class SearchEngine:
    def __init__(self):
        self.index = Trie()

    def index_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            text_content = soup.get_text().lower()
            words = text_content.split()

            # Exclude stop words
            stop_words = set(["the", "and", "in", "of", "to", "a", "is", "for", "on", "with", "as", "by", "at"])
            words = [word for word in words if word not in stop_words]

            for word in words:
                self.index.insert(word, url)
        except requests.exceptions.RequestException as e:
            print(f"Error indexing page at {url}: {e}")

    def search(self, query):
        return self.index.search(query)
