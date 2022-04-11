class Graphics:
    def __init__(self):
        self.walls = []

    def delete_walls(self, canvas):
        for wall in self.walls:
            canvas.delete(wall)
