from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import ItemState
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
        states = [ItemState.ItemState.USED,
                  ItemState.ItemState.FIXING,
                  ItemState.ItemState.ORDERED,
                  ItemState.ItemState.RETIRED,
                  ItemState.ItemState.BORROWED,
                  ItemState.ItemState.DELIVERED,
                  ItemState.ItemState.PROJECTED,
                  ItemState.ItemState.REQUESTED]

        for s in states:
            self.fStateDropDown.addItem(s.value)

        self.fStateDropDown.setCurrentText(self.item.state.value)

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
        self.item.state = ItemState.normalizeText(self.fStateDropDown.currentData())
        self.accept()

    def getItem(self) -> Item:
        return self.item