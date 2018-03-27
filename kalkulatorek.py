
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title("Kalkulatorek")

def Oblicz():
    return True





wyświetlaczStr = StringVar()
wyświetlaczStr.set("")
wyświetlacz1 = Entry(okno, width=5, font=("Courier New", "12", "bold"), textvariable=wyświetlaczStr, justify=LEFT)
wyświetlacz2 = Entry(okno, width=5, font=("Courier New", "12", "bold"), textvariable=wyświetlaczStr, justify=LEFT)
przycisk = Button(okno, text="Oblicz", command=Oblicz)
dodawanie = Radiobutton(okno, text="+", variable=)
odejmowanie
mnożenie
dzielenie
wyświetlacz1.grid(row=2, column=0)
wyświetlacz2.grid(row=2, column=2)
przycisk.grid(row=5, column=1)

okno.mainloop()
