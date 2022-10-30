import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from design.design_end_window import DesignEndWindow


class EndWindow(QMainWindow, DesignEndWindow):
    def __init__(self, results, percent):
        self.results = results
        self.percent = int(percent[:-1])
        super().__init__()
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.close)
        for word, result in self.results:
            if result != "cons" and result:
                result = "Верно"
            else:
                result = "Неверно"
            self.listWidget.addItem(word + " - " + result)
        self.progressBar.setValue(self.percent)
        if self.percent >= 88:
            self.label_3.setText("5")
        elif self.percent >= 75:
            self.label_3.setText("4")
        elif self.percent >= 50:
            self.label_3.setText("3")
        else:
            self.label_3.setText("2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pr = EndWindow([('корЫсть', True), ('создалА', False), ('аэропОрты', 'cons')], "33%")
    pr.show()
    app.exec_()
