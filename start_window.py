import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from design.design_start_window import DesignStartWindow
from PyQt5.QtWidgets import QInputDialog


class StartWindow(QMainWindow, DesignStartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.COUNT_WORDS = 100  # Ввести количество слов
    
    def initUI(self):
        self.button_choose_task.clicked.connect(self.chose_task)
        self.button_chose_count.clicked.connect(self.chose_count)
        self.button_chose_count.setVisible(False)
    
    def chose_task(self):
        self.task, self.button_choose_task_pressed = QInputDialog.getItem(
            self, "Задание", "Выберите задание:",
            ("Указать ударение в слове",
             "Из четырёх слов выбрать слово с неправильной постановкой ударения"),
            1, False)
        if self.button_choose_task_pressed:
            if self.task == "Указать ударение в слове":
                self.button_chose_count.setText("Ввести количество слов")
            elif self.task == "Из четырёх слов выбрать слово с неправильной постановкой ударения":
                self.button_chose_count.setText("Ввести кол-во задааний")
            self.button_chose_count.setVisible(True)
            
    def chose_count(self):
        if self.task == "Указать ударение в слове":
            self.count, self.button_chose_count_pressed = QInputDialog.getInt(
                self, "Количество", "Введите слов: ",
                10, 1, self.COUNT_WORDS, 1)
        elif self.task == "Из четырёх слов выбрать слово с неправильной постановкой ударения":
            self.count, self.button_chose_count_pressed = QInputDialog.getInt(
                self, "Количество", "Введите количество заданий: ",
                5, 1, self.COUNT_WORDS // 4, 1)
        if self.button_choose_task_pressed and self.button_chose_count_pressed:
            # data = {'task': self.task, 'count': self.count}
            # with open('data.json', 'w') as file:
            #     json.dump(data, file)
            global task, count
            task = self.task
            count = self.count
            self.close()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = StartWindow()
    plan.show()
    sys.exit(app.exec_())