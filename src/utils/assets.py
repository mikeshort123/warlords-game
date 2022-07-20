import pygame,json

from src.models.playerModelTwo import PlayerModelTwo
from src.animations.animationGenerator import AnimationGenerator

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

        if fp in Assets.models:
            model, generator = Assets.models[fp]
            return model, generator.newController()

        with open(fp) as f:
            model_data = json.load(f)

        texture = Assets.loadImage(model_data["texture"])

        with open(model_data["animations"]) as f:
            animation_data = json.load(f)

        parts = ["head","body","left_foot","right_foot","left_hand","right_hand"]
        generator = AnimationGenerator(animation_data,parts)

        if model_data["frame"] == "player":
            model = PlayerModelTwo(model_data,texture)


        Assets.models[fp] = [model,generator]
        return model, generator.newController()


    @staticmethod
    def flush():

        Assets.assets.clear()
        Assets.models.clear()

    font = None

    @staticmethod
    def loadFont():
        Assets.font = pygame.font.SysFont(None, 18)
