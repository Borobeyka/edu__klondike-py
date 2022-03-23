import pygame
import sys

from objects.glob import *
from objects.card import *
from objects.stack import *


pygame.init()
pygame.display.set_caption(f"Klondike {config['app']['version']}")
clock = pygame.time.Clock()

cards = []

for i in range(4):
    for j in range(13):
        cards.append(Card(window, 0, 0, config["suits"][i], j))


card = Card(window, 120, 120, config["suits"][2], config["nominal"][11])
stack = Stack(window, 20, 20)

dragged_card = None



while True:
    window.fill(config["color"]["green"])
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if card.is_in_area(x, y):
                dragged_card = card
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragged_card = None
        
    if dragged_card != None:
        dragged_card.update_coords(x, y)
        dragged_card.show()

    clock.tick(config["app"]["fps"])

    stack.show()
    card.show()


    pygame.display.update()
