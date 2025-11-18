class Item:
    group: str
    department: str
    subject: str
    location: str
    responsiblePerson: str

    def __init__(self): 
        self = self
        
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