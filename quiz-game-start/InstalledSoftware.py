import sched
from turtle import Turtle, Screen

circle = 360
sides = 4

t = Turtle()

count = int(input("how many sides do you want: "))


def draw(shape):
    angle = 360 / sides
    for _ in range(shape):
        t.color("green")
        t.forward(100)
        t.right(angle)


draw(count)
# for _ in range(4):
#     t = Turtle()
#
#     t.color("green")
#     t.forward(100)
#     t.penup()
#     t.forward(100)
#     t.pendown()
#     t.color("green")
#     t.forward(100)

# t.right(circle / sides)
# t.forward(100)

Screen().exitonclick()
