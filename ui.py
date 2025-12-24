from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from loginpage import LoginPage
from mainpage import MainPage
from adminpage import AdminPage

class UI():
    fLoginPage:LoginPage
    fMainPage: MainPage
    fAdminPage: AdminPage
    def __init__(self):
        super().__init__()
        self.fMainPage = MainPage()
        self.fLoginPage = LoginPage()
        self.fAdminPage = AdminPage()

    def showStandardPage(self):
        self.fMainPage.show()
    def showLoginPage(self):
        self.fLoginPage.show()
        return
        #TODO: Login Fehler einfügen
    def showAdminPage(self):
        self.fAdminPage.show()
    def hideAdminPage(self):
        self.fAdminPage.hide()
    def showInventoryPage(page):
        page = page
    def hideStandardPage(self):
        self.fMainPage.hide()
    def hideLoginPage(self):
        self.fLoginPage.hide()
        return
        #TODO: Login Fehler einfügen
    def hideAdminPage(page):
        page = page
    def hideInventoryPage(page):
        page = page
