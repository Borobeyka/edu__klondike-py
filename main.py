import pygame
import sys

from objects.glob import *
from objects.card import *


pygame.init()
window.fill(config["color"]["green"])
pygame.display.set_caption(f"Klondike {config['app']['version']}")
clock = pygame.time.Clock()

card = Card(window, 20, 20, config["suits"][2], config["nominal"][11])

dragged_card = None

while True:
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if card.isInArea(x, y):
                dragged_card = card
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragged_card = None
        
    if dragged_card != None:
        print("1")

    clock.tick(config["app"]["fps"])

    card.show()


    pygame.display.flip()