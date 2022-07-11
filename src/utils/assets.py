import pygame

class Assets():

    assets = {}

    @staticmethod
    def loadImage(name,fp):

        img = pygame.image.load(fp)
        Assets.assets[name] = img
        return img

    @staticmethod
    def getImage(name):

        return Assets.assets[name]

    @staticmethod
    def flush():

        Assets.assets.clear()
