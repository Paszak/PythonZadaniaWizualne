
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title("Kalkulatorek")


def Oblicz():
    global wyświetlaczStr1, wyświetlaczStr2, r1
    lewa_war= int(wyświetlaczStr1.get())
    prawa_war = int(wyświetlaczStr2.get())
    print(lewa_war, prawa_war, r1.get()) #sprawdzam co otrzymuję
    if r1.get() == 0:
        wynik = lewa_war + prawa_war
    elif r1.get() == 1:
        wynik = lewa_war - prawa_war
    elif r1.get() == 2:
        if prawa_war == 0:
            messagebox.showinfo("Błąd", "Nie można dzielić przez zero")
            wynik = False
        else:
            wynik = lewa_war / prawa_war
    elif r1.get() == 3:
        wynik = lewa_war * prawa_war
    if wynik:
        messagebox.showinfo("Wynik", 'Wynikiem działania jest: ' + str(wynik))

def tylkocyfry(*a):
    global wyświetlaczStr1, pop_s1
    s = wyświetlaczStr1.get()
    if s == '' or s.isdigit():
        pop_s1 = s
    else:
        wyświetlaczStr1.set(pop_s1)

def tylkocyfry2(*a):
    global wyświetlaczStr2, pop_s2
    s = wyświetlaczStr2.get()
    if s == '' or s.isdigit():
        pop_s2 = s
    else:
        wyświetlaczStr2.set(pop_s2)

pop_s1 = ''
pop_s2 = ''

wyświetlaczStr1 = StringVar()
wyświetlaczStr1.set("")
wyświetlaczStr2 = StringVar()
wyświetlaczStr2.set("")

wyświetlaczStr1.set(pop_s1)
wyświetlaczStr1.trace('w', tylkocyfry)

wyświetlaczStr2.set(pop_s2)
wyświetlaczStr2.trace('w', tylkocyfry2)
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
