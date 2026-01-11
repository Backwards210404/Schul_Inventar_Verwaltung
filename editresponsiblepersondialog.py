from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDialog, QComboBox, QPushButton, QVBoxLayout

from item import Item
from user import User


class EditResponsiblePersonDialog(QDialog):
    fInfoLabel: QLabel
    fResponsibleDropDown: QComboBox
    fSaveButton: QPushButton
    def __init__(self, item: Item, users: list[User], parent=None):
        super().__init__(parent)
        self.setWindowTitle('Verantwortlichen ändern')
        self.setFixedSize(300, 250)
        self.item = item
        self.users = users

        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        self.fInfoLabel = QLabel(f"<b>Fach:</b> {self.item.subject}")
        self.fInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fResponsibleDropDown = QComboBox()

        for user in self.users:
            self.fResponsibleDropDown.addItem(user.userName)

        current_name = self.item.responsiblePerson.userName if isinstance(self.item.responsiblePerson,
                                                                          User) else self.item.responsiblePerson
        self.fResponsibleDropDown.setCurrentText(current_name)

        self.fSaveButton = QPushButton('Zuweisung speichern')
        self.fSaveButton.clicked.connect(self.onSave)

    def createLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.fInfoLabel)
        layout.addWidget(QLabel('Verantwortliche Person:'))
        layout.addWidget(self.fResponsibleDropDown)
        layout.addStretch()
        layout.addWidget(self.fSaveButton)
        self.setLayout(layout)

    def onSave(self):

        if self.fResponsibleDropDown.currentText():
            for user in self.users:
                if user.userName == self.fResponsibleDropDown.currentText():
                    self.item.responsiblePerson = user

        self.accept()