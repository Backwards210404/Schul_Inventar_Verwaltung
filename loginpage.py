from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor, QPalette

class LoginPage(Page):
    fLoginButton:QPushButton
    fUserName: QLineEdit
    fPassword: QLineEdit
    fVLayout: QVBoxLayout
    fTitle: QLabel
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.createInputWidgets()
        self.createLayoutWithWidgets()
    def createInputWidgets(self):
        self.fUserName = self.createInput('Benutzername')
        self.fPassword = self.createInput('Passwort')
        self.fLoginButton = self.createButton('Anmelden')
        self.fTitle = self.createText("Willkommen!")
    def createLayoutWithWidgets(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.fVLayout = QVBoxLayout()
        widgets = [
            self.fTitle,
            self.fUserName,
            self.fPassword,
            self.fLoginButton,
        ]
        for widget in widgets:
            self.fVLayout.addWidget(widget)
        centralWidget.setContentsMargins(350, 150, 350, 200)
        centralWidget.setLayout(self.fVLayout)
    