from PyQt6.QtCore import Qt
from itemstate import normalizeText, normalizeItems
from adduserdialog import AddUserDialog
from editresponsiblepersondialog import EditResponsiblePersonDialog
from editstatedialog import EditItemStateDialog
from edituserroledialog import EditUserRoleDialog
from item import Item
from itemheader import ItemHeader
from model import Model
from ui import UI
from user import User
from additemdialog import AddItemDialog
from PyQt6.QtWidgets import *
import hashlib
import csv

from userrole import UserRole


class UIController:

    items: list[Item]
    users: list[User]
    responsiblePersons: list[User] = []
    ui: UI
    model: Model
    _is_editing: bool
    user: User
    def __init__(self):
        self._is_editing = False
        self.ui = UI()
        self.model = Model()
        self.ui.showLoginPage()
        self.initLoginPageEvents()
        self.createUsers()
        self.refreshUsers()

    def createUsers(self):
        if self.model.users.__len__() > 0:
            return
        self.model.addUser(User('b', 'd', 'b', self.hashPassword('Hallo123#'), UserRole.RESPONSIBLE))
        self.model.addUser(User('b', 'd', 'teacher', self.hashPassword('Hallo123#'), UserRole.TEACHER))
        self.model.addUser(User('b', 'd', 'admin', self.hashPassword('Hallo123#'), UserRole.ADMIN))
        self.model.save()

    def hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()


    def refreshItems(self):
        self.model.load()
        self.items = normalizeItems(self.model.items)

    def refreshUsers(self):
        self.model.load()
        self.users = self.model.users
        self.responsiblePersons = []
        for user in self.users:
            if user.getRole() == UserRole.RESPONSIBLE and not self.responsiblePersons.__contains__(user):
                self.responsiblePersons.append(user)
    def onLogin(self):
        username = self.ui.fLoginPage.fUserName.text()
        password = self.ui.fLoginPage.fPassword.text()
        if password.__len__() > 0 and username.__len__() > 0:
            self.user = self.model.login(username, self.hashPassword(password))
            if not isinstance(self.user, User):
                self.showLoginError()
                return
            if self.user.getRole() == UserRole.ADMIN:
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
        self.ui.fAdminPage.fAddItemButton.clicked.connect(self.onAddUser)
        self.ui.fAdminPage.fHeaderButton.clicked.connect(self.onLogout)
        self.refreshUsers()
        self.loadUserTableData()

        self.ui.fAdminPage.fTable.itemChanged.connect(self.onUserChanged)
        self.ui.fAdminPage.fTable.itemClicked.connect(self.openEditUserRoleDialog)

    def initInventoryPageEvents(self):
        self.selectInputForMainPage()
        self.ui.fMainPage.fFilterDropDown.currentIndexChanged.connect(self.selectInputForMainPage)
        self.ui.fMainPage.fAddItemButton.clicked.connect(self.onAddItem)
        self.ui.fMainPage.fFilterSearchButton.clicked.connect(self.onSearchInItemTable)
        self.ui.fMainPage.fHeaderButton.clicked.connect(self.onLogout)
        self.ui.fMainPage.fExportButton.clicked.connect(self.createCsvExportFile)
        self.refreshItems()
        self.loadItemTableData()
        if self.user.getRole() == UserRole.RESPONSIBLE:
            self.ui.fMainPage.fTable.setEnabled(True)
            self.ui.fMainPage.fAddItemButton.setEnabled(True)
            self.ui.fMainPage.fTable.itemChanged.connect(self.onItemChanged)
            self.ui.fMainPage.fTable.itemClicked.connect(self.handleItemClick)
            self.ui.fMainPage.fTable.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)

        else:
            self.ui.fMainPage.fTable.setEnabled(False)
            self.ui.fMainPage.fAddItemButton.setEnabled(False)

    def noClickEvent(self):
        return

    def onAddItem(self):
        if self._is_editing:
            return

        self._is_editing = True
        try:
            dialog = AddItemDialog(self.responsiblePersons, self.ui.fMainPage)
            if dialog.exec():
                item = dialog.getItem()
                if item:
                    self.model.addItem(item)
                    self.model.save()

                    self.addToTable(item)
        finally:
            self._is_editing = False

    def addToTable(self, item):
        table = self.ui.fMainPage.fTable
        table.blockSignals(True)
        try:
            rowCount = table.rowCount()
            table.insertRow(rowCount)
            table.setItem(rowCount, 0, QTableWidgetItem(item.group))
            table.setItem(rowCount, 1, QTableWidgetItem(item.department))
            table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
            table.setItem(rowCount, 3, QTableWidgetItem(item.location))
            if item.responsiblePerson is None:
                table.setItem(rowCount, 4, QTableWidgetItem(''))
            else:
                table.setItem(rowCount, 4, QTableWidgetItem(item.responsiblePerson.userName))
            table.setItem(rowCount, 5, QTableWidgetItem(item.state.value))
            table.setCellWidget(rowCount, 6, self.getDeleteButton(table))
        finally:
            table.blockSignals(False)


    def onSearchInItemTable(self):
        attribute = self.ui.fMainPage.fFilterDropDown.currentText()
        if not self.ui.fMainPage.fStateDropDown.visibleRegion().isEmpty():
            searchText = self.ui.fMainPage.fStateDropDown.currentText().lower()
        elif not self.ui.fMainPage.fResponsiblePersonDropDown.visibleRegion().isEmpty():
            searchText = self.ui.fMainPage.fResponsiblePersonDropDown.currentText().lower()
        else:
            searchText = self.ui.fMainPage.fFilterInput.text().lower()

        if not searchText:
            self.loadItemTableData()
            return

        attributeMap = {
            ItemHeader.GROUP.value: 'group',
            ItemHeader.DEPARTMENT.value: 'department',
            ItemHeader.SUBJECT.value: 'subject',
            ItemHeader.LOCATION.value: 'location',
            ItemHeader.RESPONSIBLE.value: 'responsiblePerson',
            ItemHeader.STATE.value: 'state',
        }

        table = self.ui.fMainPage.fTable
        table.setRowCount(0)

        for item in self.items:
            itemAttribute = attributeMap.get(attribute)
            if itemAttribute:
                if attribute == ItemHeader.STATE.value:
                    itemValue = getattr(item, itemAttribute, '').value.lower()
                else:
                    itemValue = getattr(item, itemAttribute, '').lower()
                if searchText in itemValue:
                    rowCount = table.rowCount()
                    table.insertRow(rowCount)
                    table.setItem(rowCount, 0, QTableWidgetItem(item.group))
                    table.setItem(rowCount, 1, QTableWidgetItem(item.department))
                    table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
                    table.setItem(rowCount, 3, QTableWidgetItem(item.location))
                    resp_name = ""
                    if item.responsiblePerson:
                        if hasattr(item.responsiblePerson, 'userName'):
                            resp_name = item.responsiblePerson.userName
                        else:
                            resp_name = str(item.responsiblePerson)

                    table.setItem(rowCount, 4, QTableWidgetItem(resp_name))
                    state_val = ""
                    if hasattr(item, 'state') and item.state:
                        state_val = item.state.value if hasattr(item.state, 'value') else str(item.state)

                    table.setItem(rowCount, 5, QTableWidgetItem(state_val))
                    table.setCellWidget(rowCount,6, self.getDeleteButton(table))
        table.setEditTriggers(QTableWidget.EditTrigger.AllEditTriggers)

    def onAddUser(self):
        dialog = AddUserDialog()
        if dialog.exec():
            new_user = dialog.getUser()
            if new_user:
                self.model.addUser(new_user)
                self.model.save()
                self.loadUserTableData()

    def onItemChanged(self, item):
        if self._is_editing:
            return
        self._is_editing = True
        try:
            column = item.column()
            row = item.row()
            newValue = item.text()
            self.editItem(row, column, newValue)
            self.model.save()
            self.refreshItems()
        finally:
            self._is_editing = False
    def onUserChanged(self, item):
        if self._is_editing:
            return
        self._is_editing = True
        try:
            column = item.column()
            row = item.row()
            newValue = item.text()
            self.editUser(row, column, newValue)
            self.model.save()
            self.refreshUsers()
        finally:
            self._is_editing = False
    def editUser(self,row,column, newValue):
        match column:
            case 0:
                self.users.__getitem__(row).firstName = newValue
            case 1:
                self.users.__getitem__(row).lastName = newValue
            case 2:
                self.users.__getitem__(row).userName = newValue
            case 3:
                self.users.__getitem__(row).role = newValue

    def handleItemClick(self, item):
        row = item.row()
        col = item.column()
        selectedItem = self.items[row]
        if col == 5 or col == 4:
            self.openEditChangeDialog(item, selectedItem)

    def openEditUserRoleDialog(self, item):
        if self._is_editing:
            return

        if item.column() == 3:
            self._is_editing = True
            try:
                row = item.row()
                selected_user = self.users[row]

                dialog = EditUserRoleDialog(selected_user)
                if dialog.exec():
                    role_text = selected_user.role.value if hasattr(selected_user.role, 'value') else str(
                        selected_user.role)
                    item.setText(role_text)
                    self.model.save()
            finally:
                self._is_editing = False
    def selectInputForMainPage(self):
        if self.ui.fMainPage.fFilterDropDown.currentText() == ItemHeader.RESPONSIBLE.value:
            self.ui.fMainPage.fResponsiblePersonDropDown.show()

            self.ui.fMainPage.fFilterInput.hide()
            self.ui.fMainPage.fStateDropDown.hide()
        elif self.ui.fMainPage.fFilterDropDown.currentText() == ItemHeader.STATE.value:
            self.ui.fMainPage.fStateDropDown.show()

            self.ui.fMainPage.fFilterInput.hide()
            self.ui.fMainPage.fResponsiblePersonDropDown.hide()
        else:
            self.ui.fMainPage.fFilterInput.show()

            self.ui.fMainPage.fStateDropDown.hide()
            self.ui.fMainPage.fResponsiblePersonDropDown.hide()
    def openEditChangeDialog(self, item, selectedItem):
        if self._is_editing:
            return

        col = item.column()
        self._is_editing = True

        try:
            dialog = None
            if col == 4:
                dialog = EditResponsiblePersonDialog(selectedItem, self.responsiblePersons, self.ui.fMainPage)
            elif col == 5:
                dialog = EditItemStateDialog(selectedItem, self.ui.fMainPage)
            if dialog and dialog.exec():
                if col == 4:
                    item.setText(selectedItem.responsiblePerson.userName if hasattr(selectedItem.responsiblePerson, 'userName') else selectedItem.responsiblePerson)
                elif col == 5:
                    item.setText(
                        selectedItem.state.value if hasattr(selectedItem.state, 'value') else selectedItem.state)

                self.model.save()
                self.loadItemTableData()
        finally:
            self._is_editing = False

    def editItem(self,row,column, newValue):
        match column:
            case 0:
                self.items.__getitem__(row).group = newValue
            case 1:
                self.items.__getitem__(row).department = newValue
            case 2:
                self.items.__getitem__(row).subject = newValue
            case 3:
                self.items.__getitem__(row).location = newValue
            case 4:
                self.items.__getitem__(row).responsiblePerson = newValue
            case 5:
                self.items.__getitem__(row).state = normalizeText(newValue)

    def getDeleteButton(self,table, userButton = False):
        deleteButton = QPushButton("Löschen")
        if not userButton:
            deleteButton.clicked.connect(lambda: self.removeItemRowAtButton(deleteButton, table))
        else:
            deleteButton.clicked.connect(lambda: self.removeUserRowAtButton(deleteButton, table))

        return deleteButton
    def removeItemRowAtButton(self, deleteButton, table):
        if deleteButton:
            index = table.indexAt(deleteButton.pos())
            if index.isValid():
                table.removeRow(index.row())
                self.model.items.pop(index.row())
        self.model.save()
    def removeUserRowAtButton(self, deleteButton, table):
        if deleteButton:
            index = table.indexAt(deleteButton.pos())
            if self.user.userName == self.users.__getitem__(index.row()).userName:
                return
            if index.isValid():
                table.removeRow(index.row())
                self.model.users.pop(index.row().__index__())
        self.model.save()

    def loadItemTableData(self):
        table = self.ui.fMainPage.fTable
        table.setRowCount(0)
        table.blockSignals(True)
        for item in self.items:
            rowCount = table.rowCount()
            table.insertRow(rowCount)
            table.setItem(rowCount, 0, QTableWidgetItem(item.group))
            table.setItem(rowCount, 1, QTableWidgetItem(item.department))
            table.setItem(rowCount, 2, QTableWidgetItem(item.subject))
            table.setItem(rowCount, 3, QTableWidgetItem(item.location))
            resp_name = ""
            if item.responsiblePerson:
                if hasattr(item.responsiblePerson, 'userName'):
                    resp_name = item.responsiblePerson.userName
                else:
                    resp_name = str(item.responsiblePerson)

            table.setItem(rowCount, 4, QTableWidgetItem(resp_name))
            state_val = ""
            if hasattr(item, 'state') and item.state:
                state_val = item.state.value if hasattr(item.state, 'value') else str(item.state)

            table.setItem(rowCount, 5, QTableWidgetItem(state_val))
            table.setCellWidget(rowCount, 6, self.getDeleteButton(table))
        table.blockSignals(False)

    def loadUserTableData(self):
        table = self.ui.fAdminPage.fTable
        table.setRowCount(0)
        for user in self.users:
            rowCount = table.rowCount()
            table.insertRow(rowCount)
            table.setItem(rowCount, 0, QTableWidgetItem(user.firstName))
            table.setItem(rowCount, 1, QTableWidgetItem(user.lastName))
            table.setItem(rowCount, 2, QTableWidgetItem(user.userName))
            table.setItem(rowCount, 3, QTableWidgetItem(user.role.value if isinstance(user.role, UserRole) else user.role))
            table.setCellWidget(rowCount, 4, self.getDeleteButton(table, True))
    def onLogout(self):
        self.ui.hideInventoryPage()
        self.ui.hideAdminPage()
        self.ui.fLoginPage.fUserName.clear()
        self.ui.fLoginPage.fPassword.clear()
        self.ui.showLoginPage()

    def showCSVMessage(self):
        csvDialog = QMessageBox(self.ui.fAdminPage)
        csvDialog.setIcon(QMessageBox.Icon.Information)
        csvDialog.setWindowTitle('Tabelle exportiert')
        csvDialog.setText('Die Tabelle wurde in einer CSV Datei exportiert!')
        csvDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        csvDialog.exec()

    def createCsvExportFile(self):
        csvContent = []
        csvHeader = ['Gruppe', 'Abteilung', 'Fach', 'Ort', 'Verantworlicher', 'Zustand']
        csvContent.append(csvHeader)
        for item in self.items:
            csvContent.append([
                item.group,
                item.department,
                item.subject,
                item.location,
                item.responsiblePerson,
                item.state.value
        ])
        with open('export.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(csvContent)
        self.showCSVMessage()


