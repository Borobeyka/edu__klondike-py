class Actions:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mouse_offset_x = abs(x - self.x)
        self.mouse_offset_y = abs(y - self.y)

    def update_coords(self, x, y):
        self.x += x - self.x - self.mouse_offset_x
        self.y += y - self.y - self.mouse_offset_y