

class Fullauto:

    def __init__(self,subtype,stats,element):

        self.firerate = 3600 // subtype["firerate"]
        self.count = self.firerate

        self.damage = subtype["damage"]
        self.status_chance = stats["element_chance"]
        self.element = element

        self.status_counter = 0

    def tick(self,handler,bulletGenerator):

        if self.count == 0:

            if handler.getKeyPressed("SHOOT"):
                bulletGenerator(handler,self)
                self.count = self.firerate

        else:

            self.count -= 1


    def generateDamageProfile(self):

        self.status_counter += self.status_chance
        procs = int(self.status_counter)
        self.status_counter %= 1

        return self.damage, self.element, procs
