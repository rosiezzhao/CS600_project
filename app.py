from flask import Flask, render_template, request
from SearchEngine import SearchEngine

app = Flask(__name__)
search_engine = SearchEngine()

# Index provided web pages
urls_to_index = [
    "https://www.bbc.co.uk/archive/agatha-christie/z6jw382",
    "https://www.bbc.co.uk/archive/enid-blyton/zfn2cqt",
    "https://www.bbc.co.uk/archive/19th-century-writers/zft8382",
    "https://www.bbc.co.uk/archive/stevie-smith/zkrwcqt",
    "https://www.bbc.co.uk/archive/around-london/zr2drj6",
    "https://www.bbc.co.uk/archive/around-yorkshire/zfq6jhv",
    "https://www.bbc.co.uk/archive/scotland/zdnyxyc",
    "https://www.bbc.co.uk/archive/wales/zmbcscw",
    "https://www.bbc.co.uk/archive/northern-ireland/zkhs2sg",
]

for url in urls_to_index:
    search_engine.index_page(url)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def perform_search():
    query = request.form.get('query')
    results = search_engine.search(query)
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
