import sqlite3

con = sqlite3.connect("data.sqlite")
cur = con.cursor()
cur.execute("""CREATE TABLE words
(id INTEGER PRIMARY KEY AUTOINCREMENT,
right TEXT NOT NULL UNIQUE,
wrong TEXT NOT NULL UNIQUE )""")
with open("db.txt", encoding='utf-8') as file:
    file = file.read().splitlines()
    for line in file:
        r, w = line.split()
        print(r, w)
        cur.execute(f"""INSERT INTO words
        (right, wrong) VALUES ('{r}', '{w}')""")
#
a = cur.execute("""SELECT * FROM words""").fetchall()
print(a)
con.commit()
# a = cur.execute("""SELECT * FROM words""").fetchall()
# print(a)
# a = cur.execute("""SELECT * FROM words""").fetchall()
# print(a)