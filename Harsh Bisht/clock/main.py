import tkinter as tk

from tkinter import *

from time import strftime

def time():

        t = strftime("%H:%M:%S %p")

        l1.config(text=t)

        l1.place(x=160, y=72)

        l1.after(1000, time)

clock = tk.Tk()

clock.title("Clock")

clock.geometry("600x400")

clock.config(bg="black")

l1 = tk.Label(clock, font=("Comic Sans MF", 30, "bold"),

              background="black", foreground="white")

tk.Button(clock, text="Reminder",

          background="white", height=1, font=("Comic Sans MF", 18, "bold")).place(x=330, y=160)

time()

clock.mainloop()
