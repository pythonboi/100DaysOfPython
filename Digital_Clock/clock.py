from tkinter import *
# from tkinter import ttk
# import tkinter as tk
from time import sleep

from datetime import datetime

root = Tk()

# myText = Label(root)

root.title("Digital Time")
root.geometry("400x250")

root.resizable(False, False)

root.config(background="grey")

# Creating the time display

searchClock = PhotoImage(file="digitalClock.png")
myClock = Label(image=searchClock, bg="black", fg="red")
myClock.place(x=50, y=20)


def timer():
    # while True:
    getTime = datetime.now()
    #sleep(1)
    myTextClock = getTime.strftime("%H:%M:%S")

    myText = Label(root, justify="center", width=6, font=("poppins", 45, "bold"), bg="black", border=0,
                   fg="red")
    myText.place(x=85, y=75)
    # root.update(1000, timer)
    root.after(1000, timer)
    return myText.config(text=myTextClock)


timer()

# root.after(1000, timer)
root.mainloop()
