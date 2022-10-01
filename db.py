import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("""CREATE TABLE words
(id INTEGER PRIMARY KEY AUTOINCREMENT,
right TEXT NOT NULL UNIQUE,
wrong TEXT NOT NULL UNIQUE )""")
cur.execute("""INSERT INTO  words
(right, wrong) VALUES ('тОрты', 'тортЫ')""")