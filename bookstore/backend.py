import sqlite3


def connect(sql):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def connect_fetch(sql):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(sql)
    all_books = cur.fetchall()
    conn.close()
    return all_books


def create_table():
    connect("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, "
            "author TEXT, isbn INTEGER)")

#
# create_table()


def insert(title, year, author, isbn):
    connect(f"INSERT INTO books VALUES(NULL, '{title}', {year}, '{author}', {isbn})")


def delete(book_id):
    connect(f"DELETE FROM books WHERE id={book_id}")


def update(book_id, title="", year="", author="", isbn=""):
    if title:
        connect(f"UPDATE books SET title='{title}' WHERE id={book_id}")
    if author:
        connect(f"UPDATE books SET author='{author}' WHERE id={book_id}")
    if year:
        connect(f"UPDATE books SET year='{year}' WHERE id={book_id}")
    if isbn:
        connect(f"UPDATE books SET isbn='{isbn}' WHERE id={book_id}")


def view_all():
    return connect_fetch("SELECT * FROM books")


def search(title="", year="", author="", isbn=""):
    return connect_fetch(f"SELECT * FROM books WHERE title='{title}' OR year='{year}' OR author='{author}' OR isbn='{isbn}'")
