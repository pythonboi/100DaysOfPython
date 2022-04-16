import time
from turtle import Turtle, Screen
import random

myScreen = Screen()

snakePosition = [0, -20, -40]
snake_draw = []
# snake_color = ['white', 'white', 'white']

is_running = True

myScreen.setup(width=600, height=600)
myScreen.bgcolor("black")
myScreen.title("Snake_Game ")

myScreen.tracer(0)


for build in range(0, 3):
    myT = Turtle()
    myT.shape("square")
    myT.color('white')
    myT.penup()
    myT.goto(snakePosition[build], 0)
    snake_draw.append(myT)


# if snakePosition == 3:
#     is_running = True


while is_running:
    myScreen.update()
    time.sleep(1)
    for snake in snake_draw:
        snake.forward(10)

myScreen.exitonclick()
