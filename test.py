import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def test_empty_trie(self):
        trie = Trie()
        self.assertEqual(trie.search("any_query"), set())

    def test_single_character_insertion(self):
        trie = Trie()
        url = "https://example.com"
        trie.insert("a", url)
        self.assertEqual(trie.search("a"), {url})

    def test_long_word_insertion(self):
        trie = Trie()
        url = "https://example.com"
        trie.insert("longword", url)
        self.assertEqual(trie.search("longword"), {url})

    def test_case_sensitivity(self):
        trie = Trie()
        url = "https://example.com"
        trie.insert("CaseSensitive", url)
        self.assertEqual(trie.search("casesensitive"), set())

    def test_special_characters(self):
        trie = Trie()
        url = "https://example.com"
        trie.insert("special!characters", url)
        self.assertEqual(trie.search("special!characters"), {url})

    def test_specific_urls(self):
        trie = Trie()
        url1 = "https://www.bbc.co.uk/archive/agatha-christie/z6jw382"
        url2 = "https://www.bbc.co.uk/archive/enid-blyton/zfn2cqt"
        url3 = "https://www.bbc.co.uk/archive/19th-century-writers/zft8382"

        trie.insert("agatha", url1)
        trie.insert("blyton", url2)
        trie.insert("19th-century", url3)

        # Test searching for terms related to specific URLs
        self.assertEqual(trie.search("agatha"), {url1})
        self.assertEqual(trie.search("blyton"), {url2})
        self.assertEqual(trie.search("19th-century"), {url3})

if __name__ == '__main__':
    unittest.main()
