
from tkinter import *


def left(event):
    global positionX, positionY
    if positionX > 0:
        positionX = positionX - 1
        head.place(x=positionX, y=positionY)

def right(event):
    global positionX, positionY
    if positionX < 445:
        positionX = positionX + 1
        head.place(x=positionX, y=positionY)

def down(event):
    global positionX, positionY
    if positionY < 445:
        positionY = positionY + 1
        head.place(x=positionX, y=positionY)

def up(event):
    global positionX, positionY
    if positionY > 0:
        positionY = positionY - 1
        head.place(x=positionX, y=positionY)

def cleft(event):
    global positionX, positionY
    if positionX > 0:
        positionX = positionX - 5
        head.place(x=positionX, y=positionY)

def cright(event):
    global positionX, positionY
    if positionX < 445:
        positionX = positionX + 5
        head.place(x=positionX, y=positionY)

def cdown(event):
    global positionX, positionY
    if positionY < 445:
        positionY = positionY + 5
        head.place(x=positionX, y=positionY)

def cup(event):
    global positionX, positionY
    if positionY > 0:
        positionY = positionY - 5
        head.place(x=positionX, y=positionY)


positionX = 225
positionY = 225
okno = Tk()
okno.title("Głowa")
okno.resizable(width=False, height=False)
okno.geometry("500x500")
head = Button(okno, bitmap="questhead", height=50, width=50)
head.place(x=positionX, y=positionY, anchor=NW)

okno.bind("<Left>", left)
okno.bind("<Right>", right)
okno.bind("<Down>", down)
okno.bind("<Up>", up)

okno.bind("<Control-Left>", cleft)
okno.bind("<Control-Right>", cright)
okno.bind("<Control-Down>", cdown)
okno.bind("<Control-Up>", cup)

okno.mainloop()
