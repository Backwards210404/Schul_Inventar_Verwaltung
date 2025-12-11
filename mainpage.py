from page import Page
from PyQt6.QtWidgets import *

class MainPage(Page):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel = QFrame
    fHeaderButton = QPushButton
    fTable = QTableWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main')
        self.createInputWidgets()
        self.createMainWidgets()
    def createInputWidgets(self):
        self.fHeaderButton = self.createButton('L', 850, 6)

    def createMainWidgets(self):
        distanceSidePanel = 200 
        self.fTable = self.createTable(['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher'],x = distanceSidePanel, y = 50)
        self.fHeader = self.createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        x = distanceSidePanel, y = 0
        )
        self.fSidePanel = self.createSidepanel()

    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')
    