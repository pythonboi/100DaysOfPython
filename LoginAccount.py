from tkinter import *

window = Tk()

window.geometry("350x300")

window.title("My Login")

window.resizable(False, False)

login = Label(window, justify="center", text="Login Window", fg="blue", font=("Candara", 20, "bold",))
login.place(x=85, y=20)

name = Label(window, text="Username:", font=("aria", 12, "bold"))
name.place(x=0, y=90)

passwd = Label(window, text="Password:", font=("arial", 12, "bold"))
passwd.place(x=0, y=130)

ntxt = Entry(window, width=40,)
ntxt.place(x=90, y=95)

ptxt = Entry(window, width=40, show='*')
ptxt.place(x=90, y=135)

lbtn = Button(window, text="Login", font=("Gabriola",), bg="green", width=10)
lbtn.place(x=200, y=200)

pbtn = Button(window, text="Cancel", font=("Gabriola",), bg="yellow", width=10)
pbtn.place(x=100, y=200)

window.mainloop()
