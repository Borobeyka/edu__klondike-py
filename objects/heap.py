from objects.glob import *
from objects.actions import *

class Heap(Actions):

    def __init__(self, surface, x, y):
        self.surface = surface
        super().__init__(x, y)
        self.cards = []

    def show(self):
        for card in self.cards:
            card.show()

    def count(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def return_prev_coords(self):
        self.x = self.oldX
        self.y = self.oldY

        for idx, card in enumerate(self.cards):
            card.x = self.x
            card.y = self.y + idx * config["stack"]["offset"]

    def saveOldCoords(self):
        self.oldX = self.x
        self.oldY = self.y

    def updateCoords(self, x, y):
        super().update_coords(x, y)

        for idx, card in enumerate(self.cards):
            card.x = self.x
            card.y = self.y + idx * config["stack"]["offset"]