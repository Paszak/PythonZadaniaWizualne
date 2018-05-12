
from tkinter import *

okno = Tk()
okno.title("Głowa")
okno.resizable(width=False, height=False)
okno.geometry("500x500")
head = Button(okno, bitmap="questhead", height=50, width=50)
head.place(x=225, y=225, anchor=NW)
val=head.cget("anchor")
okno.mainloop()