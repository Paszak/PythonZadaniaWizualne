
from tkinter import *

okno = Tk()
okno.title("Bitowiec")


def licz():
    global wynik
    suma = int(prze7.get()*(2**7)) + int(prze6.get()*(2**6)) + int(prze5.get()*(2**5)) + int(prze4.get()*(2**4)) +\
           int(prze3.get()*(2**3)) + int(prze2.get()*(2**2)) + int(prze1.get()*(2**1)) + int(prze0.get()*(2**0))
    suma = str(suma)
    wynik.set(suma)


frame = Frame(okno)
frame.pack()

bottomframe = Frame(okno)
bottomframe.pack(side=BOTTOM)

prze7 = IntVar()
prze6 = IntVar()
prze5 = IntVar()
prze4 = IntVar()
prze3 = IntVar()
prze2 = IntVar()
prze1 = IntVar()
prze0 = IntVar()
wynik = StringVar()

c7 = Checkbutton(frame, text="7", variable=prze7, command=licz).pack(side=LEFT)
c6 = Checkbutton(frame, text="6", variable=prze6, command=licz).pack(side=LEFT)
c5 = Checkbutton(frame, text="5", variable=prze5, command=licz).pack(side=LEFT)
c4 = Checkbutton(frame, text="4", variable=prze4, command=licz).pack(side=LEFT)
c3 = Checkbutton(frame, text="3", variable=prze3, command=licz).pack(side=LEFT)
c2 = Checkbutton(frame, text="2", variable=prze2, command=licz).pack(side=LEFT)
c1 = Checkbutton(frame, text="1", variable=prze1, command=licz).pack(side=LEFT)
c0 = Checkbutton(frame, text="0", variable=prze0, command=licz).pack(side=LEFT)

show = Label(bottomframe, textvariable=wynik, fg ="blue", font=("Arial", 36, "bold")).pack()
przycisk = Button(bottomframe, text="Koniec", command=okno.destroy).pack()
okno.mainloop()
