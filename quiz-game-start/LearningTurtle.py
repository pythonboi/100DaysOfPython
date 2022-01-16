from turtle import Turtle, Screen

myTurtle = Turtle()

# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)

for _ in range(15):
    myTurtle.forward(10)
    myTurtle.penup()
    myTurtle.forward(10)
    myTurtle.pendown()


Screen().exitonclick()
