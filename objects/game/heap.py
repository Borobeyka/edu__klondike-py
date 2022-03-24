from objects.glob import *
from objects.game.actions import *

class Heap(Actions):

    def __init__(self, surface, x, y):
        super().__init__(surface, x, y)
        self.cards = []

    def show(self):
        for card in self.cards:
            card.show()

    def count(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def return_prev_coords(self):
        super().return_prev_coords()

        for idx, card in enumerate(self.cards):
            card.x = self.x
            card.y = self.y + idx * config["stack"]["offset"]

    def update_coords(self, x, y):
        super().update_coords(x, y)

        for idx, card in enumerate(self.cards):
            card.x = self.x
            card.y = self.y + idx * config["stack"]["offset"]