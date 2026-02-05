from PyQt6.uic.properties import QtGui

from page import Page
from PyQt6.QtWidgets import *

class LoginPage(Page):
    fLoginButton:QPushButton
    fUserName: QLineEdit
    fPassword: QLineEdit
    fVLayout: QVBoxLayout
    fTitle: QLabel
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.styleSheet()
    def createInputWidgets(self):
        self.fUserName = self.createInput('Benutzername')
        self.fPassword = self.createInput('Passwort')
        self.fPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.fLoginButton = self.createButton('Anmelden')
        self.fTitle = self.createTitle('Willkommen!')

    def createMainWidgets(self):
        centralWidget = QWidget()
        self.fUserName.setProperty('class', 'loginElements')
        self.fPassword.setProperty('class', 'loginElements')
        self.fLoginButton.setProperty('class', 'loginElements')

        centralWidget.setProperty('class', 'loginPage')

        self.fVLayout = QVBoxLayout()
        self.fVLayout.setProperty('class', 'VLayout')
        centralWidget.setMinimumWidth(500)
        centralWidget.setMinimumHeight(300)
        widgets = [
            self.fTitle,
            self.fUserName,
            self.fPassword,
            self.fLoginButton,
        ]
        for widget in widgets:
            widget.setMinimumHeight(40)
            widget.setMinimumWidth(300)
            self.fVLayout.addWidget(widget)
        self.fVLayout.addStretch(1)
        centralWidget.setContentsMargins(350, 150, 350, 200)
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.fVLayout)
    def styleSheet(self):
        styleSheet = open('./stylesheets/login.css').read()
        self.setStyleSheet(styleSheet)
    