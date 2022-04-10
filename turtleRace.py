# importing the turtle
from turtle import Turtle, Screen
import random

# Create a screen method
screen = Screen()

# Give a title to the Windows Interface
screen.title("Turtle Race!!!")

# Create a scree size to use for the window
screen.setup(700, 500)

# Create a variable and make it False
is_RaceOn = False

# Ask a question and Enter you input message

player1 = screen.textinput("Player1 Choose", prompt="Which turtle color will win the race?")
player2 = screen.textinput("Player2 Choose", prompt="Which turtle color will win the race?")

# Create a list of rainbow colors
rainbowColors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Create a list for the y position coordinate
y_Position = [-30, -60, -90, 0, 30, 60, 90]

# Create an empty list to hold the turtle position
newTurtle = []

# For loop to create multiple turtle  with different colors
for pick in range(0, 7):
    userNames = Turtle()  # userNames.shape('turtle')
    userNames.shape("turtle")
    userNames.color(rainbowColors[pick])
    userNames.penup()
    userNames.goto(-335, y_Position[pick])
    newTurtle.append(userNames)


# Check if the players place a bet or have an input
if player1 != '' and player2 != '':
    is_RaceOn = True

# Keep running the turtle until is False
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

# Create the onclick exit once the task is completed
screen.exitonclick()
