from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
class Page(QMainWindow):


    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.setFixedSize(self.width, self.height)
    def showPage(self):
        self.show()
    def createButton(self, name:str, x = None, y = None):
        button = QPushButton(name, self)
        button.click()
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
    def createHeader(self, centerName:str, width: int, x = None, y = None):
        layout = QVBoxLayout()
        headerWidget = QFrame(self)
        headerTitle = QLabel('<h2>' + centerName + '</h2>')
        headerTitle.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(headerTitle)
        headerWidget.setFixedSize(width, 50) # Jeder der die Zahlen hier verändert ist eine Entäuschung
        headerWidget.setLayout(layout)
        if x != None and y != None:
            headerWidget.move(x, y)

        return headerWidget
    def createSidepanel(self):
        layout = QHBoxLayout()
        sidePanelWidget = QFrame(self)
        sidePanelWidget.setFixedSize(200, 600)
        sidePanelWidget.setLayout(layout)
        return sidePanelWidget


    def createTitle(self, name:str,x = None, y = None):
        label = QLabel('<h1>' + name + '</h1>')
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        if x != None and y != None:
            label.move(x, y)

        return label
    def createTable(self, tableHeaders: list, x = None, y = None):
        table = QTableWidget(self)
        table.setColumnCount(len(tableHeaders))
        table.setFixedSize(800,550)
        table.resizeColumnToContents(len(tableHeaders))
        table.setHorizontalHeaderLabels(tableHeaders)
        if x != None and y != None:
            table.move(x, y)


        return table