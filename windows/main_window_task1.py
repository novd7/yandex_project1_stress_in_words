import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.WordStressWidget import WordStressWidget
from design.design_main_window_task1 import DesignMainWindowTask1


class MainWindowTask1(QMainWindow, DesignMainWindowTask1):
    def __init__(self, word_with_stress):
        super().__init__()
        self.word_with_stress = word_with_stress
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.wsw = WordStressWidget(self.centralwidget, self.word_with_stress)
        self.btn.clicked.connect(self.close_)
        # print("________________")
    
    def close_(self):
        self.lbl.setText("")
        if self.wsw.res is not None:
            self.close()
        else:
            self.lbl.setText("Вы не выбрали ответ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pr = MainWindowTask1("тОрты")
    pr.show()
    app.exec_()
    res = pr.wsw.res
    print(res)
