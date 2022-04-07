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

rainbowColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

userNames = ['jenny', 'pam', 'tom', 'jane', 'jim', 'kim', 'sam']

colorTaken = []
nameTaken = []


# for num in range(len(rainbowColors)):
#     if num < len(rainbowColors):
#         if color not in


for pick in userNames:
    if pick not in colorTaken:
        colorTaken.append(pick)
        #getName =
print(colorTaken)

    # for check in userNames:
    #     if n not in check:
    #         getName = Turtle()
    #         getName.shape('turtle')


# Jenny = Turtle()
# Jenny.shape("turtle")
# Jenny.color("red")
# Jenny.penup()
# Jenny.goto(-335, 0)

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
