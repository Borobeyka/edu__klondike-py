import pygame

from objects.glob import *
from objects.actions import *

class Card (Actions):

    def __init__(self, surface, x, y, suit, nominal):
        super().__init__(surface, x, y)
        self.suit = suit
        self.nominal = nominal
        self.is_visible = True
        if self.suit == "heart" or self.suit == "diamond":
            self.icon_color = config["color"]["red"]
        else:
            self.icon_color = config["color"]["black"]
        self.small_icon = pygame.transform.scale(cards_icon.get(suit),
            (config["card"]["icon"]["s_width"], config["card"]["icon"]["s_height"]))
        self.large_icon = pygame.transform.scale(cards_icon.get(suit),
            (config["card"]["icon"]["l_width"], config["card"]["icon"]["l_height"]))

    def show(self):
        if self.is_visible:
            surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)

            pygame.draw.rect(surface, config["color"]["white"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                border_radius=config["card"]["radius"])
            pygame.draw.rect(surface, config["color"]["black"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                2, config["card"]["radius"])

            # nominal
            text = card_nominal.render(config["nominal"][self.nominal], True, self.icon_color)
            surface.blit(text, (config["card"]["icon"]["offsetX"], config["card"]["icon"]["offsetY"]))
            
            # icons
            surface.blit(self.small_icon, (
                config["card"]["width"] - config["card"]["icon"]["s_width"] - config["card"]["icon"]["offsetX"],
                config["card"]["icon"]["offsetY"] + 10
            ))
            surface.blit(self.large_icon, (
                config["card"]["width"] / 2 - config["card"]["icon"]["l_width"] / 2,
                config["card"]["icon"]["offsetY"] + config["card"]["icon"]["l_offset"]
            ))
        else:
            surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)
            pygame.draw.rect(surface, config["color"]["grey"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                border_radius=config["card"]["radius"])
            pygame.draw.rect(surface, config["color"]["black"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                2, config["card"]["radius"])
        self.surface.blit(surface, (self.x, self.y))

    def is_in_area(self, x, y):
        if (x > self.x and x < self.x + config["card"]["width"] and
            y > self.y and y < self.y + config["card"]["height"]):
            return True
        return False

    def set_visible(self, status):
        self.is_visible = status