# trie.py
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.urls = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, url):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True
        node.urls.add(url)

    def search(self, query):
        node = self.root
        for char in query:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.urls
