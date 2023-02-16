import tkinter as tk
from tkinter import *

ventana=Tk()

ventana.title("INCREMENTO DE INVERSION")
ventana.geometry('300x240')
ventana.resizable(0,0)
ventana.config(bg="#A3ECA0")

def simulacion():

    capital=float(c.get())
    interes=float(i.get())
    periodo=int(m.get())

    acumulativo=capital

    for n in range(periodo):
        calculo=capital*(interes/100)
        capital=capital+calculo
        acumulativo=acumulativo+calculo

    result.set(round(acumulativo,2))

Label(ventana,text="SIMULACION DEL INCREMENTO DE INVERSION",bg="#A3ECA0").place(x=23,y=5)

Label(ventana,text="CAPITAL : ",bg="#A3ECA0").place(x=30,y=35)
c=Entry(ventana, width=25, bd=5)
c.place(x=110,y=35)

Label(ventana,text="INTERES : %",bg="#A3ECA0").place(x=30,y=65)
i=Entry(ventana, width=25, bd=5)
i.place(x=110,y=65)

Label(ventana,text="PERIODO : ",bg="#A3ECA0").place(x=30,y=95)
m=Entry(ventana, width=25, bd=5)
m.place(x=110,y=95)

Button(ventana,text="SIMULAR",command=simulacion,bg="#A0E0EC").place(x=115,y=145)

result=tk.StringVar()
incremento=Entry(ventana, width= 25,bd= 5, justify = 'right', state = tk.DISABLED,textvariable= result).place(x=70,y=190)


ventana.mainloop()