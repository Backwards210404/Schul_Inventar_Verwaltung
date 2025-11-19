from page import Page
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor, QPalette

class LoginPage(Page):
    fLoginButton:QPushButton
    fUserName: QLineEdit
    fPassword: QLineEdit
    fLayout: QVBoxLayout
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.createInputWidgets()
        self.createLayoutWithWidgets()

    def createLayoutWithWidgets(self):
        self.fLayout = QVBoxLayout()
        self.setAutoFillBackground(True)
        widgets = [
            self.fLoginButton,
            self.fUserName,
            self.fPassword
        ]
        for widget in widgets:
            self.fLayout.addWidget(widget)
    def createInputWidgets(self):
        self.fLoginButton = self.createButton('Anmelden',0,100)
        self.fUserName = self.createInput('Benutzername',0,200)
        self.fPassword = self.createInput('Passwort',0,300)
    