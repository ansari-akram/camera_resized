from tkinter import *
import tkinter
from functools import partial
from ipcam import *


def show_all(string):
    camera = string.get()
    if string.get() == "0":
        camera = int(string.get())
    main_method(camera)


window = tkinter.Tk()
window.title("Insert Link")
Label(window, text="Paste Your Link:", font=("Times New Roman", 15)).grid()
link = StringVar(window)
txt1 = Entry(window, width=100, textvariable=link).grid()
show = partial(show_all, link)
btn1 = Button(window, text="Submit", command=show).grid()
btn2 = Button(window, text="Cancel", command=window.destroy).grid()
window.mainloop()