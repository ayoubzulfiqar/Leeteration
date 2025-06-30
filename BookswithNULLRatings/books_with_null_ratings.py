import sqlite3
import os

def solve_books_with_null_ratings():
    db_name = 'books_db_null_ratings.db'

    if os.path.exists(db_name):
        os.remove(db_name)

    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                rating INTEGER
            );
        ''')

        books_data = [
            ('The Hitchhiker\'s Guide to the Galaxy', 5),
            ('Dune', 4),
            ('The Lord of the Rings', None),
            ('Foundation', 5),
            ('Neuromancer', None),
            ('Brave New World', 3),
            ('Fahrenheit 451', None)
        ]
        cursor.executemany("INSERT INTO Books (title, rating) VALUES (?, ?)", books_data)
        conn.commit()

        cursor.execute("SELECT book_id, title FROM Books WHERE rating IS NULL;")
        null_rated_books = cursor.fetchall()

        for book in null_rated_books:
            print(f"Book ID: {book[0]}, Title: {book[1]}")

    finally:
        if conn:
            conn.close()
        if os.path.exists(db_name):
            os.remove(db_name)

if __name__ == "__main__":
    solve_books_with_null_ratings()