from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from itemheader import ItemHeader
from model import Model

class MainPage(Page):
    fTitle: QLabel
    fHeader: QFrame
    fSidePanel: QFrame
    fHeaderButton: QPushButton
    fExportButton: QPushButton
    fTable: QTableWidget
    fAddItemButton: QPushButton
    fFilterDropDown: QComboBox
    fFilterInput: QLineEdit
    fFilterSearchButton: QPushButton
    fFilterResetButton: QPushButton
    fStateDropDown: QComboBox
    fResponsiblePersonDropDown: QComboBox
    fFilterWidget = QWidget
    fVLayout = QVBoxLayout
    fFilterSelected = ''
    tableHeaders = [ItemHeader.GROUP.value, ItemHeader.DEPARTMENT.value, ItemHeader.SUBJECT.value, ItemHeader.LOCATION.value, ItemHeader.RESPONSIBLE.value, ItemHeader.STATE.value, 'Löschen']
    filterHeaders = [ItemHeader.GROUP.value, ItemHeader.DEPARTMENT.value, ItemHeader.SUBJECT.value, ItemHeader.LOCATION.value, ItemHeader.RESPONSIBLE.value, ItemHeader.STATE.value]
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main')
    def createInputWidgets(self):
        self.fHeaderButton = self.createButton('Logout', 850, 6)
        self.fExportButton = self.createButton('Export in CSV', 250, 6)
        self.fAddItemButton = self.createButton('+', self.width - 80, self.height - 80)
        self.fAddItemButton.setFixedSize(60, 60)
    def createMainWidgets(self):
        self.fVLayout = QVBoxLayout()
        distanceSidePanel = 200

        self.fTable = self.createTable(self.tableHeaders ,x = distanceSidePanel, y = 50, width = 850)
        self.fTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fHeader = self.createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        x = distanceSidePanel, y = 0
        )

        self.fSidePanel = self.createSidepanel()
        self.fFilterWidget = self.createDropDownFilterWidget(self.filterHeaders)
        self.fFilterWidget.move(0, 200)

        self.fHeaderButton.raise_()
        self.fExportButton.raise_()
        self.fAddItemButton.raise_()
        

    def createDropDownFilterWidget(self, filterHeaders: list):
        filterWidget = QWidget(self)

        filterLabel = self.createText('Suche:')
        filterLabel.setMinimumHeight(20)
        self.fFilterDropDown = self.createDropDownMenu(filterHeaders)
        self.fFilterSearchButton = self.createButton('Suchen')
        self.fFilterResetButton = self.createButton('Filter Zurücksetzen')
        self.fFilterSearchButton.setMinimumHeight(22)

        stateList = ['Gebraucht', 'In Reparatur', 'Bestellt', 'Ausgemustert', 'Verliehen', 'Geliefert', 'Geplant', 'Angefordert']
        self.fStateDropDown = self.createDropDownMenu(stateList)
        self.fFilterInput = self.createInput('Hier eingeben.')
        allResponsibles = Model().getAllResponsibiltityUserNames()
        self.fResponsiblePersonDropDown = self.createDropDownMenu(allResponsibles)

        self.fVLayout.addWidget(filterLabel)
        self.fVLayout.addWidget(self.fFilterDropDown)
        self.fVLayout.addWidget(self.fStateDropDown)
        self.fVLayout.addWidget(self.fFilterInput)
        self.fVLayout.addWidget(self.fResponsiblePersonDropDown)
        self.fVLayout.addWidget(self.fFilterSearchButton)
        self.fVLayout.addWidget(self.fFilterResetButton)
        self.fVLayout.setContentsMargins(0,0,0,0)
        self.fVLayout.setSpacing(5)

        filterWidget.setLayout(self.fVLayout)
        filterWidget.setFixedSize(200,130)

        return filterWidget
        

    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')