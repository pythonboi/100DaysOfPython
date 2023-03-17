from tkinter import *

app = Tk()

passw = "password"


def login():
    getpass = apptxt.get()
    if passw == getpass:
        showLogin.config(text="login successful")
        print("login successful")


app.title("My Password Manager")

app.geometry("500x300")

app.resizable(False, False)

appLabel = Label(app, text="Enter your password", fg="black", font="Monaco")
appLabel.place(x=145, y=110)

apptxt = Entry(app, width=40, show="*")
apptxt.place(x=120, y=150)

appbtn = Button(app, font="Monaco", bg="yellow", activebackground="green", width=10, text="Login", justify="center",
                command=login)
appbtn.place(x=170, y=190)

showLogin = Label(app, font="Georgia 20", fg="green")
showLogin.place(x=130, y=240)

login()

app.mainloop()
