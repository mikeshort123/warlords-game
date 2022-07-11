from src.utils.assets import Assets

class Inventory():

    def __init__(self):

        self.active = False
        self.img = Assets.getImage("inventory")

    def tick(self,handler):

        if not self.active:
             self.active = handler.getKey("OPEN_INVENTORY")
             return

        self.active = not handler.getKey("CLOSE_INVENTORY")

    def render(self,renderer):

        if not self.active:
             return

        renderer.drawImage(self.img,20,20)
