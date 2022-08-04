import pygame, json

from src.utils.vector import Vector

class Handler():

    mouse_button_codes = [
        "lmb",
        "mmb",
        "rmb"
    ]

    def __init__(self):



        with open("res/keybinds.json", encoding="utf8") as f:
            self.keyMap = json.load(f)

        self.keyList = {
            self.keyMap[i] : False for i in self.keyMap
        }

        self.keyChanges = []

        self.mousepos = Vector()

    def reset(self):
        self.keyChanges = []


    def getKeyPressed(self,key):

        return self.keyList[self.keyMap[key]]

    def getKeyChanged(self,key):

        code = self.keyMap[key]
        return code in self.keyChanges


    def getMousePos(self):

        return self.mousepos


    def handleEvent(self,e):

        if e.type == pygame.KEYDOWN:
            if e.unicode in self.keyList:
                self.keyList[e.unicode] = True

                self.keyChanges.append(e.unicode)

        if e.type == pygame.KEYUP:
            if e.unicode in self.keyList:
                self.keyList[e.unicode] = False

        if e.type == pygame.MOUSEMOTION:
            self.mousepos = Vector(e.pos)

        if e.type == pygame.MOUSEBUTTONDOWN:
            key = Handler.mouse_button_codes[e.button-1]
            if key in self.keyList:
                self.keyList[key] = True

                self.keyChanges.append(key)

        if e.type == pygame.MOUSEBUTTONUP:
            key = Handler.mouse_button_codes[e.button-1]
            if key in self.keyList:
                self.keyList[key] = False


    def playSound(self,sound):
        pygame.mixer.Sound.play(sound)
