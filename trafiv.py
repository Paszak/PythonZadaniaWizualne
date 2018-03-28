import time, subprocess
from tkinter import *

class TrafficLights:

    def __init__(self):

        window = Tk()
        window.title("Traffic Light")
        self.czas = 0
        self.timeleft = IntVar()
        self.timeleft.set(4)

        frame = Frame(window)
        frame.pack()

        self.canvas = Canvas(window, width=200, height=400, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(50, 10, 150, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(50, 120, 150, 220, fill="white")
        self.oval_green = self.canvas.create_oval(50, 230, 150, 330, fill="white")

        #self.color.set('R')
        self.canvas.itemconfig(self.oval_red, fill="red")

        start = Button(window, text="start", command=self.loop)
        start.pack()

        window.mainloop()

    def loop(self):
        while self.timeleft.get() > 0:
            self.czas = self.timeleft.get()
            time.sleep(1)
            self.czas = self.czas - 1
            print('jest', self.czas)
            self.timeleft.set(self.czas)
            self.on_RadioChange()

            # if self.timeleft.get() == 0:
            #     self.timeleft.set(4)

    def on_RadioChange(self):
        color = int(self.timeleft.get())
        print('kolor', color)
        if color == 3:
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 2:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 1:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")

TrafficLights()
