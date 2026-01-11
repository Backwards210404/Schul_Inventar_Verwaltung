from userrole import UserRole


class User:
    firstName: str
    lastName: str
    userName: str
    password: str
    role: UserRole

    def __init__(self,firstName, lastName, userName, password, role):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.role = role

    def getFirstName(self):
        return self.firstName
    def setFirstName(self, firstName):
        self.firstName = firstName
    def getLastName(self):
        return self.lastName
    def setLastName(self, lastName):
        self.lastName = lastName
    def getUserName(self):
        return self.userName
    def setUserName(self, userName):
        self.userName = userName
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password
    def setRole(self, role):
        self.role = role
    def getRole(self):
        return self.role