import cell
import random


class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        maze = [[cell.Cell(_, __, 0) for __ in range(width)] for _ in range(height)]
        self.maze = maze

        horizontal_walls = [[True for __ in range(width)] for _ in range(height + 1)]
        vertical_walls = [[True for __ in range(width + 1)] for _ in range(height)]
        self.horizontal_walls = horizontal_walls
        self.vertical_walls = vertical_walls
        self.solution = []

    def find_neighbors(self, cell):
        neighbors = []
        if cell.x == 0 and cell.y == 0:
            neighbors.append(self.maze[0][1])
            neighbors.append(self.maze[1][0])
        elif cell.x == self.height - 1 and cell.y == self.width - 1:
            neighbors.append(self.maze[cell.x][cell.y - 1])
            neighbors.append(self.maze[cell.x - 1][cell.y])
        elif cell.x == self.height - 1 and cell.y == 0:
            neighbors.append(self.maze[cell.x][1])
            neighbors.append(self.maze[cell.x - 1][0])
        elif cell.x == 0 and cell.y == self.width - 1:
            neighbors.append(self.maze[0][cell.y - 1])
            neighbors.append(self.maze[1][cell.y])
        elif cell.x == 0:
            neighbors.append(self.maze[0][cell.y - 1])
            neighbors.append(self.maze[1][cell.y])
            neighbors.append(self.maze[0][cell.y + 1])
        elif cell.x == self.height - 1:
            neighbors.append(self.maze[cell.x][cell.y - 1])
            neighbors.append(self.maze[cell.x - 1][cell.y])
            neighbors.append(self.maze[cell.x][cell.y + 1])
        elif cell.y == 0:
            neighbors.append(self.maze[cell.x - 1][0])
            neighbors.append(self.maze[cell.x][1])
            neighbors.append(self.maze[cell.x + 1][0])
        elif cell.y == self.width - 1:
            neighbors.append(self.maze[cell.x - 1][cell.y])
            neighbors.append(self.maze[cell.x][cell.y - 1])
            neighbors.append(self.maze[cell.x + 1][cell.y])
        else:
            neighbors.append(self.maze[cell.x - 1][cell.y])
            neighbors.append(self.maze[cell.x][cell.y - 1])
            neighbors.append(self.maze[cell.x + 1][cell.y])
            neighbors.append(self.maze[cell.x][cell.y + 1])

        random.shuffle(neighbors)
        return neighbors

    def dfs(self, x, y):
        if not self.maze[x][y].condition:
            self.maze[x][y].condition = 1
            neighbors = self.find_neighbors(self.maze[x][y])
            for u in neighbors:
                if not u.condition:
                    a, b, direction = self.maze[x][y].find_wall(u)
                    if direction:
                        self.horizontal_walls[a][b] = False
                    else:
                        self.vertical_walls[a][b] = False
                    self.dfs(u.x, u.y)

    def break_wall(self):
        flag = random.randint(0, 1)
        if flag:
            self.vertical_walls[0][0] = False
            self.vertical_walls[self.height - 1][self.width] = False
        else:
            self.horizontal_walls[0][0] = False
            self.horizontal_walls[self.height][self.width - 1] = False

    def find_cells(self, x, y, direction):
        if direction:
            return x, y - 1, x, y
        else:
            return x - 1, y, x, y

    def dfs_generate(self):
        x = random.randint(0, self.height - 1)
        y = random.randint(0, self.width - 1)
        self.dfs(x, y)
        self.break_wall()

    def is_wall(self, cell1, cell2):
        if cell1.x == cell2.x:
            # (cell1.x, cell1.y, cell2.y )
            if self.vertical_walls[cell1.x][max(cell1.y, cell2.y)]:
                return True
            return False

        if self.horizontal_walls[max(cell1.x, cell2.x)][cell1.y]:
            return True
        return False

    def spanning_tree(self, walls):
        count = 1
        for wall in walls:
            x1, y1, x2, y2 = self.find_cells(wall[0], wall[1], wall[2])
            if self.maze[x1][y1].condition != self.maze[x2][y2].condition or not self.maze[x1][y1].condition or not \
                    self.maze[x1][y1].condition:
                if not self.maze[x1][y1].condition and not self.maze[x1][y1].condition:
                    self.maze[x1][y1].condition = count
                    self.maze[x2][y2].condition = count
                    count += 1
                if not self.maze[x1][y1].condition:
                    self.maze[x1][y1].condition = self.maze[x2][y2].condition
                elif not self.maze[x2][y2].condition:
                    self.maze[x2][y2].condition = self.maze[x1][y1].condition
                else:
                    old_condition = self.maze[x1][y1].condition
                    for i in self.maze:
                        for j in i:
                            if j.condition == old_condition:
                                j.condition = self.maze[x2][y2].condition
                if wall[2]:
                    self.vertical_walls[wall[0]][wall[1]] = False
                else:
                    self.horizontal_walls[wall[0]][wall[1]] = False

    def tree_generate(self):
        walls = []
        for i in range(1, self.height):
            for j in range(self.width):
                walls.append((i, j, False))

        for i in range(self.height):
            for j in range(1, self.width):
                walls.append((i, j, True))
        random.shuffle(walls)
        self.spanning_tree(walls)
        self.break_wall()

    def dfs_solve(self, cur_x, cur_y):
        if not self.maze[cur_x][cur_y].used:
            self.maze[cur_x][cur_y].used = True
            neighbours = self.find_neighbors(self.maze[cur_x][cur_y])
            for i in neighbours:
                if not i.used and not self.is_wall(self.maze[cur_x][cur_y], i):
                    i.parent = (cur_x, cur_y)
                    self.dfs_solve(i.x, i.y)

    def solve(self):
        self.dfs_solve(0, 0)
        self.solution.append((self.height - 1, self.width - 1))
        (x, y) = self.maze[self.height - 1][self.width - 1].parent
        while (x, y) != (0, 0):
            self.solution.append((x, y))
            (x, y) = self.maze[x][y].parent
        self.solution.append((0, 0))
