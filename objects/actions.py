class Actions:

    def __init__(self, x, y):
        self.x = self.old_x = x
        self.y = self.old_y = y
        self.mouse_offset_x = 0
        self.mouse_offset_y = 0
        #print(self.mouse_offset_x, self.mouse_offset_y)

    def update_coords(self, x, y):
        self.x = x - self.x - self.mouse_offset_x
        self.y = y - self.y - self.mouse_offset_y

    def return_prev_coords(self):
        self.x = self.old_x
        self.y = self.old_y

    def return_old_coords(self):
        self.x = self.old_x
        self.y = self.old_y

    def save_old_coords(self):
        self.oldold_xX = self.x
        self.old_y = self.y