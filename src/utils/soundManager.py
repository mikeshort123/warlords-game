import pygame

class SoundManager:

    @staticmethod
    def playSound(sound):
        pygame.mixer.Sound.play(sound)
