import random
import sqlite3
import sys

from PyQt5.QtWidgets import QApplication

from windows.start_window import StartWindow, TASK1, TASK2
from windows.main_window_task1 import MainWindowTask1
from windows.funny_end_window_task1 import FunnyEndWindowTask1
from windows.main_window_task2 import MainWindowTask2


def main():
    app = QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    app.exec_()
    task = start_window.task
    count = start_window.count
    print(task, count, sep='\n')
    
    con = sqlite3.connect("database/data.sqlite")
    cur = con.cursor()
    data = cur.execute("""SELECT right, wrong FROM words""").fetchall()
    random.shuffle(data)
    all_results = []
    pluses = 0
    minuses = 0
    
    def print_results(results_of_test, count_right_answers, count_wrong_answers):
        print("RESULTS:")
        print(*results_of_test, sep='\n')
        print("Correct answers:", count_right_answers)
        print("Incorrect answers:", count_wrong_answers)
        print(str(round((count_right_answers / (count_right_answers + count_wrong_answers)) * 100)) + "%")
    
    if task == TASK1:
        for r, w in data[:count]:
            print(r)
            task1_window = MainWindowTask1(r)
            task1_window.show()
            app.exec_()
            res = task1_window.wsw.res
            
            if res[1] == "cons":
                funny_end = FunnyEndWindowTask1()
                funny_end.show()
                app.exec_()
                break
            if res[1]:
                pluses += 1
            else:
                minuses += 1
            print(res)
            all_results.append(res)
        print_results(all_results, pluses, minuses)
    
    elif task == TASK2:
        data = [(data[i], data[i + 1], data[i + 2], data[i + 3]) for i in range(0, count * 4, 4)]
        print(data)
        for w1, w2, w3, w4 in data:
            words = [w1[0], w2[0], w3[0], w4[1]]
            word_with_mistake = w4[1]
            random.shuffle(words)
            wrong_index = words.index(word_with_mistake)
            task2_window = MainWindowTask2(*words, ans=wrong_index)
            task2_window.show()
            app.exec_()
            res = task2_window.res
            if res[1]:
                pluses += 1
            else:
                minuses += 1
            print(res)
            all_results.append(res)
        print_results(all_results, pluses, minuses)


if __name__ == '__main__':
    main()
