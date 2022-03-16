from audioop import mul
import random
import turtle as t

tp = t.Turtle()

tp.speed("fast")

r = 100



def multiColor():
    r = random.random()
    g = random.random()
    b = random.random()

    tp.color(r,g,b)
 

# def drawCircle():

#     for _ in range(12):

#         tp.circle(100)
#         tp.tilt(10)
#         tp.left(30)
#         multiColor()

# drawCircle()


for _ in range(38):

    tp.circle(r * 1)
    tp.left(10)
    #tp.tilt(30)
    multiColor()


t.exitonclick()
