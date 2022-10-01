import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget
from start_window import StartWindow


task, count = None, None


class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(400, 70, 400, 70)
        self.setWindowTitle('Подготовка к ЕГЭ по русскому языку')


if __name__ == '__main__':
    # with open('data.json') as file:
    #     data = json.load(file)
    #     print(data)
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    print(1)
    sys.exit(app.exec())
print(task, count)
