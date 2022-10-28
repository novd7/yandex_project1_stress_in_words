from PyQt5 import QtCore, QtGui, QtWidgets


class DesignMainWindowTask1(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Задание №1")
        MainWindow.resize(686, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(0, 200)
        self.btn.setText("Далее")
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.move(0, 220)
        self.lbl.setGeometry(QtCore.QRect(0, 220, 220, 80))
        self.lbl.setText("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Нажмите на букву, которую Вы считаете ударной"))
