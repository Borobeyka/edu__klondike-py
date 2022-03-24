import pygame

from objects.glob import *

class Bar:

    def __init__(self, surface):
        self.surface = surface
    
    def show(self):
        surface = pygame.Surface((config["app"]["width"], config["bar"]["height"]), pygame.SRCALPHA)
        surface.set_alpha(160)
        pygame.draw.rect(surface, config["color"]["black"],
            (0, 0, config["app"]["width"], config["bar"]["height"]))

        text = card_nominal.render("Score: %d" % score, True, config["color"]["white"])
        text_rect = text.get_rect(center=(surface.get_rect()[2] / 2, config["bar"]["height"] / 2))
        surface.blit(text, text_rect)

        timer = abs(int(round(timeStarted - time.time())))
        if timer > 60:
            timer = "%dm %ds" % (timer / 60, timer % 60)
        else:
            timer = "%ds" % timer
        text = card_nominal.render("Time: %s" % timer, True, config["color"]["white"])
        text_rect = text.get_rect(center=(surface.get_rect()[2] / 2 + 250, config["bar"]["height"] / 2))
        surface.blit(text, text_rect)

        self.surface.blit(surface, (0, 0))
