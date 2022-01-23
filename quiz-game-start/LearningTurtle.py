from turtle import Turtle, Screen

myTurtle = Turtle()

# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)
# myTurtle.right(90)
# myTurtle.forward(100)

# for _ in range(15):
#     myTurtle.forward(10)
#     myTurtle.penup()
#     myTurtle.forward(10)
#     myTurtle.pendown()

increment = 3

full = 3

#
# for check in range(3):
#     myTurtle.color("orange")
#     myTurtle.forward(100)
#     myTurtle.right(120)
#     #increment += 1
#     print(increment)
#
# for _ in range(4):
#     myTurtle.color("peru")
#     myTurtle.forward(100)
#     myTurtle.right(90)
#     #increment += 1
#     print(increment)
#
# for new in range(5):
#     myTurtle.color("pink")
#     myTurtle.forward(100)
#     myTurtle.right(72)
#     #increment += 1
#     print(increment)
#
# for new in range(6):
#     myTurtle.color("green")
#     myTurtle.forward(100)
#     myTurtle.right(60)
#     #increment += 1
#     print(increment)
#
# for new in range(7):
#     myTurtle.color("purple")
#     myTurtle.forward(100)
#     myTurtle.right(51.4)
#     #increment += 1
#     print(increment)
#
# for new in range(8):
#     myTurtle.color("brown")
#     myTurtle.forward(100)
#     myTurtle.right(45)
#     #increment += 1
#     print(increment)
#
# for new in range(9):
#     myTurtle.color("blue")
#     myTurtle.forward(100)
#     myTurtle.right(40)
#     #increment += 1
#     print(increment)
#
# for new in range(10):
#     myTurtle.color("red")
#     myTurtle.forward(100)
#     myTurtle.right(36)
#     #increment += 1
#     print(increment)

# while full < 10:
#
#     for _ in range(increment):
#         myTurtle.color("navy")
#         myTurtle.forward(100)
#         myTurtle.right(120)
#         print(full)
#         full += 1
#
#         myTurtle.color("pink")
#         myTurtle.forward(100)
#         myTurtle.right(90)
#

fullCircle = 360
forward = 100

numbers = 5

for _ in range(numbers):
    myTurtle.color("magenta")
    myTurtle.forward(forward)
    myTurtle.right(fullCircle/numbers)
    #numbers += 1


# myTurtle.color("red")
# myTurtle.forward(forward)
# myTurtle.right(fullCircle / 4)

    print(_)

Screen().exitonclick()
