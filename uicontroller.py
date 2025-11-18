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
    def initItems(self): 
        self.items = self.model.load()