import random, turtle

t = turtle.Turtle()

#
# t.circle(50)

# t.shape("square")

# t.shapesize(7, 5)
# t.color('green')

fullshape = 360

def penUp(x):
    
    t.pensize(3)
    t.forward(100)
    t.left(fullshape/4)
    t.forward(100)
    t.fillcolor("green")
    t.begin_fill()

for _ in range(0, 4):
    penUp(t.color("green"))

t.end_fill()
    # penUp()

    
    



turtle.exitonclick()
