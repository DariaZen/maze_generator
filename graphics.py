class Graphics:
    def __init__(self):
        self.walls = []
        self.solution = []

    def delete_walls(self, canvas):
        for wall in self.walls:
            canvas.delete(wall)

    def delete_solution(self, canvas):
        for cell in self.solution:
            canvas.delete(cell)
