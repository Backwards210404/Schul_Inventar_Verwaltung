from item import Item
from model import Model
from ui import UI
from user import User
from additemdialog import AddItemDialog
from PyQt6.QtWidgets import *
import hashlib

class UIController:

    items: list[Item]
    users: list[User]
    ui: UI
    model: Model

    def __init__(self):
        self.ui = UI()
        self.model = Model()
        self.ui.showLoginPage()
        self.initLoginPageEvents()
        self.createAcc()

    def hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def createAcc(self):
        self.model.addUser(User('b','d','a', self.hashPassword('admin'), 'admin'))

    def refreshItems(self):
        self.model.load()
        self.items = self.model.items
    def refreshUsers(self):
        self.model.load()
        self.users = self.model.users
    def onLogin(self):
        username = self.ui.fLoginPage.fUserName.text()
        password = self.ui.fLoginPage.fPassword.text()
        if(password.__len__() > 0 and username.__len__() > 0):
            user = self.model.login(username, self.hashPassword(password))
            if(not isinstance(user, User)):
                self.showLoginError()
                return
            if(user.getRole() == 'admin'):
                self.ui.hideLoginPage()
                self.ui.showAdminPage()
                self.initAdminPageEvents()
            else:
                self.ui.hideLoginPage()
                self.ui.showInventoryPage()
                self.initInventoryPageEvents()

    def showLoginError(self):
        errorDialog = QMessageBox(self.ui.fLoginPage)
        errorDialog.setIcon(QMessageBox.Icon.Warning)
        errorDialog.setWindowTitle('Login Fehler')
        errorDialog.setText('Falscher Benutzername oder Passwort!')
        errorDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        errorDialog.exec()

    def initLoginPageEvents(self):
        self.ui.fLoginPage.fLoginButton.clicked.connect(self.onLogin)
        self.ui.fLoginPage.fPassword.returnPressed.connect(self.onLogin)

    def initAdminPageEvents(self):
        self.ui.fAdminPage.fHeaderButton.clicked.connect(self.onLogout)
        self.refreshUsers()
        self.loadUserTableData()

    def initInventoryPageEvents(self):
        self.ui.fMainPage.fAddItemButton.clicked.connect(self.onAddItem)
        self.ui.fMainPage.fFilterButton.clicked.connect(self.onSearchInLoginTable)
        self.ui.fMainPage.fHeaderButton.clicked.connect(self.onLogout)
        self.refreshItems()
        self.loadItemTableData()

    def onAddItem(self):
        dialog = AddItemDialog(self.ui.fMainPage)
        if dialog.exec():
            item = dialog.getItem()
            if item:
                self.model.addItem(item)
                self.model.save()
                self.addToTable(item)

    def addToTable(self, item):
        table = self.ui.fMainPage.fTable
        rowCount = table.rowCount()
        table.insertRow(rowCount)
        table.setItem(rowCount, 0, QTableWidgetItem(item.group))
        table.setItem(rowCount, 1, QTableWidgetItem(item.department))
        table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
        table.setItem(rowCount, 3, QTableWidgetItem(item.location))
        table.setItem(rowCount, 4, QTableWidgetItem(item.responsiblePerson))
    def onSearchInLoginTable(self):
        attribute = self.ui.fMainPage.fFilterDropDown.currentText()
        searchText = self.ui.fMainPage.fFilterInput.text().lower()

        if not searchText:
            self.loadTableData()
            return

        attributeMap = {
            'Gruppe': 'group',
            'Abteilung': 'department',
            'Fach': 'subject',
            'Ort': 'location',
            'Verantworlicher': 'responsiblePerson'
        }

        table = self.ui.fMainPage.fTable
        table.setRowCount(0)

        for item in self.items:
            itemAttribute = attributeMap.get(attribute)
            if itemAttribute:
                itemValue = getattr(item, itemAttribute, '').lower()
                if searchText in itemValue:
                    rowCount = table.rowCount()
                    table.insertRow(rowCount)
                    table.setItem(rowCount, 0, QTableWidgetItem(item.group))
                    table.setItem(rowCount, 1, QTableWidgetItem(item.department))
                    table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
                    table.setItem(rowCount, 3, QTableWidgetItem(item.location))
                    table.setItem(rowCount, 4, QTableWidgetItem(item.responsiblePerson))

    def loadItemTableData(self):
        for item in self.items:
            table = self.ui.fMainPage.fTable
            table.setRowCount(0)
            rowCount = table.rowCount()
            table.insertRow(rowCount)
            table.setItem(rowCount, 0, QTableWidgetItem(item.group))
            table.setItem(rowCount, 1, QTableWidgetItem(item.department))
            table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
            table.setItem(rowCount, 3, QTableWidgetItem(item.location))
            table.setItem(rowCount, 4, QTableWidgetItem(item.responsiblePerson))

    def loadUserTableData(self):
        for user in self.users:
            table = self.ui.fAdminPage.fTable
            table.setRowCount(0)
            rowCount = table.rowCount()
            table.insertRow(rowCount)
            table.insertRow(rowCount)
            table.setItem(rowCount, 0, QTableWidgetItem(user.firstName))
            table.setItem(rowCount, 1, QTableWidgetItem(user.lastName))
            table.setItem(rowCount, 2, QTableWidgetItem(user.userName))
            table.setItem(rowCount, 3, QTableWidgetItem(user.role))
    def onLogout(self):
        self.ui.hideInventoryPage()
        self.ui.hideAdminPage()
        self.ui.fLoginPage.fUserName.clear()
        self.ui.fLoginPage.fPassword.clear()
        self.ui.showLoginPage()

