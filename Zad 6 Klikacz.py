
from tkinter import *
import random
# class Przycisk:
#     def __init__(self, gridcol, gridrow):
#         self.row = gridrow
#         self.col = gridcol
#         Button(okno, height=30, width=100, text="help")
#         Button.grid(self.row=self.row, self.column=self.col)


okno = Tk()
okno.title("Klikacz")

liczby = [None] * 25

for x in range(0, 25):
    liczby[x] = random.randint(0, 999)

print(liczby)

przycisk00=Button(okno, text=liczby[0], width=5)
przycisk00.grid(row=0, column=0)
przycisk01=Button(okno, text=liczby[1], width=5)
przycisk01.grid(row=0, column=1)
przycisk02=Button(okno, text=liczby[2], width=5)
przycisk02.grid(row=0, column=2)
przycisk03=Button(okno, text=liczby[3], width=5)
przycisk03.grid(row=0, column=3)
przycisk04=Button(okno, text=liczby[4], width=5)
przycisk04.grid(row=0, column=4)
przycisk10=Button(okno, text=liczby[5], width=5)
przycisk10.grid(row=1, column=0)
przycisk11=Button(okno, text=liczby[6], width=5)
przycisk11.grid(row=1, column=1)
przycisk12=Button(okno, text=liczby[7], width=5)
przycisk12.grid(row=1, column=2)
przycisk13=Button(okno, text=liczby[8], width=5)
przycisk13.grid(row=1, column=3)
przycisk14=Button(okno, text=liczby[9], width=5)
przycisk14.grid(row=1, column=4)
przycisk20=Button(okno, text=liczby[10], width=5)
przycisk20.grid(row=2, column=0)
przycisk21=Button(okno, text=liczby[11], width=5)
przycisk21.grid(row=2, column=1)
przycisk22=Button(okno, text=liczby[12], width=5)
przycisk22.grid(row=2, column=2)
przycisk23=Button(okno, text=liczby[13], width=5)
przycisk23.grid(row=2, column=3)
przycisk24=Button(okno, text=liczby[14], width=5)
przycisk24.grid(row=2, column=4)
przycisk30=Button(okno, text=liczby[15], width=5)
przycisk30.grid(row=3, column=0)
przycisk31=Button(okno, text=liczby[16], width=5)
przycisk31.grid(row=3, column=1)
przycisk32=Button(okno, text=liczby[17], width=5)
przycisk32.grid(row=3, column=2)
przycisk33=Button(okno, text=liczby[18], width=5)
przycisk33.grid(row=3, column=3)
przycisk34=Button(okno, text=liczby[19], width=5)
przycisk34.grid(row=3, column=4)
przycisk40=Button(okno, text=liczby[20], width=5)
przycisk40.grid(row=4, column=0)
przycisk41=Button(okno, text=liczby[21], width=5)
przycisk41.grid(row=4, column=1)
przycisk42=Button(okno, text=liczby[22], width=5)
przycisk42.grid(row=4, column=2)
przycisk43=Button(okno, text=liczby[23], width=5)
przycisk43.grid(row=4, column=3)
przycisk44=Button(okno, text=liczby[24], width=5)
przycisk44.grid(row=4, column=4)




okno.mainloop()