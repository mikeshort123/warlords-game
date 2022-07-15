import pygame

class Assets():

    assets = {}

    @staticmethod
    def loadImage(fp):

        if fp in Assets.assets: return Assets.assets[fp]

        img = pygame.image.load(fp)
        Assets.assets[fp] = img
        return img


    @staticmethod
    def flush():

        Assets.assets.clear()

    font = None

    @staticmethod
    def loadFont():
        Assets.font = pygame.font.SysFont(None, 18)
