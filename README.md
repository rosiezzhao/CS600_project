# CS600_project Search Engine

This is a simple search engine implementation using Python and Flask. The search engine uses a Trie data structure to index and search web pages.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms and Data Structure](#algorithms-and-data-structure)
- [Dependencies](#dependencies)

## Overview

The Simple Search Engine is a lightweight web application that allows users to search for indexed content from a set of predefined web pages. It uses a Trie data structure for efficient indexing and searching.

## Features

- Indexing of web pages using a Trie data structure.
- Search functionality that retrieves relevant results based on user queries.
- Basic web interface for interacting with the search engine.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rosiezzhao/search-engine.git
    cd search-engine
    ```

2. Install dependencies:

    ```bash
    pip install flask requests beautifulsoup4
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a search query and click the "Search" button to see the results.

## Algorithms and Data Structure

The search engine employs the following algorithms and data structures:

- **Trie (Prefix Tree):** Used for indexing words from the web page content. This allows for efficient storage and retrieval of URLs associated with specific words.

- **Depth-First Search (DFS):** Implemented during the Trie search operation to traverse the Trie and find URLs that match the user's query.

## Test
Use following six methods to test the boundary conditions.
1. Empty Trie: Create an empty Trie and verify that attempting to search for any query results in an empty set.
2. Single Character Insertion: Insert a single-character word into the Trie and ensure that searching for that character returns the correct URL (if it was indexed).
3. Long Word Insertion: Insert a long word into the Trie and check if searching for that word returns the correct URL (if it was indexed).
4. Case Sensitivity: Insert words with mixed cases (e.g., "Search" and "search") and check if the Trie is case-sensitive or not.
5. Special Characters: Insert words containing special characters and verify that the Trie handles them correctly.
6. Performance Testing: Generate a large number of words and URLs, insert them into the Trie, and measure the time it takes. Ensure that the Trie performs well within reasonable time limits.

## Dependencies

- Flask: Web framework for building the application.
- Requests: Used for making HTTP requests to fetch web page content.
- BeautifulSoup4: Library for web scraping, used for extracting text content from web pages.
