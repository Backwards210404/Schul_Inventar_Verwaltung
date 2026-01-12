from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

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
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main')
        self.createInputWidgets()
        self.createMainWidgets()
    def createInputWidgets(self):
        self.fHeaderButton = self.createButton('Logout', 850, 6)
        self.fExportButton = self.createButton('Export in CSV', 250, 6)
        self.fAddItemButton = self.createButton('+', self.width - 80, self.height - 80)
        self.fAddItemButton.setFixedSize(60, 60)

    def createMainWidgets(self):
        distanceSidePanel = 200
        tableHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher', 'Zustand', 'Löschen']
        filterHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher', 'Zustand']
        personTypeList = ['Schüler', 'Lehrer', 'Admin']
        stateList = ['Gebraucht', 'In Reparatur', 'Bestellt', 'Ausgemustert', 'Verliehen', 'Geliefert', 'Geplant', 'Angefordert']

        self.fTable = self.createTable(tableHeaders ,x = distanceSidePanel, y = 50, width = 850)
        self.fTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.fHeader = self.createHeader(
        'Inventutator 2000 Pro Max Ultra Power Edition',
        width = self.width - distanceSidePanel,
        x = distanceSidePanel, y = 0
        )

        self.fSidePanel = self.createSidepanel()
        filterWidget = self.createFilterWidget(filterHeaders, personTypeList,  stateList, True)
        filterWidget.move(0, 200)
        self.fFilterDropDown.currentIndexChanged.connect(self.filterIndexChanged)

        self.fHeaderButton.raise_()
        self.fExportButton.raise_()
        self.fAddItemButton.raise_()
        

    def createFilterWidget(self, filterHeaders: list, personTypeList: list, stateList: list, isFirstTime: bool):
        filterWidget = QWidget(self)
        vLayout = QVBoxLayout()

        filterLabel = self.createText('Suche Nach')
        filterLabel.setMinimumHeight(20)
        if(isFirstTime):
            self.fFilterDropDown = self.createDropDownMenu(filterHeaders)
            self.fFilterDropDown.setEditable(True)
            self.fFilterDropDown.lineEdit().setReadOnly(True)
            self.fFilterDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.fFilterDropDown.setMinimumHeight(22)

        self.fFilterButton = self.createButton('Suchen')
        self.fFilterButton.setMinimumHeight(22)
        filterSelected = self.fFilterDropDown.currentText()


        vLayout.addWidget(filterLabel)
        vLayout.addWidget(self.fFilterDropDown)
        if (filterSelected == 'Verantworlicher'):
            self.fTypePersonDropDown = self.createDropDownMenu(personTypeList)
            self.fTypePersonDropDown.setEditable(True)
            self.fTypePersonDropDown.lineEdit().setReadOnly(True)
            self.fTypePersonDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.fTypePersonDropDown.setMinimumHeight(22)
            vLayout.addWidget(self.fTypePersonDropDown)
        elif (filterSelected == 'Zustand'):
            self.fStateDropDown = self.createDropDownMenu(stateList)
            self.fStateDropDown.setEditable(True)
            self.fStateDropDown.lineEdit().setReadOnly(True)
            self.fStateDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.fStateDropDown.setMinimumHeight(22)
            vLayout.addWidget(self.fStateDropDown)
        else:
            self.fFilterInput = self.createInput('Bitte gib das Wort hier ein')
            self.fFilterInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.fFilterInput.setMinimumHeight(20)
            vLayout.addWidget(self.fFilterInput)
        vLayout.addWidget(self.fFilterInput)
        vLayout.addWidget(self.fFilterButton)
        vLayout.setContentsMargins(0,0,0,0)
        vLayout.setSpacing(5)

        filterWidget.setLayout(vLayout)
        filterWidget.setFixedSize(200,100)

        return filterWidget
    def filterIndexChanged(self):
        filterHeaders = ['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher', 'Zustand']
        personTypeList = ['Schüler', 'Lehrer', 'Admin']
        stateList = ['Gebraucht', 'In Reparatur', 'Bestellt', 'Ausgemustert', 'Verliehen', 'Geliefert', 'Geplant', 'Angefordert']
        self.fFilterWidget = self.createFilterWidget(filterHeaders, personTypeList,  stateList, False)

    def styleSheet(self):
        self.fSidePanel.setStyleSheet('background: Gainsboro')
        self.fHeader.setStyleSheet('background: grey')
    