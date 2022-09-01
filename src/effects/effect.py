

class Effect: # I dont know if i need to have effects inheret this, but here it is for now

    def __init__(self, source):

        self.stacks = 0
        self.source = source

    def addStacks(self,stacks):

        self.stacks += stacks
