import random

import requests
from collections import namedtuple

# Define the named tuple 'Book' to store title, author, year, and ISBN_13
Book = namedtuple('Book', ['isbn', 'title', 'author', 'year'])


def fetch_books_from_api(keyword, max_results=5):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': keyword,
        'maxResults': max_results,
        'printType': 'books',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        response.raise_for_status()


def parse_book_data(item):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title', 'N/A')
    authors = volume_info.get('authors', ['N/A'])
    published_date = volume_info.get('publishedDate', 'N/A')
    industry_identifiers = volume_info.get('industryIdentifiers', [])

    # Extract ISBN_13
    isbn_13_identifier = None

    for identifier in industry_identifiers:
        if identifier['type'] == 'ISBN_13':
            isbn_13_identifier = identifier['identifier']
            break

    # Extract the year from the published_date if it exists
    year = published_date.split('-')[0] if published_date != 'N/A' else 'N/A'

    return Book(isbn=isbn_13_identifier, title=title, author=', '.join(authors), year=year)


# Generate random keyword (for demonstration, using 'biology' here)
keywords = ['science', 'history', 'art', 'technology', 'literature', 'math', 'geography', 'biology', 'chemistry']
random_keyword = random.choice(keywords)

# Fetch and parse book data
book_items = fetch_books_from_api(random_keyword)
print(book_items)

books = [parse_book_data(item) for item in book_items]
books.sort(key=lambda book: book.year)

# Print the book details
print(f"Books fetched using the keyword: {random_keyword} sorted by the year")
for book in books:
    print(f"ISBN_13: {book.isbn} Title: {book.title}, Author: {book.author}, Year: {book.year}")
