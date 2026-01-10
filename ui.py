from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from loginpage import LoginPage
from mainpage import MainPage
from adminpage import AdminPage

class UI():
    fLoginPage: LoginPage
    fMainPage: MainPage
    fAdminPage: AdminPage
    def __init__(self):
        super().__init__()
        self.fMainPage = MainPage()
        self.fLoginPage = LoginPage()
        self.fAdminPage = AdminPage()


    def showLoginPage(self):
        self.fLoginPage.show()
        return
    def showAdminPage(self):
        self.fAdminPage.show()
    def hideAdminPage(self):
        self.fAdminPage.hide()
    def showInventoryPage(self):
        self.fMainPage.show()
    def hideInventoryPage(self):
        self.fMainPage.hide()
    def hideLoginPage(self):
        self.fLoginPage.hide()
    def showLoginPage(self):
        self.fLoginPage.show()

