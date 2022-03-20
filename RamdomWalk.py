import turtle as t 

import random

tim = t.Turtle()

direction = [0, 90, 180, 270]

#t.colormode(255)

def colorRange():

    r = random.random()
    g  = random.random()
    b = random.random()

    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)

    tim.color(r, g, b)

    # tim.color(r,g,b)

for _ in range(200):
    
    tim.pensize(5)
    tim.forward(40)
    tim.setheading(random.choice(direction))
    colorRange()
    

t.exitonclick()
