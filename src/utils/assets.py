import pygame,json

from src.models.playerModelTwo import PlayerModelTwo

class Assets():

    assets = {}
    models = {}

    @staticmethod
    def loadImage(fp):

        if fp in Assets.assets: return Assets.assets[fp]

        img = pygame.image.load(fp)
        Assets.assets[fp] = img
        return img

    @staticmethod
    def loadModel(fp):

        if fp in Assets.models: return Assets.models[fp]

        with open(fp) as f:
            model_data = json.load(f)

        texture = Assets.loadImage(model_data["texture"])

        if model_data["frame"] == "player":
            model = PlayerModelTwo(model_data,texture)


        Assets.models[fp] = model
        return model


    @staticmethod
    def flush():

        Assets.assets.clear()
        Assets.models.clear()

    font = None

    @staticmethod
    def loadFont():
        Assets.font = pygame.font.SysFont(None, 18)
