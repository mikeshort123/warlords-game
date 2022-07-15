from pygame.locals import *
import json

from src.utils.vector import Vector

class Handler():

    def __init__(self):

        with open("res/keybinds.json", encoding="utf8") as f:
            self.keyMap = json.load(f)

        self.keyList = {
            self.keyMap[i] : False for i in self.keyMap
        }
        self.keyBinds = {
            self.keyMap[i] : None for i in self.keyMap
        }

        self.mousepos = Vector()

        self.mouseButtons = [False for i in range(3)]
        self.mouseButtonBinds = [None for i in range(3)]


    def getKey(self,key):

        return self.keyList[self.keyMap[key]]

    def getMousePos(self):

        return self.mousepos

    def getMouseKey(self,index):

        return self.mouseButtons[index]

    def handleEvent(self,e):

        if e.type == KEYDOWN:
            if e.unicode in self.keyList:
                self.keyList[e.unicode] = True

                if self.keyBinds[e.unicode] != None:
                    self.keyBinds[e.unicode](self)

        if e.type == KEYUP:
            if e.unicode in self.keyList:
                self.keyList[e.unicode] = False

        if e.type == MOUSEMOTION:
            self.mousepos = Vector(e.pos)

        if e.type == MOUSEBUTTONDOWN:
            self.mouseButtons[e.button-1] = True

            if self.mouseButtonBinds[e.button-1] != None:
                self.mouseButtonBinds[e.button-1](self)

        if e.type == MOUSEBUTTONUP:
            self.mouseButtons[e.button-1] = False

    def bindClickFunction(self,f,k):
        self.mouseButtonBinds[k] = f

    def bindButtonFunction(self,f,key):
        self.keyBinds[self.keyMap[key]] = f

    def clearBinds(self):
        self.keyBinds = {
            self.keyMap[i] : None for i in self.keyMap
        }
        self.mouseButtonBinds = [None for i in range(3)]
