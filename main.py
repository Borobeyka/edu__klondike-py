import pygame
import sys

from random import randint
from objects.glob import *
from objects.card import *
from objects.heap import *
from objects.stack import *
from objects.storage import *
from objects.deck import *
from objects.bar import *

pygame.init()
pygame.display.set_caption("Klondike v%s" % config["app"]["version"])
clock = pygame.time.Clock()


for i in range(4):
    for j in range(13):
        cards.append(Card(window, 0, 0, config["suits"][i], j))
x = 10
for i in range(7):
    stacks.append(Stack(window, x, config["bar"]["height"] + 170))
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
    storages.append(Storage(window, x, config["bar"]["height"] + 10))
    x += config["card"]["width"] + config["stack"]["offset"]

deck = Deck(window, (config["card"]["width"] + config["stack"]["offset"]) * 6 + 10, config["bar"]["height"] + 10);
for i in range(len(cards)):
    card = cards[randint(0, len(cards) - 1)]
    deck.add_card(card)
    cards.remove(card)
bar = Bar(window)

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

                # Прокрутка колоды -20, при этом счет уменьшается только до 0 очков
                if deck.is_scrolled():
                    bar.add_score(-20)
                    print("-20 за прокрутку")

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
                        
                        # Открытие карты на стол +5
                        if isinstance(dragged_stack, Stack) and dragged_stack.count() != 0:
                            bar.add_score(5)

                        # Перетаскивание карты из колоды на стол +5
                        if isinstance(dragged_stack, Deck):
                            bar.add_score(5)

                        # Перетаскивание карты из дома на стол -15
                        if isinstance(dragged_stack, Storage):
                            bar.add_score(-15)
                        
                        dragged_heap = None

            for storage in storages:
                if storage.is_in_area(x, y):
                    if storage.is_can_stack(dragged_heap):
                        storage.push_heap(dragged_heap)
                        if dragged_stack.count() > 0:
                            dragged_stack.get_last_card().set_visible(True)

                        # Перетаскивание карты со стола или колоды в дом +10
                        if isinstance(dragged_stack, Stack) or isinstance(dragged_stack, Deck):
                            bar.add_score(10)

                        dragged_heap = None

            if dragged_heap != None:
                dragged_heap.return_prev_coords()
                dragged_stack.push_heap(dragged_heap)
                dragged_heap = None
                dragged_stack = None          
            

    for stack in stacks:
        stack.show()
    for storage in storages:
        storage.show()
    deck.show()
    bar.show()

    if dragged_heap != None:
        dragged_heap.update_coords(x, y)
        dragged_heap.show()


    clock.tick(config["app"]["fps"])
    pygame.display.update()