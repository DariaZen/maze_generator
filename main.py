import tkinter
import sys
import maze
import graphics

sys.setrecursionlimit(1000000)

count = 0
current_maze = maze.Maze(5, 5)


def draw(size):
    global current_maze
    graphics.delete_walls(canvas)
    graphics.delete_solution(canvas)
    for i in range(current_maze.height + 1):
        for j in range(current_maze.width):
            if current_maze.horizontal_walls[i][j]:
                graphics.walls.append(
                    canvas.create_line(300 + i * 10 * 50 // size, 100 + j * 10 * 50 // size,
                                       300 + 10 * i * 50 // size, 100 + 10 * 50 // size + 10 * j * 50 // size,
                                       fill='black'))
    for i in range(current_maze.height):
        for j in range(current_maze.width + 1):
            if current_maze.vertical_walls[i][j]:
                graphics.walls.append(
                    canvas.create_line(300 + i * 10 * 50 // size, 100 + j * 10 * 50 // size,
                                       300 + 10 * 50 // size + 10 * i * 50 // size, 100 + 10 * j * 50 // size,
                                       fill='black'))


def draw_solution(size):
    global current_maze
    for i in current_maze.solution:
        x = 10 * 50 // (4 * size)
        graphics.solution.append(
            canvas.create_oval(x + 300 + i[0] * 10 * 50 // size, x + 100 + i[1] * 10 * 50 // size,
                               -x + 300 + 10 * 50 // size + 10 * i[0] * 50 // size,
                               -x + 100 + 10 * 50 // size + 10 * i[1] * 50 // size,
                               outline='green',
                               fill='green'))


def check():
    try:
        height = int(ent_height.get())
        if not (2 <= height <= 50):
            height = 50
    except:
        height = 50

    try:
        width = int(ent_width.get())
        if not (2 <= width <= 50):
            width = 50
    except:
        width = 50

    return height, width


def click_btn_dfs():
    global current_maze
    height, width = check()
    current_maze = maze.Maze(width, height)
    current_maze.dfs_generate()
    size = max(height, width)
    draw(size)
    btn_sol['text'] = "Show solution"
    btn_sol.place(x=800, y=0)


def click_btn_tree():
    global current_maze
    height, width = check()
    current_maze = maze.Maze(width, height)
    current_maze.tree_generate()
    size = max(height, width)
    draw(size)
    btn_sol['text'] = "Show solution"
    btn_sol.place(x=800, y=0)


def click_btn_download():
    name = "my_maze"
    global count
    if count == 0:
        f = open(name + ".txt", "w+")
    else:
        f = open(name + str(count) + ".txt", "w+")
    count += 1
    f.close()


def click_btn_sol():
    global current_maze
    if btn_sol['text'] == "Show solution":
        current_maze.solve()
        size = max(current_maze.width, current_maze.height)
        draw_solution(size)
        btn_sol['text'] = "Hide solution"
    else:
        graphics.delete_solution(canvas)
        btn_sol['text'] = "Show solution"


graphics = graphics.Graphics()
window = tkinter.Tk()
window.title("Maze generator")
canvas = tkinter.Canvas(bg="white", width=1200, height=1200)
canvas.pack()

lbl_height = tkinter.Label(text="Choose height (from 2 to 50)")
ent_height = tkinter.Entry(window)
lbl_height.place(x=0, y=0)
ent_height.place(x=0, y=20)
lbl_width = tkinter.Label(text="Choose width (from 2 to 50)")
ent_width = tkinter.Entry(window)
lbl_width.place(x=200, y=0)
ent_width.place(x=200, y=20)

btn_dfs = tkinter.Button(
    text="Generate using DFS",
    width=20,
    height=3,
    command=click_btn_dfs
)
btn_dfs.place(x=400, y=0)

btn_tree = tkinter.Button(
    text="Generate using spanning tree",
    width=20,
    height=3,
    command=click_btn_tree
)
btn_tree.place(x=600, y=0)

btn_sol = tkinter.Button(
    text="Show solution",
    width=20,
    height=3,
    command=click_btn_sol
)

window.mainloop()
