import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.WordStressWidget import WordStressWidget
from design.design_funny_end_window_task1 import DesignFunnyEndWindowTask1


class FunnyEndWindowTask1(QMainWindow, DesignFunnyEndWindowTask1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.smile_path = "design/smile.png"
        if __name__ == '__main__':
            self.smile_path = "../" + self.smile_path
        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.watch_result)
        self.pixmap = QPixmap(self.smile_path)
        self.image.setPixmap(self.pixmap)

    def watch_result(self):
        self.close()
        # TODO: go to the window with results


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = FunnyEndWindowTask1()
    plan.show()
    app.exec_()
