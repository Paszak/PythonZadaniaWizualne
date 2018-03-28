
from tkinter import *
from tkinter import messagebox

okno = Tk()
okno.title("PESEL")


def ObliczPesel():
    global wyświetlaczStr
    pesel = wyświetlaczStr.get()
    dlugosc_pesel = len(wyświetlaczStr.get())

    if dlugosc_pesel != 11:
        messagebox.showinfo("Błąd", "Został wprowadzony błędny pesel, sprawdź czy długość wynosi 11 albo czy nie znajdują się cyfry")

    else:
        suma_kontrolna = int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) + 9 * int(pesel[3]) + int(
        pesel[4]) + 3 * int(
        pesel[5]) + 7 * int(pesel[6]) + 9 * int(pesel[7]) + int(pesel[8]) + 3 * int(pesel[9]) + int(pesel[10])
        suma_kontrolna = str(suma_kontrolna)

        if suma_kontrolna[-1] != '0':
            messagebox.showinfo("Błąd","Suma kontrolna się nie zgadza, twój PESEL jest fałszywy!!!")
        else:
            messagebox.showinfo("Zgadza się", "Twój PESEL jest poprawyny")


def tylkocyfry(*a):
    global wyświetlaczStr, pop_s
    s = wyświetlaczStr.get()
    if s == '' or s.isdigit():
        pop_s = s
    else:
        wyświetlaczStr.set(pop_s)

pop_s = ''
wyświetlaczStr = StringVar()
wyświetlaczStr.set("")
tc = okno.register(tylkocyfry)
wyświetlaczStr.set(pop_s)
wyświetlaczStr.trace('w', tylkocyfry)
wyświetlacz = Entry(okno, width=11, font=("Courier New", "12", "bold"), textvariable=wyświetlaczStr, justify=LEFT)
przycisk = Button(okno, text="Sprawdź", command=ObliczPesel)
Label(okno, text="PESEL:").grid(row=0, column=0)
wyświetlacz.grid(row=0, column=1)
przycisk.grid(row=1, column =1)

okno.mainloop()
