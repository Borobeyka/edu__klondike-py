from objects.stack import *
from objects.deck import *
from objects.storage import *

class Canceler:
    def __init__(self):
        self.is_can_cancel = False
        pass

    def save_last_move(self, stack, d_stack, heap):
        self.stack = stack
        self.d_stack = d_stack
        self.heap = heap
        self.is_can_cancel = True

    def return_last_move(self, bar):
        if(isinstance(self.stack, Stack) and self.stack.count() != 0):
            self.stack.get_last_card().set_visible(False)
        
        if isinstance(self.stack, Stack) and self.stack.count() > 0 and isinstance(self.d_stack, Stack):
            bar.add_score(-5)
        if isinstance(self.stack, Deck) and isinstance(self.d_stack, Stack):
            bar.add_score(-5)
        if (isinstance(self.stack, Stack) or isinstance(self.stack, Deck)) and isinstance(self.d_stack, Storage):
            bar.add_score(-10)
        if isinstance(self.stack, Deck) and isinstance(self.d_stack, Stack):
            bar.add_score(15)

        if isinstance(self.stack, Deck):
            self.stack.push_heap(self.heap, True)
        else:
            self.stack.push_heap(self.heap)
        del self.d_stack.cards[-self.heap.count()]
        self.is_can_cancel = False

    def is_can_canceled(self):
        return self.is_can_cancel
    
    def reset(self):
        self.stack = self.d_stack = self.heap = None
        self.is_can_cancel = False