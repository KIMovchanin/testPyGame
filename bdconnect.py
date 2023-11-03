import sqlite3


def addindb(name, seconds, score):
    with sqlite3.connect("scores.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS scores (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL DEFAULT JOHN_DOE,
        time INTEGER DEFAULT 0,
        score INTEGER DEFAULT 0
        )""")

        # ran = random.randint(5, 5000)
        cur.execute(f"INSERT OR IGNORE INTO scores (name, time, score) VALUES (?, ?, ?)",
                    (name, seconds, score))
