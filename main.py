import pygame
import sys

from random import randint
from objects.glob import *
from objects.game.card import *
from objects.game.heap import *
from objects.game.stack import *
from objects.game.storage import *
from objects.game.deck import *

from objects.menu.menu import *

pygame.init()
pygame.display.set_caption("Klondike v%s" % config["app"]["version"])
clock = pygame.time.Clock()

for i in range(4):
    for j in range(13):
        cards.append(Card(window, 0, 0, config["suits"][i], j))
x = 10
for i in range(7):
    stacks.append(Stack(window, x, 170))
    for j in range(i + 1):
        if (i + 1) - j == 1:
            stacks[i].push_card(cards[randint(0, len(cards) - 1)])
        else:
            card = cards[randint(0, len(cards) - 1)]
            card.set_visible(False)
            stacks[i].push_card(card);
    x += config["card"]["width"] + config["stack"]["offset"]

x = 10
for i in range(4):
    storages.append(Storage(window, x, 10))
    x += config["card"]["width"] + config["stack"]["offset"]

deck = Deck(window, (config["card"]["width"] + config["stack"]["offset"]) * 6 + 10, 10);
for i in range(len(cards)):
    card = cards[randint(0, len(cards) - 1)]
    deck.add_card(card)
    cards.remove(card)

menu = Menu(window)

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
                    if dragged_heap != None:
                        dragged_heap.save_old_coords()
                        dragged_stack = stack

            for storage in storages:
                if storage.is_in_area(x, y) and not storage.is_empty():
                    dragged_heap = storage.get_heap_on_focus(x, y)
                    if dragged_heap != None:
                        dragged_heap.save_old_coords()
                        dragged_stack = storage
                    
            if deck.is_in_area(x, y) and dragged_heap == None:
                deck.pick_card()

            for idx, card in enumerate(deck.cards):
                if card.is_in_area(x, y) and deck.current_card_index == idx:
                    dragged_heap = deck.get_heap_on_focus(x, y)
                    if dragged_heap != None:
                        dragged_heap.save_old_coords()
                        dragged_stack = deck

        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragged_heap != None:

            for stack in stacks:
                if stack.is_in_area(x, y):
                    if stack.is_can_stack(dragged_heap):
                        stack.push_heap(dragged_heap)
                        if dragged_stack.count() > 0:
                            dragged_stack.get_last_card().set_visible(True)
                        dragged_heap = None

            for storage in storages:
                if storage.is_in_area(x, y):
                    if storage.is_can_stack(dragged_heap):
                        storage.push_heap(dragged_heap)
                        if dragged_stack.count() > 0:
                            dragged_stack.get_last_card().set_visible(True)
                        dragged_heap = None

            if dragged_heap != None:
                dragged_heap.return_prev_coords()
                dragged_stack.push_heap(dragged_heap)
                dragged_heap = None
                dragged_stack = None
        
    

    clock.tick(config["app"]["fps"])

    for stack in stacks:
        stack.show()

    for storage in storages:
        storage.show()
    
    deck.show()

    if dragged_heap != None:
        dragged_heap.update_coords(x, y)
        dragged_heap.show()

    menu.show()

    pygame.display.update()