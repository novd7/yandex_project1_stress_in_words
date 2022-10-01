import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(400, 70, 400, 70)
        self.setWindowTitle('Подготовка к ЕГЭ по русскому языку')


if __name__ == '__main__':
    print(1)
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec())
