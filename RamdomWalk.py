import turtle as t 

import random


tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


direction = [0, 90, 180, 270]

# t.colormode(255)

def colorRange():

    r = random.random()
    g  = random.random()
    b = random.random()


    tim.color(r,g,b)

# colorRange()

for _ in range(300):
  
    
    tim.pensize(5)
    tim.forward(40)
    tim.setheading(random.choice(direction))
    colorRange()

    
    
  

t.exitonclick()


