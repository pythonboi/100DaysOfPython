from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime

import requests
import pytz


root = Tk()
root.title("Weather App")

root.geometry("900x500")
root.resizable(False, False)


# Creating the search box

search_image = PhotoImage(file="search2.png")
myImage = Label(image=search_image)
myImage.place(x=20, y=20)



root.mainloop()
