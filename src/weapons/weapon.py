from src.items.item import Item

class Weapon(Item):

    def __init__(self,fn):

        self.model = WeaponModel(fn, None)
