import tkinter
from pygame import mixer
from tkinter import *
from time import strftime

def tym():
    t = strftime("%H:%M:%S:%p")

    lbl.config(text=t)
    lbl.pack()
    lbl.after(1000, tym)

    pass

clock = Tk()
clock.title("GUI clock")
lbl = tkinter.Label(clock,)

tym()
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(1.0)
mixer.music.play()

lbl = Label(clock, font=("open sans", 40, 'bold'),
            background='white',
            foreground='red')


clock.mainloop()

