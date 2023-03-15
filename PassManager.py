from tkinter import *

app = Tk()

app.title("My Password Manager")

app.geometry("500x300")

app.resizable(False, False)

appLabel = Label(app, text="Enter your password", fg="black", font="Monaco")
appLabel.place(x=145, y=110)

apptxt = Entry(app, width=40, show="*")
apptxt.place(x=120, y=150)

appbtn = Button(app, font="Monaco", bg="green", width=10, text="Login", justify="center")
appbtn.place(x=170, y=190)

app.mainloop()
