import tkinter
from time import strftime
def tym():
    t= strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(1000, tym)
    # temp= f"Current time is: {t}"
    # print(temp)
    # print(t)
    pass
clock = tkinter.Tk()

lbl=tkinter.Label(clock)
lbl = tkinter.Label(clock, background="blue", foreground="yellow", font=("monotype corsiva",50,"bold"))
lbl_2 = tkinter.Label(clock, text="Time is:",background="green", foreground="black", font=("monotype corsiva ",50,"underline"))
lbl_2.pack()
tym()
# Create a Button
btn = tkinter.Button(clock, text = 'SET ALARM', bd = '10',command = clock.bell, background="red",foreground="black", font=("aerial black",25,"bold"))
 
# Set the position of button on the top of window.  
btn.pack(side='top'  ) 



clock.mainloop()
