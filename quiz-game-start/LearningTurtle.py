# from turtle import Turtle, Screen
# import random
#
# myTurtle = Turtle()
#
# # myTurtle.forward(100)
# # myTurtle.right(90)
# # myTurtle.forward(100)
# # myTurtle.right(90)
# # myTurtle.forward(100)
# # myTurtle.right(90)
# # myTurtle.forward(100)
#
# # for _ in range(15):
# #     myTurtle.forward(10)
# #     myTurtle.penup()
# #     myTurtle.forward(10)
# #     myTurtle.pendown()
#
# increment = 3
#
# full = 3
#
# #
# # for check in range(3):
# #     myTurtle.color("orange")
# #     myTurtle.forward(100)
# #     myTurtle.right(120)
# #     #increment += 1
# #     print(increment)
# #
# # for _ in range(4):
# #     myTurtle.color("peru")
# #     myTurtle.forward(100)
# #     myTurtle.right(90)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(5):
# #     myTurtle.color("pink")
# #     myTurtle.forward(100)
# #     myTurtle.right(72)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(6):
# #     myTurtle.color("green")
# #     myTurtle.forward(100)
# #     myTurtle.right(60)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(7):
# #     myTurtle.color("purple")
# #     myTurtle.forward(100)
# #     myTurtle.right(51.4)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(8):
# #     myTurtle.color("brown")
# #     myTurtle.forward(100)
# #     myTurtle.right(45)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(9):
# #     myTurtle.color("blue")
# #     myTurtle.forward(100)
# #     myTurtle.right(40)
# #     #increment += 1
# #     print(increment)
# #
# # for new in range(10):
# #     myTurtle.color("red")
# #     myTurtle.forward(100)
# #     myTurtle.right(36)
# #     #increment += 1
# #     print(increment)
#
# # while full < 10:
# #
# #     for _ in range(increment):
# #         myTurtle.color("navy")
# #         myTurtle.forward(100)
# #         myTurtle.right(120)
# #         print(full)
# #         full += 1
# #
# #         myTurtle.color("pink")
# #         myTurtle.forward(100)
# #         myTurtle.right(90)
# #
#
# colors = ["dark olive green", "teal", "blue", "light slate gray", "dark magenta", "deep pink", "dark salmon", "navajo white"]
#
#
# def number(numb_sides):
#     angle = 360 / numb_sides
#     for _ in range(numb_sides):
#         #myTurtle.color("magenta")
#         myTurtle.forward(100)
#         myTurtle.right(angle)
#
#
# for draw_shape in range(3, 11):
#     # myTurtle.color("Orange")
#     myTurtle.color(random.choice(colors))
#     number(draw_shape)
#
#
#
#
#
# # number(count=count)
# # count += 1
#
# # myTurtle.color("red")
# # myTurtle.forward(forward)
# # myTurtle.right(fullCircle / 4)
#
# # print(_)
#
# Screen().exitonclick()

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_total_price(self):
        return self.price * self.quantity


item1 = Item("phone", 100, 1)

item2 = Item("laptop", 1000, 3)

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)

print(item1.calc_total_price())
print(item2.calc_total_price())

