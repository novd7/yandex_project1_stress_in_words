import random
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication

from main_window_task1 import MainWindowTask1
from start_window import StartWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    app.exec_()
    task = ex.task
    count = ex.count
    print(task, count, sep='\n')

    # count = 2
    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()
    data = cur.execute("""SELECT right, wrong FROM words""").fetchall()
    random.shuffle(data)
    print(data)
    for r, w in data[:count]:
        print(r)
        app2 = QApplication(sys.argv)
        ex2 = MainWindowTask1(r)
        ex2.show()
        app2.exec_()
        res = ex2.wsw.res
        if res == "cons":
            # TODO: open new window with funny image "Go to the first form!:)"
            break
        print(res)
