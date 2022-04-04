from turtle import Turtle, Screen

tm = Turtle()

screen = Screen()

print(tm.position())


def forward():
    tm.forward(100)


def backward():
    tm.backward(100)


def right():
    tm.right(10)


def left():
    tm.left(10)


def clear():
    tm.clear()
    tm.penup()
    tm.goto(0.00, 0.00)
    tm.setheading(0)
    tm.pd()


screen.listen()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key='a', fun=left)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
