import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog

from design.design_start_window import DesignStartWindow

task, count = None, None
TASK1 = "Указать ударение в слове"
TASK2 = "Из четырёх слов выбрать слово с неправильной постановкой ударения"

class StartWindow(QMainWindow, DesignStartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.COUNT_WORDS = 203
    
    def initUI(self):
        self.button_choose_task.clicked.connect(self.chose_task)
        self.button_chose_count.clicked.connect(self.chose_count)
        self.button_chose_count.setVisible(False)
    
    def chose_task(self):
        self.task, self.button_choose_task_pressed = QInputDialog.getItem(
            self, "Задание", "Выберите задание:",
            (TASK1, TASK2), 0, False)
        if self.button_choose_task_pressed:
            if self.task == TASK1:
                self.button_chose_count.setText("Ввести количество слов")
            elif self.task == TASK2:
                self.button_chose_count.setText("Ввести кол-во заданий")
            self.button_chose_count.setVisible(True)
    
    def chose_count(self):
        if self.task == TASK1:
            self.count, self.button_chose_count_pressed = QInputDialog.getInt(
                self, "Количество", "Введите слов: ",
                10, 1, self.COUNT_WORDS, 1)
        elif self.task == TASK2:
            self.count, self.button_chose_count_pressed = QInputDialog.getInt(
                self, "Количество", "Введите количество заданий: ",
                5, 1, self.COUNT_WORDS // 4, 1)
        if self.button_choose_task_pressed and self.button_chose_count_pressed:
            global task, count
            task = self.task
            count = self.count
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = StartWindow()
    plan.show()
    app.exec_()
