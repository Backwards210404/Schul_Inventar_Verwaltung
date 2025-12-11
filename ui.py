from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from loginpage import LoginPage
from mainpage import MainPage

class UI():
    fLoginPage:LoginPage
    fMainPage: MainPage
    def __init__(self):
        super().__init__()
        self.fMainPage = MainPage()
        self.fLoginPage = LoginPage()
    def showStandardPage(self):
        self.fMainPage.show()
    def showLoginPage(self):
        self.fLoginPage.show()
        return
        #TODO: Login Fehler einfügen
    def showAdminPage(page):
        page = page
    def showInventoryPage(page):
        page = page
