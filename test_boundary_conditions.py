# test_boundary_conditions.py
import unittest
from search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        self.search_engine = SearchEngine()

    def test_empty_query(self):
        results = self.search_engine.search("")
        self.assertEqual(results, set(), "Failed: Empty query did not return an empty result set")

    def test_stop_words(self):
        self.search_engine.index_page(url)
        results = self.search_engine.search("the")
        self.assertEqual(results, set(), "Failed: Stop words did not return an empty result set")

    def test_nonexistent_query(self):
        self.search_engine.index_page(url)
        results = self.search_engine.search("nonexistentterm")
        self.assertEqual(results, set(), "Failed: Nonexistent query did not return an empty result set")

    def test_empty_page_indexing(self):
        self.search_engine.index_page(url)
        results = self.search_engine.search("term")
        self.assertEqual(results, set(), "Failed: Empty page indexing did not return an empty result set")

    def test_repeated_indexing(self):
        self.search_engine.index_page(url)
        self.search_engine.index_page(url)
        results = self.search_engine.search("agatha")
        self.assertEqual(results, {url},"Failed: Repeated indexing did not return the correct result set")


    def test_special_characters_in_query(self):
        self.search_engine.index_page(url)
        results = self.search_engine.search("special!@#$%^&*()_+characters")
        self.assertEqual(results, set(), "Failed: Special characters in query did not return an empty result set")

if __name__ == "__main__":
    url = "https://www.bbc.co.uk/archive/agatha-christie/z6jw382"
    unittest.main()
