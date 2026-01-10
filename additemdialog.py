from PyQt6.QtWidgets import *
from item import Item

class AddItemDialog(QDialog):
    fGroupInput: QLineEdit
    fDepartmentInput: QLineEdit
    fSubjectInput: QLineEdit
    fLocationInput: QLineEdit
    fResponsiblePersonInput: QLineEdit
    fSaveButton: QPushButton
    item: Item | None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Neues Item hinzufügen')
        self.setFixedSize(400, 300)
        self.item = None
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

        self.fResponsiblePersonInput = QLineEdit()
        self.fResponsiblePersonInput.setPlaceholderText('Verantwortlicher')

        self.fSaveButton = QPushButton('Speichern')
        self.fSaveButton.clicked.connect(self.onSave)

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
        layout.addWidget(QLabel('Verantwortlicher:'))
        layout.addWidget(self.fResponsiblePersonInput)
        layout.addWidget(self.fSaveButton)

        self.setLayout(layout)

    def onSave(self):
        group = self.fGroupInput.text()
        department = self.fDepartmentInput.text()
        subject = self.fSubjectInput.text()
        location = self.fLocationInput.text()
        responsiblePerson = self.fResponsiblePersonInput.text()

        if not (group and department and subject and location and responsiblePerson):
            return

        self.item = Item(group, department, subject, location, responsiblePerson)
        self.accept()

    def getItem(self) -> Item | None:
        return self.item
