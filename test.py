# test_boundary_conditions.py
from search_engine import SearchEngine

def test_empty_query():
    search_engine = SearchEngine()
    query = ""
    results = search_engine.search(query)
    assert results == set(), "Failed: Empty query did not return an empty result set"

def test_stop_words():
    search_engine = SearchEngine()
    query = "the"
    results = search_engine.search(query)
    assert results == set(), "Failed: Stop words were not excluded during indexing"

def test_nonexistent_query():
    search_engine = SearchEngine()
    query = "nonexistentterm"
    results = search_engine.search(query)
    assert results == set(), "Failed: Nonexistent query did not return an empty result set"

def test_empty_page_indexing():
    search_engine = SearchEngine()
    empty_url = "https://www.example.com/empty"
    search_engine.index_page(empty_url)
    assert search_engine.search("anyterm") == set(), "Failed: Empty page did not index correctly"

def test_repeated_indexing():
    search_engine = SearchEngine()
    repeated_url = "https://www.example.com/repeated"
    search_engine.index_page(repeated_url)
    search_engine.index_page(repeated_url)
    results = search_engine.search("anyterm")
    assert len(results) == 1, "Failed: Repeated indexing resulted in duplicate entries"

def test_special_characters_in_query():
    search_engine = SearchEngine()
    query = "!@#$%^&*()_+"
    results = search_engine.search(query)
    assert results == set(), "Failed: Special characters in query did not return an empty result set"

if __name__ == "__main__":
    # Run all test functions
    test_empty_query()
    test_stop_words()
    test_nonexistent_query()
    test_empty_page_indexing()
    test_repeated_indexing()
    test_special_characters_in_query()

    print("All tests passed!")
