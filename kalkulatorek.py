
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title("Kalkulatorek")


def Oblicz():
    global wyświetlaczStr1, wyświetlaczStr2, r1
    lewaWar= int(wyświetlaczStr1.get())
    prawaWar = int(wyświetlaczStr2.get())
    print(lewaWar, prawaWar, r1.get()) #sprawdzam co otrzymuję
    if r1.get() == 0:
        wynik = lewaWar + prawaWar
    elif r1.get() == 1:
        wynik = lewaWar - prawaWar
    elif r1.get() == 2:
        if prawaWar == 0:
            messagebox.showinfo("Błąd", "Nie można dzielić przez zero")
            wynik = False
        else:
            wynik = lewaWar / prawaWar
    elif r1.get() == 3:
        wynik = lewaWar * prawaWar
    if wynik:
        messagebox.showinfo("Wynik", 'Wynikiem działania jest: ' + str(wynik))

def tylkocyfry(*a):
    global wyświetlaczStr1, pop_s
    s = wyświetlaczStr1.get()
    if s == '' or s.isdigit():
        pop_s = s
    else:
        wyświetlaczStr1.set(pop_s)

pop_s = ''
wyświetlaczStr1 = StringVar()
wyświetlaczStr1.set("")
wyświetlaczStr2 = StringVar()
wyświetlaczStr2.set("")

wyświetlaczStr1.set(pop_s)
wyświetlaczStr1.trace('w', tylkocyfry)
tc = okno.register(tylkocyfry)


wyświetlacz1 = Entry(okno, width=5, font=("Courier New", "12", "bold"), textvariable=wyświetlaczStr1, justify=LEFT)
wyświetlacz2 = Entry(okno, width=5, font=("Courier New", "12", "bold"), textvariable=wyświetlaczStr2, justify=LEFT)

r1 = IntVar()
r2 = IntVar()
r3 = IntVar()
r4 = IntVar()
oblicz = Button(okno, text="Oblicz", command=Oblicz)
dodawanie = Radiobutton(okno, text="+", variable=r1, value=0)
odejmowanie = Radiobutton(okno, text="-", variable=r1, value=1)
dzielenie = Radiobutton(okno, text="/", variable=r1, value=2)
mnożenie = Radiobutton(okno, text="*", variable=r1, value=3)

dodawanie.grid(row=0, column=1)
odejmowanie.grid(row=1, column=1)
dzielenie.grid(row=2, column=1)
mnożenie.grid(row=3, column=1)
wyświetlacz1.grid(row=0, column=0, rowspan=5)
wyświetlacz2.grid(row=0, column=2, rowspan=5)
oblicz.grid(row=5, column=1)

okno.mainloop()
