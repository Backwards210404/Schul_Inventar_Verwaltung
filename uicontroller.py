from item import Item
from model import Model
from ui import UI


class UIController:

    items: list[Item]
    ui: UI
    model: Model
    
    def __init__(self):
        self.ui = UI()
        self.model = Model()
    def refreshItems(self): 
        self.items = self.model.load()
    def onLogin(self):
        # todo
        self = self
    def initClickEvents(self):
        # todo
        self = self
    def onFilterSelected(self):
        # todo
        self = self
