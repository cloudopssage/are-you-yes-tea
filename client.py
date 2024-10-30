import requests

BASE_URL = "http://127.0.0.1:8080/books"

def get_books():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        books = response.json()
        print("Books:", books)
    else:
        print("Failed to fetch books:", response.status_code)

def add_book(book):
    response = requests.post(BASE_URL, json=book)
    if response.status_code == 200:
        print("Book added:", response.json())
    else:
        print("Failed to add book:", response.status_code)

if __name__ == "__main__":
    # Add a book
    new_book = {"id": 1, "title": "The Rust Book", "author": "Steve Klabnik"}
    add_book(new_book)

    # Get all books
    get_books()
