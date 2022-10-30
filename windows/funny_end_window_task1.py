import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.design_funny_end_window_task1 import DesignFunnyEndWindowTask1


class FunnyEndWindowTask1(QMainWindow, DesignFunnyEndWindowTask1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.smile_path = get_path()
        self.initUI()
        self.would_like_to_receive_result = False
    
    def initUI(self):
        self.pushButton.clicked.connect(self.watch_result)
        self.pixmap = QPixmap(self.smile_path)
        self.image.setPixmap(self.pixmap)
    
    def watch_result(self):
        self.would_like_to_receive_result = True
        self.close()
        
def get_path():
    path = "design/smile.png"
    try:
        open(path)
    except FileNotFoundError:
        path = "../" + path
    print(path)
    return path


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pr = FunnyEndWindowTask1()
    pr.show()
    app.exec_()
