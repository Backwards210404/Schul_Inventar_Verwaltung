from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QDialog, QComboBox, QPushButton, QVBoxLayout
from user import User
from userrole import UserRole, normalizeRoleText


class EditUserRoleDialog(QDialog):
    fInfoLabel:QLabel
    fRoleDropDown:QComboBox
    fSaveButton:QPushButton
    user:User
    def __init__(self, user: User, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Benutzerrolle ändern')
        self.setFixedSize(300, 250)
        self.user = user

        self.available_roles = [UserRole.RESPONSIBLE.value, UserRole.ADMIN.value, UserRole.TEACHER.value]

        self.createWidgets()
        self.createLayout()

    def createWidgets(self):
        self.fInfoLabel = QLabel(f"<b>Benutzer:</b> {self.user.userName}<br>"
                                 f"<b>Name:</b> {self.user.firstName} {self.user.lastName}")
        self.fInfoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fRoleDropDown = QComboBox()
        self.fRoleDropDown.addItems(self.available_roles)

        self.fRoleDropDown.setCurrentText(self.user.role.value)

        self.fSaveButton = QPushButton('Rolle speichern')
        self.fSaveButton.clicked.connect(self.onSave)

    def createLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.fInfoLabel)
        layout.addSpacing(10)
        layout.addWidget(QLabel('Neue Rolle zuweisen:'))
        layout.addWidget(self.fRoleDropDown)
        layout.addStretch()
        layout.addWidget(self.fSaveButton)
        self.setLayout(layout)

    def onSave(self):
        self.user.role = normalizeRoleText(self.fRoleDropDown.currentText())
        self.accept()