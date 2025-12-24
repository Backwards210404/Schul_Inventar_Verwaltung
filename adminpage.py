from page import Page
from PyQt6.QtWidgets import *

class AdminPage(Page):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel = QFrame
    fHeaderButton = QPushButton
    fTable = QTableWidget
    fNewEntryButtton = QPushButton
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin')
        self.createInputWidgets()
        self.createMainWidgets()
    def createInputWidgets(self):
        self.fHeaderButton = self.createButton('Logout', 850, 6)

    def createMainWidgets(self):
        self.fTable = self.createTable(['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher'],x = 0, y = 50)
        self.fHeader = self.createHeader(
        'Admin Seite',
        width = 1000,
        )
        self.fNewEntryButtton = self.createButton('+', self.width - 100, self.height - 100)
        self.fNewEntryButtton.setFixedSize(75, 75)
        self.fNewEntryButtton.setStyleSheet("""
        QPushButton {
            border-radius: 35px;
            background-color: #3498db;
            color: white;
            border: 2px solid #2980b9;  
            font-size: 30px;
            text-align: center;                                     
        }
        QPushButton:hover {
            background-color: transparent;
            border: 1px solid black;
            color: black;                                
        }
        """)

    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')

    