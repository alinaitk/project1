# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width = 300, height = 500)
# canvas.pack()
# rect = canvas.create_rectangle(100,100,150,200, fill = 'red')
# lines = canvas.create_line(90,500,90,0, fill = 'green')
# lines = canvas.create_line(180,500,180,0, fill = 'green')
# def move_circle(event):
#     if event.keysym == 'Up':
#         canvas.move(rect,0,-10)
#     elif event.keysym == 'Down':
#         canvas.move(rect,0,10)
#     elif event.keysym == 'Right':
#         canvas.move(rect,5,0)
#     elif event.keysym == 'Left':
#         canvas.move(rect,-5,0)
# list1 = ['<Up>', '<Down>', '<Left>', '<Right>']
# for x in range(0,len(list1)):
#     canvas.bind_all(list1[x], move_circle)
#
# tk.mainloop()
#
# from tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=500)
# canvas.pack()
# house = canvas.create_rectangle(100, 300, 200, 350, fill='white')
# ground = canvas.create_rectangle(0, 350, 400, 500, fill='green')
# sun = canvas.create_oval(300, 100, 400, 200, fill='yellow')
# roof = canvas.create_polygon(100, 300, 150, 250, 200, 300, fill='brown')
# cloud = canvas.create_oval(30, 100, 100, 150, fill='white')
# cloud2 = canvas.create_oval(150, 20, 250, 80, fill='blue')
# door = canvas.create_rectangle(140, 350, 160, 315, fill='pink')
# window = canvas.create_rectangle(110, 325, 125, 345, fill='blue')
# window2 = canvas.create_rectangle(175, 325, 190, 345, fill='blue')
# tk.mainloop()
import random
import time
from tkinter import *
tk = Tk()
tk.title('jumping ball')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
tk.update()
class Ball:
    def __init__(self, canvas, colour, paddle, score):
        self.canvas = canvas
        self.score = score
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=colour)
        self.canvas.move(self.id, 250, 150)
        self.canvaswidth = self.canvas.winfo_width()
        self.canvasheight = self.canvas.winfo_height()
        list1 = [-3, -2, -1, 1, 2, 3]
        random.shuffle(list1)
        self.x = list1[0]
        self.y = -1
        self.bottom = False

    def draw_circle(self):
        self.canvas.move(self.id, self.x, self.y)
        coord = self.canvas.coords(self.id)
        if coord[1] <= 0:
            self.y = -self.y
        elif coord[0] <= 0 or coord[2] >= self.canvaswidth:
            self.x = -self.x
        elif self.hit_paddle(coord):
            self.y = -self.y
        elif coord[3] >= self.canvasheight:
            self.bottom = True

    def hit_paddle(self, coord):
        i = self.canvas.coords(self.paddle.id)
        if coord[2] >= i[0] and coord[0] <= i[2]:
           if i[3] >= coord[3] >= i[1]:
               self.score.app_score()
               return True
        return False


class Paddle:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=colour)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvaswidth = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)

    def turn_right(self, event):
        coord = self.canvas.coords(self.id)
        if coord[2] <= self.canvaswidth:
            self.x = 2

    def turn_left(self, event):
        coord = self.canvas.coords(self.id)
        if coord[0] > 0:
            self.x = -2

    def draw_rectangle(self):
        self.canvas.move(self.id, self.x, 0)
        coord = self.canvas.coords(self.id)
        if coord[0] <= 0 or coord[2] >= self.canvaswidth:
            self.x = 0


class Points:
    def __init__(self, canvas, colour):
        self.canvas = canvas
        self.colour = colour
        self.score = 0
        self.id = canvas.create_text(100, 40, text=self.score, fill=self.colour)

    def app_score(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)


rect1 = Paddle(canvas, 'yellow')
sc1 = Points(canvas, 'pink')
ball1 = Ball(canvas, 'red', rect1, sc1)
print(rect1.canvaswidth)
while 1:
    if not ball1.bottom:
        ball1.draw_circle()
        rect1.draw_rectangle()
    else:
        window = Toplevel(tk)
        window.title('jumping ball')
        window.resizable(0, 0)
        window.wm_attributes('-topmost', 1)
        canvas2 = Canvas(window, width=100, height=300)
        canvas2.create_text(50, 130, text="you've lost")
        canvas2.pack()
        window.update()
        time.sleep(3)
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)



