import pygame

from objects.glob import *

class Card:

    def __init__(self, surface, x, y, suit, nominal):
        self.surface = surface
        self.x = x
        self.y = y
        self.suit = suit
        self.nominal = nominal
        self.small_icon = pygame.transform.scale(cards_icon.get(suit),
            (config["card"]["icon"]["s_width"], config["card"]["icon"]["s_height"]))
        self.large_icon = pygame.transform.scale(cards_icon.get(suit),
            (config["card"]["icon"]["l_width"], config["card"]["icon"]["l_height"]))

    def show(self):
        surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)
        
        pygame.draw.rect(surface, config["color"]["white"],
            (0, 0, config["card"]["width"], config["card"]["height"]),
            border_radius=8)
        pygame.draw.rect(surface, config["color"]["black"],
            (0, 0, config["card"]["width"], config["card"]["height"]),
            2, config["card"]["radius"])

        # nominal
        text = card_nominal.render(str(self.nominal), True, config["color"]["red"])
        surface.blit(text, (config["card"]["icon"]["offsetX"], config["card"]["icon"]["offsetY"]))
        
        # icons
        surface.blit(self.small_icon, (
            config["card"]["width"] - config["card"]["icon"]["s_width"] - config["card"]["icon"]["offsetX"],
            config["card"]["icon"]["offsetY"] + 10
        ))
        surface.blit(self.large_icon, (
            config["card"]["width"] / 2 - config["card"]["icon"]["l_width"] / 2,
            config["card"]["icon"]["offsetY"] + 55
        ))

        self.surface.blit(surface, (self.x, self.y))

    def isInArea(self, *coords):
        x, y = coords
        if (x > self.x and x < self.x + config["card"]["width"] and
            y > self.y and y < self.y + config["card"]["height"]):
            return True
        return False
