

class Semiauto:



    def __init__(self,subtype,stats,element):

        self.firerate = 3600 // subtype["firerate"]
        self.prefire_delta = self.firerate // 3
        self.count = self.firerate


        self.prefire = False

        self.element = element

    def tick(self,handler,bulletGenerator):

        if self.count <= self.prefire_delta and handler.getKeyChanged("SHOOT"):
            self.prefire = True

        if self.count == 0:

            if self.prefire:
                bulletGenerator(handler,self.element.colour)
                self.count = self.firerate
                self.prefire = False

        else:

            self.count -= 1
