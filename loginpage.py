from page import Page
from PyQt6.QtWidgets import *

class LoginPage(Page):
    fLoginButton:QPushButton
    fUserName: QLineEdit
    fPassword: QLineEdit
    fLayout: QVBoxLayout
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.fLoginButton = self.createButton('Anmelden',500,400)
        self.fUserName = self.createInput('Benutzername',500,500)
        self.fPassword = self.createInput('Passwort',500,600)
        self.fLayout = QVBoxLayout()
    