import tkinter
import time
import random
from life import life


def create_animation_window(animation_window_width, animation_window_height):
  window = tkinter.Tk()
  window.title("Game of life")
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window

def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas

colors = ["black", "gray"]

def fill_matrix(canvas, matrix, m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            canvas.itemconfig(matrix[y][x], fill=colors[m[y][x]])
  
def animate_ball(window, canvas, m):
    
    h = len(m)
    w = len(m[0]) if h > 0 else 0
    matrix = []
    i = -1
    for y in range(h):
        i += 1
        line = []
        j = -1
        for x in range(w):
            j += 1
            line.append(canvas.create_rectangle(start_x + j * rect_w, start_y + i * rect_h, 
                        start_x + (j + 1) * rect_w, start_y + (i + 1) * rect_h, 
                        fill="black", outline="#303030", width=1))
        matrix.append(line)

    fill_matrix(canvas, matrix, m)
    window.update()
    time.sleep(animation_refresh_seconds * 5)
    
    while True:
        m = life(m)
        fill_matrix(canvas, matrix, m)
        window.update()
        time.sleep(animation_refresh_seconds)


# m = [
    # "................",
    # "................",
    # "................",
    # "................",
    # "................",
    # "..........X..X..",
    # ".X.X..........X.",
    # "..XX......X...X.",
    # "..X........XXXX.",
    # "................",
# ]
# area_x = 35
# area_y = 20
# rect_h = 15
# rect_w = 15
# animation_refresh_seconds = 0.2


m = [
    ".............................................................................",
    "..............X...............................................X..............",
    "....XXX.....X..X.............................................X..X.....XXX....",
    ".....XXX....X..X.............................................X..X....XXX.....",
    ".............X.................................................X.............",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    "...XX...................................................................XX...",
    "...XX...................................................................XX...",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    ".............................................................................",
    "....................................X........................................",
    "....................................X........................................",
    "...................................X.X.......................................",
    "....................................X........................................",
    ".XX...XX............................X................................XX...XX.",
    "....................................X........................................",
    "..X...X...........XX................X................XX...............X...X..",
    "...XXX............X................X.X................X................XXX...",
    "...XXX...............X..............X..............X...................XXX...",
    "....................XX..............X..............XX........................",
    ".............................................................................",
    "......X...............................................................X......",
    ".....XXX.............................................................XXX.....",
    "....X...X...........................................................X...X....",
    "......X...............................................................X......",
    "...X.....X......................XXX...XXX..........................X.....X...",
    "...X.....X.........................................................X.....X...",
    "....X...X............X........X....X.X....X........X................X...X....",
    ".....XXX.............X........X....X.X....X........X.................XXX.....",
    ".....................X........X....X.X....X........X.........................",
    "................................XXX...XXX....................................",
    ".................XXX...XXX.....................XXX...XXX.....................",
    "................................XXX...XXX....................................",
    ".....................X........X....X.X....X........X.........................",
    ".....................X........X....X.X....X........X.........................",
    ".....................X........X....X.X....X........X.........................",
    ".............................................................................",
    ".....XX.........................XXX...XXX.............................XX.....",
    ".....XX...............................................................XX.....",
    ".............................................................................",
]
area_x = 70
area_y = 55
rect_h = 7
rect_w = 7
animation_refresh_seconds = 0.001


m = [[1 if c == 'X' else 0 for c in line] for line in m]

add_x = area_x - len(m[0])
add_y = area_y - len(m)
for y in range(len(m)):
    for _ in range(add_x):
        m[y].append(0)
line_len = len(m[0])
for _ in range(add_y):
    m.append([0] * line_len)

start_y = 30
start_x = 30

animation_window_width = len(m[0]) * rect_w + start_x * 2 + 7
animation_window_height= len(m) * rect_h + start_y * 2 + 7
 
animation_window = create_animation_window(animation_window_width, animation_window_height)
animation_canvas = create_animation_canvas(animation_window)
animate_ball(animation_window, animation_canvas, m)

animation_window.mainloop()
  
