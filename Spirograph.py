import random
import turtle as t

tp = t.Turtle()

tp.speed("fastest")
t.setup(850, 750)

r = 100



def multiColor():
    r = random.random()
    g = random.random()
    b = random.random()

    tp.color(r,g,b)
 

# def drawCircle():

#     for _ in range(12):

#         tp.circle(100)
#         #tp.tilt(10)
#         tp.left(10)
#         multiColor()

# drawCircle()


for _ in range(70):

    tp.circle(r * 1)
    #tp.tilt(40)
    tp.left(6)
    multiColor()


t.exitonclick()
