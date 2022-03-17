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
 


for _ in range(73):

    tp.pensize(1)
    tp.circle(r * 1)
    tp.left(5)
    multiColor()


t.exitonclick()
