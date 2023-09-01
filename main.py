# importing tkinter which helps in building UI
from tkinter import *
# importing ttk which helps in assigning good fonts and looks to the clock
from tkinter.ttk import *
# strftime stands for string format time and used to extract time and display in a particular format
from time import strftime
# custom font in tkinter
from tkinter.font import Font

root = Tk()
root.title("Clock")


# Load a custom font
custom_font = ("Courier", 60, "bold")


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=custom_font, background="black", foreground="white")
label.pack(anchor="center")
time()

mainloop()
