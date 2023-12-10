# CS600_project Search Engine

This is a simple search engine developed in Python, utilizing Flask for web development and a Trie data structure for efficient word indexing. The goal is to provide users with a simple and responsive search experience, allowing them to search through the content of indexed web pages.

## Table of Contents
- [Algorithms and Data Structure](#algorithms-and-data-structure)
- [Testing](#testing)
- [Usage](#usage)
- [Prerequisites](#prerequisites)


## Algorithms and Data Structure

The search engine employs the following algorithms and data structures:

- **Trie:** The project employs a Trie data structure for indexing words from the web pages. The Trie is a tree-like structure that efficiently stores a dynamic set of strings, making it suitable for fast word lookups.

- **Search Engine:** The Simple Search Engine class acts as a wrapper around the Trie, providing methods to index web pages and perform searches.
  
- **Data:** Data used for this project is shown in urls.txt.

## Testing

Use following six methods to test the boundary conditions.
1. Empty query
2. Stop words
3. Nonexistent query
4. Empty page indexing
5. Repeated indexing
6. Special Characters

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a search query and click the "Search" button to see the results.

## Prerequisites

- Python3
- Flask
- Requests
- BeautifulSoup4
- Unittest
