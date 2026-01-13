from page import Page
from PyQt6.QtWidgets import *

class AdminPage(Page):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel: QFrame
    fHeaderButton: QPushButton
    fTable: QTableWidget
    fNewEntryButton: QPushButton
    fAddItemButton: QPushButton
    fRemoveItemButton: QPushButton
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Admin')
        self.styleSheet()
    def createInputWidgets(self):
        self.fHeaderButton = self.createButton('Logout', 850, 6)

    def createMainWidgets(self):
        self.fTable = self.createTable(['Vorname', 'Nachname', 'Nutzername', 'Rolle', 'Löschen'],x = 0, y = 50)
        self.fHeader = self.createHeader(
        'Admin Seite',
        width = 1000,
        )
        self.fAddItemButton = self.createButton('+', self.width - 80, self.height - 80)
        self.fAddItemButton.setFixedSize(60, 60)

    def styleSheet(self):
        styleSheet = open('./stylesheets/admin.css').read()
        self.setStyleSheet(styleSheet)

    