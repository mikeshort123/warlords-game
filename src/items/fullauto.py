

class Fullauto:

    def __init__(self,subtype,stats,element):

        self.firerate = 3600 // subtype["firerate"]
        self.count = self.firerate

        self.element = element

    def tick(self,handler,bulletGenerator):

        if self.count == 0:

            if handler.getKeyPressed("SHOOT"):
                bulletGenerator(handler,self.element.colour)
                self.count = self.firerate

        else:

            self.count -= 1
