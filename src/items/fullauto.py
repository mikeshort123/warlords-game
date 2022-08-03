

class Fullauto:

    def __init__(self):

        self.count = 0


    def tick(self,handler,firerate):

        if self.count >= firerate:

            if handler.getKeyPressed("SHOOT"):
                self.count = 0
                return True

        else:

            self.count += 1

        return False
