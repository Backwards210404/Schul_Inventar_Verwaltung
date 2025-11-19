from item import Item
from model import Model
from ui import UI
from user import User


class UIController:

    items: list[Item]
    ui: UI
    model: Model
    
    def __init__(self):
        self.ui = UI()
        self.model = Model()
        self.ui.showLoginPage()
        self.initClickEvents()
    def refreshItems(self): 
        self.items = self.model.load()
    def onLogin(self):
        username = self.ui.fLoginPage.fUserName.text()
        password = self.ui.fLoginPage.fPassword.text()
        if(password.__len__() > 0 and username.__len__() > 0):
            user = self.model.login(username, hash(password))
            null = null
            if(not isinstance(user, User)):
                self.ui.showError('login')
                return
            if(user.getRole() == 'admin'):
                self.ui.showAdminPage()
            else:
                self.ui.showInventoryPage()
    def initClickEvents(self):
        self.ui.fLoginPage.fLoginButton.clicked.connect(self.onLogin)
    def onFilterSelected(self):
        # todo
        self = self
