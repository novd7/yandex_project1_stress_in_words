import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class DesignStartWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Выбрать задание")
        MainWindow.resize(375, 154)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 371, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_greetings = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_greetings.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_greetings.setObjectName("label_greetings")
        self.verticalLayout.addWidget(self.label_greetings)
        self.button_choose_task = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_choose_task.setObjectName("button_choose_task")
        self.verticalLayout.addWidget(self.button_choose_task)
        self.button_chose_count = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_chose_count.setObjectName("button_chose_count")
        self.verticalLayout.addWidget(self.button_chose_count)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_greetings.setText(_translate("MainWindow", "Добро пожаловать!\n"
                                                              "Предлагаю Вам подготовиться к ЕГЭ по русскому языку (задание 4)\n"
                                                              "и к другим диагностическим работам, \n"
                                                              "а конкретно к заданиям про постановку ударения"))
        self.button_choose_task.setText(_translate("MainWindow", "Выбрать задание"))
        self.button_chose_count.setText(_translate("MainWindow", "PushButton"))


if __name__ == '__main__':
    class Test(QMainWindow, DesignStartWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
    
    
    app = QApplication(sys.argv)
    plan = Test()
    plan.show()
    sys.exit(app.exec_())
