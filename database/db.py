import sqlite3

def create_bd_of_words():
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
    con.commit()
    
def create_bd_of_results():
    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()
    cur.execute("""CREATE TABLE results
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT NOT NULL,
        task_number INT NOT NULL,
        count_right_answers INT NOT NULL,
        count_wrong_answers INT NOT NULL,
        result INT NOT NULL)""")
    con.commit()

create_bd_of_words()
create_bd_of_results()
