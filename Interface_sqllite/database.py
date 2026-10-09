import sqlite3

DB_NAME = "data.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS house (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        address TEXT,
        surface REAL,
        bedrooms INTEGER,
        price REAL,
        internet_link TEXT
    )
    """)

    conn.commit()
    conn.close()
