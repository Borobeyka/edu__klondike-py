import pygame
import sys

from objects.glob import *
from objects.card import *


pygame.init()
window.fill(config["color"]["green"])
pygame.display.set_caption(f"Klondike {config['app']['version']}")
clock = pygame.time.Clock()

card = Card(window, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
          print ( pygame.mouse.get_pos() )
    clock.tick(config["app"]["fps"])

    card.draw()

    pygame.display.flip()