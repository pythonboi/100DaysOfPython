from tkinter import *

app = Tk()

passw = "password"


def login():
    getpass = apptxt.get()
    if passw == getpass:
        showLogin.config(text="login successful")
        print("login successful")

        app.destroy()

        newapp = Tk()

        newapp.geometry("800x550")
        newapp.title("User Entry")

        vLabel = Label(newapp, font="Monaco, 10", text="View Account")
        vLabel.place(x=20, y=20)

        vBtn = Button(newapp, font="Arial, 10", fg="black", text="View Account", bg="orange", width=12, height=2)
        vBtn.place(x=20, y=50)

        cLabel = Label(newapp, font="Monaco, 10", text="Create Account")
        cLabel.place(x=650, y=20)

        cBtn = Button(newapp, font="Arial, 10", fg="black", text="Add Account", bg="green", width=12, height=2)
        cBtn.place(x=650, y=50)

    # else:
    #     showLogin.config(text="wrong password")


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
