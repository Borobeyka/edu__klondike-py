import pygame
import sys

from random import randint
from objects.glob import *
from objects.card import *
from objects.heap import *
from objects.stack import *


pygame.init()
pygame.display.set_caption(f"Klondike {config['app']['version']}")
clock = pygame.time.Clock()

for i in range(4):
    for j in range(13):
        cards.append(Card(window, 0, 0, config["suits"][i], j))
x = 10
for i in range(7):
    stacks.append(Stack(window, x, 150))
    for j in range(i + 1):
        if (i + 1) - j == 1:
            #print(1)
            stacks[i].push_card(cards[randint(0, len(cards) - 1)])
        else:
            card = cards[randint(0, len(cards) - 1)]
            card.set_visible(False)
            stacks[i].push_card(card);
    x += config["card"]["width"] + config["stack"]["offset"]

dragged_card = None

while True:
    window.fill(config["color"]["green"])
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for stack in stacks:
                if stack.is_in_area(x, y) and not stack.is_empty():
                    dragged_heap = stack.get_heap_on_focus(x, y)
                    if type(dragged_heap) is None:
                        dragged_heap.save_old_coords()
                        dragged_stack = stack
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if dragged_heap != None:
                dragged_heap.return_prev_coords()
                dragged_stack.push_heap(dragged_heap)
                dragged_heap = None
                dragged_stack = None
        
    if dragged_heap != None:
        dragged_heap.update_coords(x, y)
        dragged_heap.show()

    clock.tick(config["app"]["fps"])

    for stack in stacks:
        stack.show()
    # stack.show()
    # card.show()


    pygame.display.update()
