from PyQt6.QtWidgets import *
class Page(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 600)
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