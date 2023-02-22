from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime

import requests
import pytz

root = Tk()
root.title("Weather App")

root.geometry("900x600")
root.resizable(False, False)


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(type(result))
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)

        current_time = local_time.strftime("%I:%M %p")

        cityName.config(text=city.upper())
        name.config(text="CURRENT WEATHER")
        clock.config(text=current_time)

        # API from Weather

        apiKey = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=d6e234f967558c4bb00121c136f07250"

        json_data = requests.get(apiKey).json()
        print(json_data)
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        #
        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!!")


# Creating the search box

search_image = PhotoImage(file="search2.png", )
myImage = Label(image=search_image)
myImage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=25, font=("poppins", 10, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=55, y=45)
textfield.focus()

search_icon = PhotoImage(file="icons8-search-30.png")
myImage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", command=getWeather)
myImage_icon.place(x=250, y=40)

# logo

logo_image = PhotoImage(file="cloudLogo.png")
myLogo = Label(image=logo_image)
myLogo.place(x=10, y=100)

# Bottom box
frameImage = PhotoImage(file="box.png")
myFrameBox = Label(image=frameImage)
myFrameBox.pack(padx=5, pady=5, side=BOTTOM)

# Showing the name of the city and time

name = Label(root, font=("arial", 15, "bold"))
name.place(x=600, y=50)

cityName = Label(root, font=("Times New Roman", 25, "bold"))
cityName.place(x=600, y=100)

clock = Label(root, font=("Helvetica", 20))
clock.place(x=600, y=150)

# label

label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#00bfff")
label1.place(x=100, y=420)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#00bfff")
label2.place(x=220, y=420)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#00bfff")
label3.place(x=400, y=420)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#00bfff")
label4.place(x=650, y=420)

# for displaying the temperature and condition

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"))  # fg="#1ab5ef")
w.place(x=100, y=500)
h = Label(text="...", font=("arial", 20, 'bold'))
h.place(x=220, y=500)
d = Label(text="...", font=("arial", 20, "bold"))  # fg="#1ab5ef")
d.place(x=400, y=500)
p = Label(text="...", font=("arial", 20, 'bold'))
p.place(x=650, y=500)

root.mainloop()
