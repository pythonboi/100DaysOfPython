import random, turtle

t = turtle.Turtle()

#
# t.circle(50)

# t.shape("square")

# t.shapesize(7, 5)
# t.color('green')

fullshape = 360

t.penup()
t.goto(-175, 100)

t.color("green")
t.begin_fill()

print(t.position())

def penDown():
    
    #t.pendown()
    
    t.pensize(3)
    t.forward(100)
    t.left(fullshape/4)
    
    #t.forward(100)
    

def penUp():

    t.penup()
    t.forward(100)
    t.left(fullshape/4)
    # t.forward(100)


for _ in range(0, 4):
    penDown()
    #print(penDown(t.position))
    # for m in range(4):
    
    #     penUp()

t.end_fill()
print(t.position())

t.goto(100.0, 0)
for m in range(4):
    
    penUp()

print(t.position())
t.goto(200, -0.00)
t.begin_fill()
for thr in range(4):

    t.pendown()
    #t.forward(10)
    penDown()

t.end_fill()
t.goto(300, 0.00)
print(t.position())
    

turtle.exitonclick()
