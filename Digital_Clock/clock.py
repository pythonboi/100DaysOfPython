from tkinter import *
from datetime import datetime

root = Tk()

root.title("Digital Time")
root.geometry("400x250")

root.resizable(False, False)

root.config(background="grey")

# Creating the GUI time display

searchClock = PhotoImage(file="digitalClock.png")
myClock = Label(image=searchClock, bg="black", fg="red")
myClock.place(x=50, y=20)


# Create a function for the time
def timer():
    getTime = datetime.now()

    myTextClock = getTime.strftime("%H:%M:%S")

    myText = Label(root, justify="center", width=6, font=("poppins", 45, "bold"), bg="black", border=0,
                   fg="red")
    myText.place(x=85, y=75)

    root.after(1000, timer)
    return myText.config(text=myTextClock)


timer()

root.mainloop()
