# Import both the Turtle and Random Module 
import random, turtle

# create an object and instanciate the Turtle Class 
t = turtle.Turtle()

# Use the shape method for the t object to switch to any shape to draw
#t.shape("arrow")

# Define/ Create a variable for diagram
fullshape = 360


# Use the penup object to not draw on the screen 
t.penup()

# Assign a color to you drawing and shape
t.color("green")


# Create a function for the Drawing  
def penDown():
    
    t.pensize(3)
    t.pendown()
    t.forward(100)
    t.left(fullshape/4)
    
# Create a function to not draw 
def penUp():

    t.penup()
    t.forward(100)
    t.left(fullshape/4)


# Here is the begining of the function Line 
# set or position you drawing starting point. 
t.goto(-150, 0.00)
# Use the begin fill method to color the shape once the shape is completed
t.begin_fill()
# Create a for loop to draw the square shape
for _ in range(0, 4):
    penDown()
   
# End the color inside the square shape 
t.end_fill()
# print(t.position())

# Here is the blank/white flag
#placing the position for the white shape 
t.goto(-50.0, 0.00)
for noline in range(4):
    
    penUp()

# print the position of the box after drawing the shape
print(t.position())

# Place the position for third box/shape 
t.goto(40, 0.00)
t.begin_fill()
# This is the function for the third side of the flag
for thr in range(4):

    penDown()

t.end_fill()
t.goto(140, 0.00)
print(t.position())
    
# exits the Turtle display once the task is completed upon clicking the window
turtle.exitonclick()
