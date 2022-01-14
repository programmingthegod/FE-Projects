import tkinter
from time import strftime


def tym():
    t = strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(1000, tym)
    # temp= f"Current time is: {t}"
    # print(temp)
    # print(t)
    pass


clock = tkinter.Tk()

lbl = tkinter.Label(clock, background="yellow", foreground="red", font=("Georgia", 47, "bold"))
lbl_2 = tkinter.Label(clock, text="Time is:", background="purple", foreground="turquoise", font=("sans-serif ", 45))
lbl_2.pack()
tym()
# Create a Button
btn = tkinter.Button(clock, text='SET ALARM', bd='20', command=clock.bell, background="pink", foreground="blue", font=("Times New roman", 21, "bold"))

# Set the position of button on the top of window.  
btn.pack(side='top')

clock.mainloop()
