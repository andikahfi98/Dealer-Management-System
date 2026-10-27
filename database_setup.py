import sqlite3

conn = sqlite3.connect("dealers.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dealers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
""")

conn.commit()

conn.close()