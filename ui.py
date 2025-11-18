from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Hello, world!'
        self.left = 1000
        self.top = 1000
        self.width = 1000
        self.height = 1000

    def showStandardPage(page):
        page = page
    def showLoginPage(self):
        self.setWindowTitle('Login')
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QVBoxLayout()
        InputUserName = QLineEdit(self)
        InputUserName.setPlaceholderText('Benutzer Name')
        InputUserName.move(400, 400)
        InputUserName.resize(280, 40)

        InputPassword = QLineEdit(self)
        InputPassword.setPlaceholderText('Passwort')
        InputPassword.move(400, 500)
        InputPassword.resize(280, 40)

        # Button
        InputLoginButton = QPushButton('Anmelden', self)
        InputLoginButton.move(400, 600)

        layout.addWidget(InputUserName)
        layout.addWidget(InputPassword)
        layout.addWidget(InputLoginButton)

        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        self.show()
    def showAdminPage(page):
        page = page
    def showInventoryPage(page):
        page = page

app = QApplication(sys.argv)
ui = UI()
ui.showLoginPage()
sys.exit(app.exec())