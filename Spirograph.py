# Import both the Random and Turtle module 
import random
import turtle as t

# Instantiate the Turtle class 
tp = t.Turtle()

# make the speed of the circle drawing very fast 
tp.speed("fastest")

# Create a window screen size of widht and height 
t.setup(850, 750)

# Assign a radius variable of 100
r = 100


# Create a function to make randoms colors 
def multiColor():
    r = random.random()
    g = random.random()
    b = random.random()

    tp.color(r,g,b)
 

# for loop to 
for _ in range(73):

    tp.pensize(1)
    tp.circle(r * 1)
    tp.left(5)
    multiColor()


# exit the window once the task is completed upon click on the window screen
t.exitonclick()
