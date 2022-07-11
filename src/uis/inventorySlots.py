

class InventorySlot(list):

    def __init__(self):
        list.__init__(self)

    def getActive(self):
        if len(self) == 0:
            return None
        return list.__getitem__(self, 0)

    def setActive(self,i):
        self[0],self[i] = self[i],self[0]


    def tick(self,handler): return

    def render(self,renderer): return
