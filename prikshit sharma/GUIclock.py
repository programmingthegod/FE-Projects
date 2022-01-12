#from tkinter import *
import tkinter
from time import strftime

def tym():
    t=strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(1000,tym)
pass

clock=tkinter.Tk()
clock.title("GUI clock")

lbl=tkinter.Label(clock,background="black",foreground="yellow",font=("Comic Sans MS", 85, "bold"))
lbl_2=tkinter.Label(clock,text="Time is:",background="black",foreground="yellow",font=("Comic Sans MS", 85, "bold"))
lbl_2.pack()
tym()

clock.mainloop()

