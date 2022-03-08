import random, turtle

t = turtle.Turtle()

fullshape = 360


t.penup()

t.color("green")


def penDown():
    
    t.pensize(3)
    t.pendown()
    t.forward(100)
    t.left(fullshape/4)
    #t.forward(100)
    
# Create a function for PenUp funtion 
def penUp():

    t.penup()
    t.forward(100)
    t.left(fullshape/4)


# Here is the begining of the function 

t.goto(-150, 0.00)
t.begin_fill()
for _ in range(0, 4):
    penDown()
   

t.end_fill()
print(t.position())

# Here is the blank/white flag
t.goto(-50.0, 0.00)
for noline in range(4):
    
    penUp()

print(t.position())

# This is the function for the third side of the flag
t.goto(40, 0.00)
t.begin_fill()
for thr in range(4):

    #t.pendown()
    penDown()

t.end_fill()
t.goto(145, 0.00)
print(t.position())
    

turtle.exitonclick()
