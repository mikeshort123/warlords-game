import pygame, json

from src.utils.vector import Vector
from src.utils.renderer import Renderer

class Handler():


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


    def getUIMousePos(self):

        return ((self.mousepos - Vector(Renderer.renderer.x_offset, Renderer.renderer.y_offset)) / Renderer.renderer.min_ratio).int()

    def getGameMousePos(self):

        return (self.mousepos - Renderer.renderer.windowSize / 2) / Renderer.renderer.max_ratio


    def handleEvent(self,e):

        if e.type == pygame.KEYDOWN:
            self.setKey(e.unicode, True)

        if e.type == pygame.KEYUP:
            self.setKey(e.unicode, False)

        if e.type == pygame.MOUSEBUTTONDOWN:
            self.setKey("mb" + str(e.button), True)

        if e.type == pygame.MOUSEBUTTONUP:
            self.setKey("mb" + str(e.button), False)

        if e.type == pygame.MOUSEMOTION:
            self.mousepos = Vector(e.pos)


    def setKey(self, key, mode):
        if key in self.keyList:
            self.keyList[key] = mode

            if mode: self.keyChanges.append(key)
