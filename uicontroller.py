from item import Item
from model import Model
from ui import UI
from user import User
from PyQt6.QtCore import *

class UIController:

    items: list[Item]
    ui: UI
    model: Model
    
    def __init__(self):
        self.ui = UI()
        self.model = Model()
        self.ui.showStandardPage()
        self.initLoginPageEvents()
        # self.createAcc()

    def createAcc(self):
        self.model.addUser(User('first','last','b', hash('b'), 'user'))
    def refreshItems(self): 
        self.model.load()
        self.items = self.model.items

    def onLogin(self):
        username = self.ui.fLoginPage.fUserName.text()
        password = self.ui.fLoginPage.fPassword.text()
        if(password.__len__() > 0 and username.__len__() > 0):
            user = self.model.login(username, hash(password))
            if(not isinstance(user, User)):
                self.ui.showError('login')
                return
            if(user.getRole() == 'admin'):
                self.ui.showAdminPage()
                self.initAdminPageEvents()
            else:
                self.ui.showInventoryPage()
                self.initInventoryPageEvents()

    def initLoginPageEvents(self):
        self.ui.fLoginPage.fLoginButton.clicked.connect(self.onLogin)

    def initAdminPageEvents(self):
        # TODO: Admin page events hier hinzufügen
        pass

    def initInventoryPageEvents(self):
        # TODO: Inventory page events hier hinzufügen
        pass
    def onFilterSelected(self):
        # todo
        self = self
