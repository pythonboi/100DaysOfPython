from tkinter import *
from tkinter import messagebox
import random

app = Tk()

passw = "password"

dpass = []


def login():
    getpass = apptxt.get()
    if passw == getpass:
        showLogin.config(text="login successful")
        print("login successful")

        app.destroy()

        newapp = Tk()
        frame = Frame(newapp)

        newapp.geometry("800x550")
        newapp.title("User Entry")

        def vcommand():
            txtfield = Text(font="Optima", width=85)
            txtfield.place(x=20, y=100)

        def generatePass():
            passLenght = 12

            alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
            cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
            num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

            for make in alpha:

                if len(dpass) != passLenght:
                    dpass.append(random.choice(make))

                for n in cap:

                    if len(dpass) != passLenght:
                        dpass.append(random.choice(n))

                    for o in num:

                        if len(dpass) != passLenght:
                            dpass.append(random.choice(o))

                        for p in sym:

                            if len(dpass) != passLenght:
                                dpass.append(random.choice(p))

            print(dpass)

        def newAccount():
            userNameLabel = Label(newapp, font="Arial", text="Username:")
            userNameLabel.place(x=20, y=120)

            userNameEntry = Entry(newapp, font="Arial", width=40)
            userNameEntry.place(x=20, y=150)

            gen = Button(newapp, fg="black", font="Arial", text="Generate Password", width=18, height=2, bg="green",
                         command=generatePass)
            gen.place(x=20, y=190)

            passGen = Entry(newapp, font="Arial", width=40, )
            passGen.place(x=20, y=250)

        vLabel = Label(newapp, font="Monaco, 10", text="View Account")
        vLabel.place(x=20, y=20)

        vBtn = Button(newapp, font="Arial, 10", fg="black", text="View Account", bg="orange", width=12, height=2,
                      command=vcommand)
        vBtn.place(x=20, y=50)

        cLabel = Label(newapp, font="Monaco, 10", text="Create Account")
        cLabel.place(x=680, y=20)

        cBtn = Button(newapp, font="Arial, 10", fg="black", text="Add Account", bg="green", width=12, height=2,
                      command=newAccount)
        cBtn.place(x=680, y=50)

    # elif getpass != passw:
    #     messagebox.showinfo("Message", "Wrong Password")


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
