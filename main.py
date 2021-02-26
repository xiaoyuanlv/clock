from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Your time is now")


def time():
    str_time = strftime('%I:%M:%S %p')
    label.config(text=str_time)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="yellow")
label.pack(anchor='center')
time()

mainloop()
