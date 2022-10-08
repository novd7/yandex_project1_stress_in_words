import sys

from PyQt5.QtWidgets import QApplication, QWidget

from start_window import StartWindow, task, count


class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        StartWindow()
    
    def initUI(self):
        self.setGeometry(400, 70, 400, 70)
        self.setWindowTitle('Подготовка к ЕГЭ по русскому языку')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    app.exec_()
    task = ex.task
    count = ex.count
