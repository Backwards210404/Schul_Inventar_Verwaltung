from ItemState import ItemState
from user import User


class Item:
    group: str
    department: str
    subject: str
    location: str
    responsiblePerson: User
    state: ItemState

    def __init__(self,group,department, subject, location, responsiblePerson, state):
        self.group = group
        self.department = department
        self.subject = subject
        self.location = location 
        self.responsiblePerson = responsiblePerson
        self.state = state
        
    def getGroup(self): 
        return self.group
    def setGroup(self, group): 
        self.group = group
    def getDepartment(self): 
        return self.department
    def setDepartment(self, department): 
        self.department = department
    def getSubject(self): 
        return self.subject
    def setSubject(self, subject): 
        self.subject = subject
    def getLocation(self):
        return self.location 
    def setLocation(self, location): 
        self.location = location
    def getResponsiblePerson(self):
        return self.responsiblePerson
    def setResponsiblePerson(self, responsiblePerson): 
        self.responsiblePerson = responsiblePerson