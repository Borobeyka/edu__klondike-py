import pygame
import sys

from objects.glob import *
from objects.card import *


pygame.init()
window.fill(config["color"]["green"])
pygame.display.set_caption(f"Klondike {config['app']['version']}")
clock = pygame.time.Clock()

card = Card(window, 20, 20, "heart", 1)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            if card.isInArea(x, y):
                print(card.nominal)

    clock.tick(config["app"]["fps"])

    card.show()


    pygame.display.flip()