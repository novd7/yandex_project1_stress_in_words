import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.WordStressWidget import WordStressWidget
from design.design_main_window_task1 import DesignMainWindowTask1


class MainWindowTask1(QMainWindow, DesignMainWindowTask1):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.wsw = WordStressWidget(self.centralwidget, "тОрты")
        self.wsw.buttons[0].move(0, 100)
        print("________________")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = MainWindowTask1()
    plan.show()
    app.exec_()
    print("_______________________________________________")
    res = plan.wsw.res
    print(res)
