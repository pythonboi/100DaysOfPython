import turtle as t 

import random


tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


direction = [0, 90, 180, 270]


for _ in range(300):

    tim.pensize(5)
    tim.forward(40)
    tim.setheading(random.choice(direction))

    tim.color(random.choice(colours))
    
  

# t.exitonclick()


