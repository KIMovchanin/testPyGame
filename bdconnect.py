import random
import sqlite3



def addindb():
    import main
    with sqlite3.connect("scores.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS scores (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL DEFAULT JOHN_DOE,
        score INTEGER DEFAULT 0
        )""")

        name = 'test'
        # ran = random.randint(5, 5000)
        cur.execute(f"INSERT OR IGNORE INTO scores (name, score) VALUES (?, ?)", (name, main.score))
