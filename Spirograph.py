import random
import turtle as t

tp = t.Turtle()

tp.speed("fast")

#t.colormode(255)


def multiColor():
    r = random.random()
    g = random.random()
    b = random.random()

    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)

    tp.color(r,g,b)
 

def drawCircle():

    for _ in range(12):
        tp.circle(100)
        tp.tilt(10)
        tp.left(30)
        multiColor()
    
#     tp.circle(100)
#     tp.tilt(10)
#     tp.fd(20)
#     tp.circle(95)

drawCircle()

t.exitonclick()
