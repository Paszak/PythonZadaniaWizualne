
from tkinter import *
from tkinter import messagebox
import random


class Przycisk:
    def __init__(self, gridcol, gridrow,number):
        self.row = gridrow
        self.col = gridcol
        self.number = number

    def przycisk(self):
        global okno
        self.przy = Button(okno, width=5, text=self.number, command=self.click)
        self.przy.grid(row=self.row, column=self.col)

    def click(self):
        self.val = int(self.przy.cget("text"))
        if self.val == min(liczby):
            self.przy.config(state=DISABLED)
            self.position = liczby.index(self.val)
            del liczby[self.position]
        if len(liczby) == 0:
            messagebox.showinfo("Koniec", "Gratulacje, skończyłeś zadanie")


okno = Tk()
okno.title("Klikacz")
liczby = random.sample(range(1000), 25)
num = 0
for i in range(5):
    for j in range(5):
        Przycisk(i, j, liczby[num]).przycisk()
        num += 1
okno.mainloop()
