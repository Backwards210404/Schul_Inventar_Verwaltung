from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from loginpage import LoginPage
from mainpage import MainPage
from adminUserpage import AdminUserPage

class UI():
    fLoginPage: LoginPage
    fMainPage: MainPage
    fAdminUserPage: AdminUserPage
    def __init__(self):
        super().__init__()
        self.fMainPage = MainPage()
        self.fLoginPage = LoginPage()
        self.fAdminUserPage = AdminUserPage()


    def showAdminUserPage(self):
        self.fAdminUserPage.showPage()
    def hideAdminPage(self):
        self.fAdminUserPage.hide()
    def showInventoryPage(self):
        self.fMainPage.showPage()
    def hideInventoryPage(self):
        self.fMainPage.hide()
    def hideLoginPage(self):
        self.fLoginPage.hide()
    def showLoginPage(self):
        self.fLoginPage.showPage()

