import pygame

from objects.glob import *
from objects.actions import *
from objects.heap import *

class Stack(Actions):

    def __init__(self, surface, x, y):
        self.surface = surface
        super().__init__(x, y)
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

        else:
            for card in self.cards:
                card.show()

        self.surface.blit(surface, (self.x, self.y))
    
    def is_in_area(self, x, y):
        if (x > self.x and x < self.x + config["card"]["width"] and
            y > self.y and y < self.y + config["card"]["height"] +
            (self.count() == 1 or 0 if self.count() == 0 else (self.count() - 1) * config["stack"]["offset"])):
            # self.mouse_offset_x = abs(x - self.x)
            # self.mouse_offset_y = abs(y - self.y)
            return True
        return False
    
    def is_can_stack(self, heap):
        if(self.is_empty() and heap.cards[0].nominal != 12):
            return False
        if(self.count() >= 1 and (self.get_last_card().icon_color == heap.cards[0].iconColor or
            self.get_last_card().nominal - heap.cards[0].nominal != 1)):
            return False
        return True
    
    def get_last_card(self):
        return self.cards[-1]


    def get_heap_on_focus(self, x, y):
        for card in self.cards[::-1]:
            if card.is_in_area(x, y) and card.is_visible:
                heap = Heap(card.x, card.y)
                index = self.cards.index(card)

                for idx, card in enumerate(self.cards):
                    if idx >= index:
                        heap.add_card(card)
                self.cards.pop(index)
        
    def push_heap(self, heap):
        for card in heap.cards:
            card.x = self.x
            card.y = self.y + self.count() * config["stack"]["offset"]

    def push_card(self, card):
        cards.pop(card)
        card.x = self.x;
        card.y = self.y + self.count() * config.stack.offset;
        self.card.append(card)

    def add_card(self, card):
        if self.is_empty() and card.nominal != 12:
            return
        if self.count() >= 1 and (self.get_last_card().icon_color == card.icon_color or
            self.get_last_card().nominal - card.nominal != 1):
            return
        card.x = self.x
        card.y = self.y + self.count() * config["stack"]["offset"]
        self.cards.append(card)