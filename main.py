import random
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication

from windows.main_window_task1 import MainWindowTask1
from windows.main_window_task2 import MainWindowTask2
from windows.start_window import StartWindow, TASK1, TASK2


def main():
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    app.exec_()
    task = ex.task
    count = ex.count
    print(task, count, sep='\n')
    
    # count = 2
    con = sqlite3.connect("database/data.sqlite")
    cur = con.cursor()
    data = cur.execute("""SELECT right, wrong FROM words""").fetchall()
    random.shuffle(data)
    # print(data)
    if task == TASK1:
        results = []
        pluses = 0
        minuses = 0
        for r, w in data[:count]:
            print(r)
            # app2 = QApplication(sys.argv)
            ex2 = MainWindowTask1(r)
            ex2.show()
            app.exec_()
            # app.exec()
            res = ex2.wsw.res
            
            if res[1] == "cons":
                # TODO: open new window with funny image "Go to the first form!:)"
                break
            if res[1]:
                pluses += 1
            else:
                minuses += 1
            print(res)
            results.append(res)
        print("results:")
        print(*results, sep='\n')
        print("Correct answers:", pluses)
        print("Incorrect answers:", minuses)
        print(str(round((pluses / (pluses + minuses)) * 100)) + "%")
        
    elif task == TASK2:
        results = []
        pluses = 0
        minuses = 0
        data = [(data[i], data[i + 1], data[i + 2], data[i + 3]) for i in range(0, count * 4, 4)]
        print(data)
        for w1, w2, w3, w4 in data:
            print("###")
            words = [w1[0], w2[0], w3[0], w4[1]]
            wrong = w4[1]
            random.shuffle(words)
            wrong_index = words.index(wrong)
            ex2 = MainWindowTask2(*words, ans=wrong_index)
            ex2.show()
            app.exec_()
            # app.exec()
            res = ex2.res
            if res[1]:
                pluses += 1
            else:
                minuses += 1
            print(res)
            results.append(res)
        print("results:")
        print(*results, sep='\n')
        print("Correct answers:", pluses)
        print("Incorrect answers:", minuses)
        print(str(round((pluses / (pluses + minuses)) * 100)) + "%")


if __name__ == '__main__':
    main()
