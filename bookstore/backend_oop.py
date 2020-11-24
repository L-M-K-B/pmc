import sqlite3


class BooksBackend:
    def __init__(self):
        self.connect("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, "
                     "author TEXT, isbn INTEGER)")

    @staticmethod
    def connect(sql):
        conn = sqlite3.connect("bookstore.db")
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def connect_fetch(sql):
        conn = sqlite3.connect("bookstore.db")
        cur = conn.cursor()
        cur.execute(sql)
        all_books = cur.fetchall()
        conn.close()
        return all_books

    def insert(self, title, year, author, isbn):
        self.connect(f"INSERT INTO books VALUES(NULL, '{title}', {year}, '{author}', {isbn})")

    def delete(self, book_id):
        self.connect(f"DELETE FROM books WHERE id={book_id}")

    def update(self, book_id, title="", year="", author="", isbn=""):
        if title:
            self.connect(f"UPDATE books SET title='{title}' WHERE id={book_id}")
        if author:
            self.connect(f"UPDATE books SET author='{author}' WHERE id={book_id}")
        if year:
            self.connect(f"UPDATE books SET year='{year}' WHERE id={book_id}")
        if isbn:
            self.connect(f"UPDATE books SET isbn='{isbn}' WHERE id={book_id}")

    def view_all(self):
        return self.connect_fetch("SELECT * FROM books")

    def search(self, title="", year="", author="", isbn=""):
        return self.connect_fetch(f"SELECT * FROM books WHERE title='{title}' OR year='{year}' OR author='{author}' OR isbn='{isbn}'")
