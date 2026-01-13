from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from userrole import UserRole


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
    fFilterButton: QPushButton
    fStateDropDown: QComboBox
    fTypePersonDropDown: QComboBox
    fFilterWidget = QWidget
    fVLayout = QVBoxLayout
    tableHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', UserRole.RESPONSIBLE.value, 'Zustand', 'Löschen']
    filterHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', UserRole.RESPONSIBLE.value, 'Zustand']
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

        personTypeList = ['Schüler', 'Lehrer', 'Admin']

        stateList = ['Gebraucht', 'In Reparatur', 'Bestellt', 'Ausgemustert', 'Verliehen', 'Geliefert', 'Geplant', 'Angefordert']

        self.fTable = self.createTable(self.tableHeaders ,x = distanceSidePanel, y = 50, width = 850)
        self.fTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fHeader = self.createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        x = distanceSidePanel, y = 0
        )

        self.fSidePanel = self.createSidepanel()
        self.fFilterWidget = self.createDropDownFilterWidget(self.filterHeaders, personTypeList,  stateList, True)
        self.fFilterWidget.move(0, 200)
        self.fFilterDropDown.currentIndexChanged.connect(self.filterIndexChanged)

        self.fHeaderButton.raise_()
        self.fExportButton.raise_()
        self.fAddItemButton.raise_()
        

    def createDropDownFilterWidget(self, filterHeaders: list, personTypeList: list, stateList: list, isFirstTime: bool):
        filterWidget = QWidget(self)

        filterLabel = self.createText('Suche:')
        filterLabel.setMinimumHeight(20)
        filterSelected = ""
        if not isFirstTime:
            filterSelected = self.fFilterDropDown.currentText()
        self.fFilterDropDown = self.createDropDownMenu(filterHeaders)
        self.fFilterButton = self.createButton('Suchen')
        self.fFilterButton.setMinimumHeight(22)
        

        self.fVLayout.addWidget(filterLabel)
        self.fVLayout.addWidget(self.fFilterDropDown)

        self.fVLayout.addWidget(self.fFilterButton)
        self.fVLayout.setContentsMargins(0,0,0,0)
        self.fVLayout.setSpacing(5)

        filterWidget.setLayout(self.fVLayout)
        filterWidget.setFixedSize(200,100)

        return filterWidget
    def createInputOrDropdown(self, filterSelected, personTypeList, stateList):
        if filterSelected == UserRole.RESPONSIBLE.value:
            self.fTypePersonDropDown = self.createDropDownMenu(personTypeList)
            self.fVLayout.addWidget(self.fTypePersonDropDown)
        elif filterSelected == 'Zustand':
            self.fStateDropDown = self.createDropDownMenu(stateList)
            self.fVLayout.addWidget(self.fStateDropDown)
        else:
            self.fFilterInput = self.createInput('Hier eingeben')
            self.fFilterInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.fFilterInput.setMinimumHeight(20)
            self.fVLayout.addWidget(self.fFilterInput)
    def filterIndexChanged(self):
        personTypeList = [UserRole.RESPONSIBLE.value, UserRole.TEACHER.value, UserRole.ADMIN.value]
        stateList = ['Gebraucht', 'In Reparatur', 'Bestellt', 'Ausgemustert', 'Verliehen', 'Geliefert', 'Geplant', 'Angefordert']
        #ItemState enum benutzen
        self.fFilterWidget = self.createDropDownFilterWidget(self.filterHeaders, personTypeList,  stateList, False)
        self.fFilterWidget.move(0, 200)
        self.fFilterWidget.show()
        self.fFilterDropDown.currentIndexChanged.connect(self.filterIndexChanged)

    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')
    