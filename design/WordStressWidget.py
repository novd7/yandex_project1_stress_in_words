from PyQt5 import QtWidgets, QtCore, QtGui

CONSONANTS = "бвгджзйклмнпрстфхцчшщъь"
VOWELS = "аеёиоуыэюя"


class WordStressWidget:
    def __init__(self, centralwidget, word_with_stress):
        self.centralwidget = centralwidget
        self.word_with_stress = word_with_stress
        self.right_index = [i for i, letter in enumerate(self.word_with_stress) if letter.isupper()].pop()
        self.buttons = []
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 150, len(self.word_with_stress) * 40, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.__add_buttons()
        for i in self.buttons:
            self.horizontalLayout.addWidget(i)
        
        self.res = None
    
    def __add_buttons(self):
        """add button for each letter in word"""
        for n, i in enumerate(self.word_with_stress.lower()):
            push_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            push_button.setFont(font)
            push_button.setText(i)
            if i in CONSONANTS:
                push_button.clicked.connect(self.__cons_answer)
                print(1)
            elif n == self.right_index:
                push_button.clicked.connect(self.__right_answer)
                print(2)
            else:
                push_button.clicked.connect(self.__wrong_answer)
                print(3)
            self.buttons.append(push_button)
    
    def __cons_answer(self):
        self.res = "cons"
        print("cons")
    
    def __right_answer(self):
        self.res = True
        print(True)
    
    def __wrong_answer(self):
        self.res = False
        print(False)
