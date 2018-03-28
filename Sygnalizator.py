import time
from tkinter import *


okno = Tk()
okno.title("Sygnalizacja")
timeleft = IntVar()
timeleft.set(3)


def loop():
    if timeleft.get() > 0:
        czas = timeleft.get()
        czas = czas - 1
        timeleft.set(czas)
        Zmiana()
        canvas.after(1000, loop)
        if timeleft.get() == 0:
            timeleft.set(4)


def Zmiana():
    color = int(timeleft.get())
    if color == 3:
        canvas.itemconfig(oval_red, fill="red")
        canvas.itemconfig(oval_yellow, fill="white")
        canvas.itemconfig(oval_green, fill="white")
    elif color == 2:
            canvas.itemconfig(oval_red, fill="red")
            canvas.itemconfig(oval_yellow, fill="yellow")
            canvas.itemconfig(oval_green, fill="white")
    elif color == 1:
        canvas.itemconfig(oval_red, fill="white")
        canvas.itemconfig(oval_yellow, fill="white")
        canvas.itemconfig(oval_green, fill="green")
    elif color == 0:
        canvas.itemconfig(oval_red, fill="white")
        canvas.itemconfig(oval_yellow, fill="yellow")
        canvas.itemconfig(oval_green, fill="white")


frame = Frame(okno)
frame.pack()

canvas = Canvas(okno, width=200, height=350, bg="white")
canvas.pack()
canvas.after(1000, loop)

oval_red = canvas.create_oval(50, 10, 150, 110, fill="white")
oval_yellow = canvas.create_oval(50, 120, 150, 220, fill="white")
oval_green = canvas.create_oval(50, 230, 150, 330, fill="white")
canvas.itemconfig(oval_red, fill="red")

okno.mainloop()


