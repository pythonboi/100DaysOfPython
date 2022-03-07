import random, turtle

t = turtle.Turtle()

#
# t.circle(50)

# t.shape("square")

# t.shapesize(7, 5)
# t.color('green')

fullshape = 360

# t.goto(-175, 100)
#t.penup()

# t.fillcolor("green")
t.begin_fill()

def penDown(x):
    
    t.pendown
    t.pensize(3)
    # t.forward(100)
    t.left(fullshape/4)
    t.forward(100)
    

def penUp():

    t.penup()
    t.forward(100)
    t.left(fullshape/4)
    # t.forward(100)


for _ in range(0, 4):
    penDown(t.color("green"))
    #print(penDown(t.position))
    # for m in range(4):
    
    #     penUp()

t.end_fill()
print(t.position())

#t.goto(-10.0, 0)
for m in range(4):
    
    penUp()

print(t.position())
t.goto(90, 0.00)
for thr in range(4):

    t.pendown()
    t.forward(20)
    
    

turtle.exitonclick()
