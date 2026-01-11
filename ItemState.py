from enum import Enum

def normalizeItems(items):
    for item in items:
        if not isinstance(item, ItemState):
            item.state = normalizeText(item.state)

    return items

def normalizeText(text):
    match text:
        case 'Eingesetzt':
            return ItemState.USED
        case 'Projektiert':
            return ItemState.PROJECTED
        case 'Angefordert':
            return ItemState.REQUESTED
        case 'Bestellt':
            return ItemState.ORDERED
        case 'Geliefert':
            return ItemState.DELIVERED
        case 'Ausgeliehen':
            return ItemState.BORROWED
        case 'Reperatur':
            return ItemState.FIXING
        case 'Ausgemustert':
            return ItemState.RETIRED
        case _:
            if isinstance(text, ItemState):
                return text
            return None

class ItemState(Enum):
    PROJECTED = "Projektiert"
    REQUESTED = "Angefordert"
    ORDERED = "Bestellt"
    DELIVERED = "Geliefert"
    USED = "Eingesetzt"
    BORROWED = "Ausgeliehen"
    FIXING = "Reperatur"
    RETIRED = "Ausgemustert"


