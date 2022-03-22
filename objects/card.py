import pygame

from objects.glob import *

class Card:

    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def draw(self):
        surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)
        pygame.draw.rect(surface, config["color"]["white"],
            (0, 0, config["card"]["width"], config["card"]["height"]),
            border_radius=8)
        pygame.draw.rect(surface, config["color"]["black"],
            (0, 0, config["card"]["width"], config["card"]["height"]),
            2, config["card"]["radius"])

        self.surface.blit(surface, (self.x, self.y))

    #def isInArea(self, x, y):
        