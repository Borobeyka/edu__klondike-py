import pygame

from objects.glob import *
from objects.actions import *
from objects.heap import *

class Deck(Actions):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
        self.cards = []
        self.current_card_index = None

    def add_card(self, card):
        card.x = self.x
        card.y = self.y
        card.set_visible(False)
        self.cards.append(card)
    
    def show(self):

        if self.current_card_index != None and self.current_card_index <= self.count():
            self.cards[self.current_card_index].show()
        elif self.current_card_index == None:
            for card in self.cards:
                card.x = self.x
                card.set_visible(False)
        
        if int(self.current_card_index or 0) + 1 < self.count():
            next_card = self.cards[int(self.current_card_index or 0) + 1]
            next_card.set_visible(False)
            next_card.show()

        if int(self.current_card_index or 0) + 1 >= self.count():
            surface = pygame.Surface((config["card"]["width"], config["card"]["height"]), pygame.SRCALPHA)
                
            pygame.draw.rect(surface, config["color"]["darkgreen"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                border_radius=config["card"]["radius"])
            pygame.draw.rect(surface, config["color"]["lightgreen"],
                (0, 0, config["card"]["width"], config["card"]["height"]),
                2, config["card"]["radius"])
            self.surface.blit(surface, (self.x, self.y))
    
    def is_in_area(self, x, y):
        if (x > self.x and x < self.x + config["card"]["width"] and
            y > self.y and y < self.y + config["card"]["height"]):
            return True
        return False

    def count(self):
        return len(self.cards)
    
    def pick_card(self):
        if self.current_card_index == None:
            self.current_card_index = 0;
        else:
            self.current_card_index += 1

        if self.current_card_index >= self.count():
            self.current_card_index = None
        else:
            self.cards[self.current_card_index].set_visible(True);
            self.cards[self.current_card_index].x -= config["card"]["width"] + config["stack"]["offset"];

    def get_heap_on_focus(self, x, y):
        card = self.cards[self.current_card_index]
        heap = Heap(self.surface, card.x, card.y)
        heap.mouse_offset_x = abs(x - card.x)
        heap.mouse_offset_y = abs(y - card.y)
        card.set_visible(True)
        heap.add_card(card)
        self.cards.remove(card)
        if self.current_card_index == self.count():
            self.current_card_index += 1
        return heap

    def push_heap(self, heap):
        if int(self.current_card_index or 0) + 1 > self.count():
            self.current_card_index -= 1
        self.cards.insert(self.current_card_index, heap.cards[0])

    
    def get_last_card(self):
        return self.cards[-1]