class Cell:
    def __init__(self, x, y, condition):
        self.x = x
        self.y = y
        self.condition = condition

    def find_wall(self, other):
        if other.x == self.x:
            y = min(other.y, self.y)
            return other.x, y + 1, False
        elif other.y == self.y:
            x = min(other.x, self.x)
            return x + 1, other.y, True
