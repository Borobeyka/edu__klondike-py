import pygame

from objects.glob import *
from objects.actions import *
from objects.heap import *

class Storage(Actions):

    TOTAL_CARDS = 0

    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
        self.cards = []

    def count(self):
        return len(self.cards)

    def is_empty(self):
        return False if self.count() > 0 else True
    
    def show(self):
        if self.is_empty():
            surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)
            
            pygame.draw.rect(surface, config["color"]["darkgreen"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                border_radius=config["card"]["radius"])
            pygame.draw.rect(surface, config["color"]["lightgreen"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                2, config["card"]["radius"])
            self.surface.blit(surface, (self.x, self.y))
        else:
            self.get_last_card().show()

    def is_in_area(self, x, y):
        if (x > self.x and x < self.x + config["card"]["width"] and
            y > self.y and y < self.y + config["card"]["height"]):
            return True
        return False

    def get_last_card(self):
        return self.cards[-1]

    def is_can_stack(self, heap):
        head_card = heap.cards[0]
        if self.is_empty() and head_card.nominal != 0:
            return False
        if self.count() >= 1 and (self.get_last_card().suit != head_card.suit or
            head_card.nominal - self.get_last_card().nominal != 1):
            return False
        if heap.count() > 1:
            return False
        return True
    
    def get_heap_on_focus(self, x, y):
        card = self.get_last_card()
        heap = Heap(self.surface, card.x, card.y)
        heap.mouse_offset_x = abs(x - card.x)
        heap.mouse_offset_y = abs(y - card.y)
        heap.add_card(card)
        self.cards.remove(card)
        Storage.TOTAL_CARDS -= 1
        return heap

    def push_heap(self, heap):
        heap.cards[0].x = self.x
        heap.cards[0].y = self.y
        self.cards.append(heap.cards[0])
        Storage.TOTAL_CARDS += 1
    
    @staticmethod
    def is_game_completed():
        if Storage.TOTAL_CARDS == 52:
            return True
        return False