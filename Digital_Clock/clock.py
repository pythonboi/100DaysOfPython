from tkinter import *
from tkinter import ttk
import tkinter as tk
from time import sleep

from datetime import datetime

root = Tk()

root.title("Digital Time")
root.geometry("400x250")

root.resizable(False, False)

root.config(background="grey")

# Creating the time display

searchClock = PhotoImage(file="digitalClock.png")
myClock = Label(image=searchClock, bg="black", fg="red")
myClock.place(x=50, y=20)


# mytText = tk.Entry(root, justify="center", width=6, font=("poppins", 50, "bold"), bg="black", border=0, fg="red")
# mytText.place(x=85, y=70)
# mytText.focus()


def timer():
    while True:

        getTime = datetime.now()
        sleep(1)
        myTextClock = getTime.strftime("%H:%M:%S")
        # myText = Label(root, justify="center", width=6, font=("poppins", 45, "bold"), bg="black", border=0,
        #                fg="red")
        # myText.place(x=85, y=75)

        # return myText

        # print(getTime.strftime("%H:%M:%S"))

        myText = Label(root, justify="center", width=6, font=("poppins", 45, "bold"), bg="black", border=0,
                       fg="red")
        myText.place(x=85, y=75)
        myText.config(text=myTextClock)


timer()

# myClock = Label(root)
# canvas = Canvas(root, width=400, height=250)
# canvas.pack()
#
# tm = canvas.create_rectangle(200, 200, 150, 150, bd)

root.mainloop()
