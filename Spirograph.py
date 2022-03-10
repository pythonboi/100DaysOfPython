import random
import turtle as t

t.colormode(255)


def multiColor():
    r = random.random()
    g = random.random()
    b = random.random()

    t.pencolor(r,g,b)

def drawCircle(x):

    
    t.circle(100)
    t.tilt(10)
    t.fd(20)
    t.circle(95)

drawCircle(multiColor)

t.exitonclick()
