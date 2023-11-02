import random
import sqlite3


    # cur.execute("DROP TABLE IF EXISTS scores")
def addInDb():
    with sqlite3.connect("scores.db") as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS scores (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL DEFAULT JOHN_DOE,
        score INTEGER DEFAULT 0
        )""")

        # while True:
        #     try:
        #         times = int(input("How many players we have? > "))  # сюда должно передаваться имя, что игрок введёт в начале
        #         if times <= 0:
        #             print("Please, print a number more then 0.")
        #         else:
        #             break
        #     except ValueError:
        #         print("Please, enter a number")

        name = input("Your name? > ")
        ran = random.randint(5, 5000)
        # print(name, idd, ran)
        # print(type(name), type(idd), type(ran))
        cur.execute(f"INSERT OR IGNORE INTO scores (name, score) VALUES (?, ?)", (name, ran))