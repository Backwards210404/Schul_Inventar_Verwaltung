from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
class Page(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 600)
        self.setStyleSheet("background-color: white;")
    def showPage(self):
        self.show()
    def createButton(self, name:str, x = None, y = None):
        button = QPushButton(name, self)
        if x != None and y != None:
            button.move(x, y)
        return button
    def createInput(self, placeHolderName:str, x = None, y = None):
        input = QLineEdit(self)
        input.setPlaceholderText(placeHolderName)
        if x != None and y != None:
            input.move(x, y)

        return input
    def createText(self, name:str,x = None, y = None):
        label = QLabel(name)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        if x != None and y != None:
            label.move(x, y)

        return label
    def createTitle(self, name:str,x = None, y = None):
        label = QLabel('<h1>' + name + '</h1>')
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        if x != None and y != None:
            label.move(x, y)

        return label