from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from itemstate import ItemState, normalizeText
from item import Item
from user import User


class EditItemStateDialog(QDialog):
    fSaveButton: QPushButton
    fInfoLabel: QLabel
    fStateDropDown: QComboBox
    def __init__(self, item: Item, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Status bearbeiten')
        self.setFixedSize(300, 250)
        self.item = item

        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        self.fInfoLabel = QLabel(f"<b>Fach:</b> {self.item.subject}<br><b>Ort:</b> {self.item.location}")
        self.fInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fStateDropDown = QComboBox()
        states = [ItemState.USED,
                  ItemState.FIXING,
                  ItemState.ORDERED,
                  ItemState.RETIRED,
                  ItemState.BORROWED,
                  ItemState.DELIVERED,
                  ItemState.PROJECTED,
                  ItemState.REQUESTED]

        for s in states:
            self.fStateDropDown.addItem(s.value)

        self.fStateDropDown.setCurrentText(self.item.state)

        self.fSaveButton = QPushButton('Status aktualisieren')
        self.fSaveButton.clicked.connect(self.onSave)

    def createLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.fInfoLabel)
        layout.addSpacing(20)
        layout.addWidget(QLabel('Neuer Zustand:'))
        layout.addWidget(self.fStateDropDown)
        layout.addStretch()
        layout.addWidget(self.fSaveButton)
        self.setLayout(layout)

    def onSave(self):
        self.item.state = normalizeText(self.fStateDropDown.currentText())
        self.accept()

    def getItem(self) -> Item:
        return self.item