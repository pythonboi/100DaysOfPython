import turtle as t 

import random


tim = t.Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


direction = [0, 90, 180, 270]

# def selectColor():
#     for cl in colours:
#         # getColor = cl
#         myColor = random.choice(colours)
#     print(myColor)

# selectColor()

for _ in range(300):

    tim.pensize(5)
    tim.forward(40)
    tim.setheading(random.choice(direction))

    tim.color(random.choice(colours))
    

    
    


# t.exitonclick()


