class Teacher:
    firstName: str
    lastName: str

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName