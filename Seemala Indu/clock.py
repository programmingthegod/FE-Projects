import tkinter
from time import strftime
def tym():
    t = strftime("%H:%M:%S %p")
    lbl.config(text =t)
    lbl.pack()
    lbl.after(1000,tym)
    pass
clock = tkinter.Tk()
lbl = tkinter.Label(clock)
lbl = tkinter.Label(clock,bg = "yellow", fg = "blue", font=("Comic Sans MS", 74,"bold", "italic"))
lbl_2 = tkinter.Label(clock, text = "Time is: ", fg="black", font=("Comic Sans MS", 74,"bold","italic") )
lbl_2.pack()
btn = tkinter.Button(clock, text = 'Set alarm', bd ='15', command = clock.bell,bg = "Red", fg = "White",font=("Comic Sans MS",33,"bold","italic" ))
btn.pack(side = 'right')
tym()
clock.mainloop()