import sqlite3


def connect_to_db(sql):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def create_table():
    connect_to_db("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, isbn INTEGER)")


create_table()


def insert(title, year, author, isbn):
    connect_to_db(f"INSERT INTO books VALUES(NULL, '{title}', {year}, '{author}', {isbn})")


def delete(book_id):
    connect_to_db(f"DELETE FROM books WHERE id={book_id}")


def update(book_id, title, author, year, isbn):
    connect_to_db(f"UPDATE books SET year={year}, isbn={isbn}, author='{author}', title='{title}' WHERE id={book_id}")


def view_all():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    all_books = cur.fetchall()
    conn.close()
    return all_books
