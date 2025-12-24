from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

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
        self.fHeaderButton = self.createButton('Logout', 850, 6)

    def createMainWidgets(self):
        distanceSidePanel = 200
        tableHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher']
    
        self.fTable = self.createTable(tableHeaders ,x = distanceSidePanel, y = 50, width = 850)
    
        self.fHeader = self.createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        x = distanceSidePanel, y = 0
        )

        self.fSidePanel = self.createSidepanel()
        filterWidget = self.createFilterWidget(tableHeaders)
        filterWidget.move(0, 200)
        

    def createFilterWidget(self, tableHeaders: list):
        filterWidget = QWidget(self)
        vLayout = QVBoxLayout()

        filterLabel = self.createText('Suche Nach')
        filterLabel.setMinimumHeight(20)

        filterDropDownMenu = self.createDropDownMenu(tableHeaders)
        filterDropDownMenu.setEditable(True)
        filterDropDownMenu.lineEdit().setReadOnly(True)
        filterDropDownMenu.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
        filterDropDownMenu.setMinimumHeight(22)

        filterButton = self.createButton('Suchen')
        filterButton.setMinimumHeight(22)

        filterWord = self.createInput('Bitte gib das Wort hier ein')
        filterWord.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        filterWord.setMinimumHeight(20)

        vLayout.addWidget(filterLabel)
        vLayout.addWidget(filterDropDownMenu)
        vLayout.addWidget(filterWord)
        vLayout.addWidget(filterButton)
        vLayout.setContentsMargins(0,0,0,0)
        vLayout.setSpacing(5)

        filterWidget.setLayout(vLayout)
        filterWidget.setFixedSize(200,100)

        return filterWidget


    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')
    