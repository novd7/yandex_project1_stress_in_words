import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.design_main_window_task2 import DesignMainWindowTask2


class MainWindowTask2(QMainWindow, DesignMainWindowTask2):
    def __init__(self, *words, ans: int):
        self.words = words
        self.res = ()
        self.ans = ans
        super().__init__()
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.radioButton.setText(self.words[0])
        self.radioButton_2.setText(self.words[1])
        self.radioButton_3.setText(self.words[2])
        self.radioButton_4.setText(self.words[3])
        self.pushButton.clicked.connect(self.close_)
    
    def close_(self):
        self.label_2.setText("")
        give_res = lambda x: (self.words[self.ans], self.words[self.ans] == x)
        if self.radioButton.isChecked():
            self.res = give_res(self.radioButton.text())
            self.close()
        elif self.radioButton_2.isChecked():
            self.res = give_res(self.radioButton_2.text())
            self.close()
        elif self.radioButton_3.isChecked():
            self.res = give_res(self.radioButton_3.text())
            self.close()
        elif self.radioButton_4.isChecked():
            self.res = give_res(self.radioButton_4.text())
            self.close()
        else:
            self.label_2.setText("Вы не\nвыбрали\nответ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pr = MainWindowTask2("corr1", "corr2", "incorr", "corr3", ans=2)
    pr.show()
    app.exec_()
    print(pr.res)
