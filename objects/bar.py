import pygame

from objects.glob import *

class Bar:

    def __init__(self, surface):
        self.surface = surface
        self.score = 0
    
    def show(self):
        if game_loop:
            surface = pygame.Surface((config["app"]["width"], config["bar"]["height"]), pygame.SRCALPHA)
            surface.set_alpha(160)
            pygame.draw.rect(surface, config["color"]["black"],
                (0, 0, config["app"]["width"], config["bar"]["height"]))

            text = card_nominal.render("Score: %d" % self.score, True, config["color"]["white"])
            text_rect = text.get_rect(center=(surface.get_rect()[2] / 2, config["bar"]["height"] / 2))
            surface.blit(text, text_rect)

            timer = abs(int(time_started - time.time()))
            timer = "%.2d:%.2d" % (timer / 60, timer % 60)
            text = card_nominal.render("Time: %s" % timer, True, config["color"]["white"])
            text_rect = text.get_rect(center=(surface.get_rect()[2] / 2 + 250, config["bar"]["height"] / 2))
            surface.blit(text, text_rect)

            self.surface.blit(surface, (0, 0))

    def add_score(self, score):
        if self.score + score < 0:
            self.score = 0
        else:
            self.score += score
