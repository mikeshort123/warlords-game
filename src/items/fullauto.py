

class Fullauto:

    def __init__(self,firerate):

        self.firerate = firerate
        self.count = self.firerate


    def tick(self,handler):

        if self.count == 0:

            if handler.getKeyPressed("SHOOT"):
                self.count = self.firerate
                return True

        else:

            self.count -= 1

        return False
