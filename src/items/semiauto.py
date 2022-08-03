

class Semiauto:

    PREFIRE_RATIO = 0.7

    def __init__(self):

        self.count = 0

        self.prefire = False



    def tick(self, handler, firerate):

        if self.count >= firerate * Semiauto.PREFIRE_RATIO and handler.getKeyChanged("SHOOT"):
            self.prefire = True

        if self.count >= firerate:

            if self.prefire:
                self.count = 0
                self.prefire = False
                return True

        else:

            self.count += 1

        return False
