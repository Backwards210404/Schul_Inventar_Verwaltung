from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from loginpage import LoginPage

class UI():
    fLoginPage:LoginPage
    def __init__(self):
        super().__init__()
        self.fLoginPage = LoginPage()


    def showStandardPage(page):
        page = page
    def showLoginPage(self):
        self.fLoginPage.show()
    def showAdminPage(page):
        page = page
    def showInventoryPage(page):
        page = page
