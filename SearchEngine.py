from bs4 import BeautifulSoup
import requests
from trie import Trie

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
            for word in words:
                self.index.insert(word, url)
        except requests.exceptions.RequestException as e:
            print(f"Error indexing page at {url}: {e}")

    def search(self, query):
        return self.index.search(query)
