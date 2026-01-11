from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from user import User
from userrole import UserRole


class AddUserDialog(QDialog):
    fFirstNameInput: QLineEdit
    fLastNameInput: QLineEdit
    fUserNameInput: QLineEdit
    fPasswordInput: QLineEdit
    fRoleDropDown: QComboBox
    fSaveButton: QPushButton
    user: User | None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Neuen Benutzer hinzufügen')
        self.setFixedSize(400, 400)
        self.user = None

        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        self.fFirstNameInput = QLineEdit()
        self.fFirstNameInput.setPlaceholderText('Vorname')

        self.fLastNameInput = QLineEdit()
        self.fLastNameInput.setPlaceholderText('Nachname')

        self.fUserNameInput = QLineEdit()
        self.fUserNameInput.setPlaceholderText('Benutzername')

        self.fPasswordInput = QLineEdit()
        self.fPasswordInput.setPlaceholderText('Passwort')
        self.fPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.fRoleDropDown = QComboBox()
        self.fRoleDropDown.addItems([UserRole.RESPONSIBLE.value,UserRole.ADMIN.value,UserRole.TEACHER.value])
        self.fRoleDropDown.setEditable(True)
        self.fRoleDropDown.lineEdit().setReadOnly(True)
        self.fRoleDropDown.lineEdit().setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.fSaveButton = QPushButton('Benutzer speichern')
        self.fSaveButton.clicked.connect(self.onSave)

    def createLayout(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Vorname:'))
        layout.addWidget(self.fFirstNameInput)

        layout.addWidget(QLabel('Nachname:'))
        layout.addWidget(self.fLastNameInput)

        layout.addWidget(QLabel('Benutzername:'))
        layout.addWidget(self.fUserNameInput)

        layout.addWidget(QLabel('Passwort:'))
        layout.addWidget(self.fPasswordInput)

        layout.addWidget(QLabel('Rolle:'))
        layout.addWidget(self.fRoleDropDown)

        layout.addSpacing(10)
        layout.addWidget(self.fSaveButton)

        self.setLayout(layout)

    def onSave(self):
        firstName = self.fFirstNameInput.text()
        lastName = self.fLastNameInput.text()
        userName = self.fUserNameInput.text()
        password = self.fPasswordInput.text()
        role = self.fRoleDropDown.currentText()

        if not (firstName and lastName and userName and password and role):
            QMessageBox.warning(self, "Eingabefehler", "Bitte alle Felder ausfüllen!")
            return

        self.user = User(
            firstName=firstName,
            lastName=lastName,
            userName=userName,
            password=password,
            role=role
        )
        self.accept()

    def getUser(self) -> User | None:
        return self.user