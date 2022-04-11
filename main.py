import tkinter
import sys
import maze
import graphics
from tkinter.filedialog import asksaveasfile

sys.setrecursionlimit(1000000)


def draw(current_maze, size):
    graphics.delete_walls(canvas)
    for i in range(current_maze.height + 1):
        for j in range(current_maze.width):
            if current_maze.horizontal_walls[i][j]:
                graphics.walls.append(
                    canvas.create_line(300 + i * 10 * 50 // size, 100 + j * 10 * 50 // size,
                                       300 + 10 * i * 50 // size, 100 + 10 * 50 // size + 10 * j * 50 // size, fill='black'))
    for i in range(current_maze.height):
        for j in range(current_maze.width + 1):
            if current_maze.vertical_walls[i][j]:
                graphics.walls.append(
                    canvas.create_line(300 + i * 10 * 50 // size, 100 + j * 10 * 50 // size,
                                       300 + 10 * 50 // size + 10 * i * 50 // size, 100 + 10 * j * 50 // size, fill='black'))


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
    height, width = check()
    current_maze = maze.Maze(height, int(width))
    current_maze.dfs_generate()
    size = max(height, width)
    draw(current_maze, size)
    btn_download.place(x=800, y=0)


def click_btn_tree():
    height, width = check()
    current_maze = maze.Maze(height, int(width))
    current_maze.tree_generate()
    size = max(height, width)
    draw(current_maze, size)
    btn_download.place(x=800, y=0)


def click_btn_download():
    files = [('PDF Files', '*.pdf'),]
    file = asksaveasfile(filetypes=files, defaultextension=files)


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

btn_download = tkinter.Button(
    text="Download",
    width=20,
    height=3,
    command=click_btn_download
)

window.mainloop()
