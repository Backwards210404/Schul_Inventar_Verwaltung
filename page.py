from PyQt6.QtWidgets import *

class Page(QMainWindow):
    def showPage(self):
        self.show()
    def createButton(self, name:str, position:tuple):
        button = QPushButton(name, self)
        button.move(position)

        return button
    def createInput(self, placeHolderName:str, position):
        input = QLineEdit(self)
        input.setPlaceholderText(placeHolderName)
        input.move(position)

        return input
    def createHeader(self, name:str)
    def createText(self, name:str,position: tuple):
        label = QLabel(name)
        label.move(position)

        return label
    def createButton(self, name:str)
    def createButton(self, name:str)
    def createButton(self, name:str)