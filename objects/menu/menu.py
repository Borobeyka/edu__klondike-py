import pygame

from objects.glob import *

class Menu:
    def __init__(self, surface):
        self.surface = surface

    
    def show(self):
        surface = pygame.Surface((config["app"]["width"], config["app"]["height"]), pygame.SRCALPHA)
        surface.fill(config["color"]["black"])
        surface.set_alpha(255 * config["menu"]["shadow"] / 100)
        self.surface.blit(surface, (0, 0))