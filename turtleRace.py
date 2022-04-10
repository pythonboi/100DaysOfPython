# importing the turtle
from turtle import Turtle, Screen
import random

screen = Screen()

# Give a title to the Windows Interface
screen.title("Turtle Race!!!")

# Create a scree size to use for the window
screen.setup(700, 500)

is_RaceOn = False

# Ask a question and Enter you input message

player1 = screen.textinput("Player1 Choose", prompt="Which turtle color will win the race?")
player2 = screen.textinput("Player2 Choose", prompt="Which turtle color will win the race?")

# print(Answer)

rainbowColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# userNames = ['jenny', 'pam', 'tom', 'jane', 'jim', 'kim']#, #'sam']

y_Position = [-30, -60, -90, 0, 30, 60, 90]

newTurtle = []

#
# def changeRange(x, y):
#     global num
#     for num in range(0, 6):
#         num = num + 10
#         turtle.goto(-335, num)


for pick in range(0, 7):
    userNames = Turtle()  # userNames.shape('turtle')
    userNames.shape("turtle")
    userNames.color(rainbowColors[pick])
    userNames.penup()
    userNames.goto(-335, y_Position[pick])
    newTurtle.append(userNames)

# print(newTurtle)

if player1 != '' and player2 != '':
    is_RaceOn = True

while is_RaceOn:

    for turtle in newTurtle:
        if turtle.xcor() > 320:
            winnerTurtle = turtle.pencolor()

            print(winnerTurtle)
            is_RaceOn = False
            if player1 == winnerTurtle:
                print(f"Player1 Won, the {winnerTurtle} turtle won the race")

            elif player2 == winnerTurtle:
                print(f"Player2 Won, the {winnerTurtle} turtle won the race")
            else:
                print(f"You both loose, the {winnerTurtle} turtle won the race")
        # print(turtle)
        count = random.randint(0, 10)
        turtle.forward(count)



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
