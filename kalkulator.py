from tkinter import *

Suma = 0

def Kasuj():
    global wyświetlaczStr,Suma
    wyświetlaczStr.set("0")
    Suma = 0

def Cyfra0():
    global wyświetlaczStr
    s = wyświetlaczStr.get()
    if(len(s) < 10 and s != '0'):
        s = s + '0'
        wyświetlaczStr.set(s)

def Cyfra(c):
    global wyświetlaczStr
    s = wyświetlaczStr.get()
    if(len(s) < 10):
        if(s == '0'):
            s = c
        else:
            s = s + c
        wyświetlaczStr.set(s)

def Plus():
    global wyświetlaczStr, Suma
    s = wyświetlaczStr.get()
    if(s != '0'):
        Suma = int(s)
    else:
        Suma = Suma + int(s)
    wyświetlaczStr.set(str("0"))

def RównaSię():
    global wyświetlaczStr, Suma
    s = wyświetlaczStr.get()
    Suma = Suma + int(s)
    wyświetlaczStr.set(str(Suma))

def Cyfra1():
    Cyfra('1')

def Cyfra2():
    Cyfra('2')

def Cyfra3():
    Cyfra('3')

def Cyfra4():
    Cyfra('4')

def Cyfra5():
    Cyfra('5')

def Cyfra6():
    Cyfra('6')

def Cyfra7():
    Cyfra('7')

def Cyfra8():
    Cyfra('8')

def Cyfra9():
    Cyfra('9')

okno = Tk()    
wyświetlaczStr = StringVar()
wyświetlaczStr.set("0")
wyświetlacz = Entry(okno, width=10, font=("Courier New","12", "bold"),textvariable=wyświetlaczStr,justify=RIGHT)
wyświetlacz.grid(row=0,columnspan=3)

cyfra7 = Button(okno, text="7",command=Cyfra7)
cyfra7.grid(row=1,column=0)

cyfra8 = Button(okno, text="8",command=Cyfra8)
cyfra8.grid(row=1,column=1)

cyfra9 = Button(okno, text="9",command=Cyfra9)
cyfra9.grid(row=1,column=2)

cyfra4 = Button(okno, text="4",command=Cyfra4)
cyfra4.grid(row=2,column=0)

cyfra5 = Button(okno, text="5",command=Cyfra5)
cyfra5.grid(row=2,column=1)

cyfra6 = Button(okno, text="6",command=Cyfra6)
cyfra6.grid(row=2,column=2)

cyfra1 = Button(okno, text="1",command=Cyfra1)
cyfra1.grid(row=3,column=0)

cyfra2 = Button(okno, text="2",command=Cyfra2)
cyfra2.grid(row=3,column=1)

cyfra3 = Button(okno, text="3",command=Cyfra3)
cyfra3.grid(row=3,column=2)

cyfra0 = Button(okno, text="0",command=Cyfra0)
cyfra0.grid(row=4,column=0)

plus = Button(okno, text="+",command=Plus)
plus.grid(row=4,column=1)
równasię = Button(okno, text="=",command=RównaSię)
równasię.grid(row=4,column=2)
kasuj = Button(okno, text="C",command=Kasuj)
kasuj.grid(row=5,column=1)
okno.mainloop()
