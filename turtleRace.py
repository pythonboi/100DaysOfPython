import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

# Give a title to the Windows Interface
screen.title("Turtle Race!!!")

# Create a scree size to use for the window
screen.setup(700, 500)

# Ask a question and Enter you input message

# Answer = screen.textinput("Question", prompt="Which turtle color will win the race?")
#
# print(Answer)

rainbowColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']#, 'violet']

userNames = ['jenny', 'pam', 'tom', 'jane', 'jim', 'kim']#, #'sam']

y_Position = [30, 60, 90, 0, -30, -60, -90]

colorTaken = []
nameTaken = []

#
# def changeRange(x, y):
#     global num
#     for num in range(0, 6):
#         num = num + 10
#         turtle.goto(-335, num)

for pick in range(0, 6):

    userNames = Turtle()  # userNames.shape('turtle')
    userNames.shape("turtle")
    #userNames.color(pick)
    userNames.penup()

    userNames.goto(-335, y_Position[pick])
    userNames.color()
    # userNames.goto(changeRange(x, y=num))


# def pickUser():
#     for name in userNames:
#         name.



    # for n in userNames:
    #     if n in userNames:
    #         n.goto(-335, 30)

# pam = Turtle()
# pam.color("orange")
# pam.shape('turtle')
# pam.penup()
# pam.goto(-335, 30)
#
# tom = Turtle()
# tom.color("yellow")
# tom.shape('turtle')
# tom.penup()
# tom.goto(-335, 60)
#
# jane = Turtle()
# jane.color("green")
# jane.shape('turtle')
# jane.penup()
# jane.goto(-335, 90)
#
# jim = Turtle()
# jim.color("blue")
# jim.shape('turtle')
# jim.penup()
# jim.goto(-335, -30)
#
# kim = Turtle()
# kim.color("indigo")
# kim.shape('turtle')
# kim.penup()
# kim.goto(-335, -60)
#
# sam = Turtle()
# sam.color("violet")
# sam.shape('turtle')
# sam.penup()
# sam.goto(-335, -90)
#
#
# class Select:
#     def __init__(self, color, shape, position):
#         self.color = color
#         self.shape = shape
#         self.position = position


screen.exitonclick()
