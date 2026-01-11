from PyQt6.QtWidgets import *

import ItemState
from ItemState import normalizeText
from item import Item
from PyQt6.QtCore import Qt

from user import User


class AddItemDialog(QDialog):
    fGroupInput: QLineEdit
    fDepartmentInput: QLineEdit
    fSubjectInput: QLineEdit
    fLocationInput: QLineEdit
    fResponsiblePersonDropDown: QComboBox
    fSaveButton: QPushButton
    fStateDropDown: QComboBox
    item: Item | None
    users: list[User]
    def __init__(self,users: list[User], parent=None ):
        super().__init__(parent)
        self.setWindowTitle('Neues Item hinzufügen')
        self.setFixedSize(400, 450)
        self.item = None
        self.users = users
        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        self.fGroupInput = QLineEdit()
        self.fGroupInput.setPlaceholderText('Gruppe')

        self.fDepartmentInput = QLineEdit()
        self.fDepartmentInput.setPlaceholderText('Abteilung')

        self.fSubjectInput = QLineEdit()
        self.fSubjectInput.setPlaceholderText('Fach')

        self.fLocationInput = QLineEdit()
        self.fLocationInput.setPlaceholderText('Ort')

        self.fStateDropDown = self.createDropDownMenu(self.getItemStates())
        self.fStateDropDown.setEditable(True)
        self.fStateDropDown.lineEdit().setReadOnly(True)
        self.fStateDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.fStateDropDown.setMinimumHeight(22)

        self.fResponsiblePersonDropDown = self.createDropDownMenu(self.getUserNames())
        self.fResponsiblePersonDropDown.setEditable(True)
        self.fResponsiblePersonDropDown.lineEdit().setReadOnly(True)
        self.fResponsiblePersonDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.fResponsiblePersonDropDown.setMinimumHeight(22)

        self.fSaveButton = QPushButton('Speichern')
        self.fSaveButton.clicked.connect(self.onSave)
    def getUserNames(self):
        names = []
        for user in self.users:
            names.append(user.userName)
        return names

    def getItemStates(self):
        return [ItemState.ItemState.USED,
                ItemState.ItemState.FIXING,
                ItemState.ItemState.ORDERED,
                ItemState.ItemState.RETIRED, ItemState.ItemState.BORROWED,
                ItemState.ItemState.DELIVERED, ItemState.ItemState.PROJECTED,
                ItemState.ItemState.REQUESTED]
    def createDropDownMenu(self, wordList: list):
        dropDownMenu = QComboBox(self)

        for word in wordList:
            if isinstance(word, str):
                dropDownMenu.addItem(word)
            else:
                dropDownMenu.addItem(word.value)

        return dropDownMenu
    def createLayout(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Gruppe:'))
        layout.addWidget(self.fGroupInput)
        layout.addWidget(QLabel('Abteilung:'))
        layout.addWidget(self.fDepartmentInput)
        layout.addWidget(QLabel('Fach:'))
        layout.addWidget(self.fSubjectInput)
        layout.addWidget(QLabel('Ort:'))
        layout.addWidget(self.fLocationInput)
        layout.addWidget(QLabel("Zustand"))
        layout.addWidget(self.fStateDropDown)
        layout.addWidget(QLabel('Verantwortlicher:'))
        layout.addWidget(self.fResponsiblePersonDropDown)
        layout.addWidget(self.fSaveButton)

        self.setLayout(layout)

    def onSave(self):
        group = self.fGroupInput.text()
        department = self.fDepartmentInput.text()
        subject = self.fSubjectInput.text()
        location = self.fLocationInput.text()
        for user in self.users:
            if user.userName == self.fResponsiblePersonDropDown.currentText():
                responsiblePerson = user
        state = self.fStateDropDown.currentText()

        if not (group and department and subject and location and state):
            return

        self.item = Item(group, department, subject, location, responsiblePerson, normalizeText(state))
        self.accept()

    def getItem(self) -> Item | None:
        return self.item
