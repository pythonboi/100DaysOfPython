import time
from turtle import Turtle, Screen
import random

myScreen = Screen()

snakePosition = [0, -20, -40]
snake_draw = []

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

while is_running:
    myScreen.update()
    time.sleep(0.1)

    for snake_seg in range(len(snake_draw) - 1, 0, -1):
        new_x = snake_draw[snake_seg - 1].xcor()
        new_y = snake_draw[snake_seg - 1].ycor()
        snake_draw[snake_seg].goto(new_x, new_y)

    # for snake in snake_draw:
    snake_draw[0].forward(10)

    snake_draw[0].left(90)

myScreen.exitonclick()
