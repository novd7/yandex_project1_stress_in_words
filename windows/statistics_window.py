import sys
import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

from design.design_statistics_window import DesignStatisticsWindow


class StatisticsWindow(QMainWindow, DesignStatisticsWindow):
    def __init__(self):
        super().__init__()
        self.path_to_db = "database/data.sqlite"
        if __name__ == '__main__':
            self.path_to_db = "../" + self.path_to_db
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.clear_history)
        self.pin_table()
        
    def pin_table(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.path_to_db)
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('results')
        model.sort(0, QtCore.Qt.DescendingOrder)
        model.select()
        self.tableView.setModel(model)
        
    def clear_history(self):
        con = sqlite3.connect(self.path_to_db)
        cur = con.cursor()
        cur.execute("""DELETE FROM results""")
        con.commit()
        self.pin_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = StatisticsWindow()
    plan.show()
    app.exec_()

