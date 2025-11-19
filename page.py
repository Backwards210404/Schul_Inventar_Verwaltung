from PyQt6.QtWidgets import *
from screeninfo import *


class Page(QMainWindow):

    fScreen:Monitor

    def __init__(self):
        super().__init__()
        self.fScreen = get_monitors().__getitem__(0) 
        self.setGeometry(1, 1, self.fScreen.width, self.fScreen.height)
    def showPage(self):
        self.show()
    def createButton(self, name:str, x, y):
        button = QPushButton(name, self)
        button.move(x, y)

        return button
    def createInput(self, placeHolderName:str, x, y):
        input = QLineEdit(self)
        input.setPlaceholderText(placeHolderName)
        input.move(x, y)

        return input
    def createText(self, name:str,x, y):
        label = QLabel(name)
        label.move(x, y)

        return label