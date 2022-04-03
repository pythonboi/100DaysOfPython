# Import the Cologram module 
# import colorgram

# getImages = colorgram.extract(r"C:\Users\admin\Documents\PyDev\100DaysOfPython\hirst.jpg", 20)

# myDic = []

# #print(type(getImages))
# # print(getImages)


# for m in getImages:
#     # myDic.append(m.rgb)
#     red, green, blue = m.rgb.r, m.rgb.g, m.rgb.b
#     myTuple = (red, green, blue)
#     myDic.append(myTuple)
#     #print(red, green, blue)
# print(myDic)

import random
import turtle as t

myListColor = [(246, 240, 228), (248, 237, 243), (234, 246, 239), (235, 240, 247), (196, 153, 117), (139, 71, 89),
               (145, 81, 69), (61, 97, 127), (225, 215, 109), (136, 165, 184), (187, 145, 159), (34, 20, 15),
               (20, 26, 41), (133, 176, 148), (191, 93, 81), (45, 24, 33), (54, 123, 94), (186, 88, 104), (15, 25, 19),
               (83, 156, 112)]

tp = t.Turtle()
t.Screen()

t.colormode(255)


# print(random.choice(myListColor))


def draw(x, y):
    tp.penup()
    tp.hideturtle()
    tp.goto(-275, -200)
    for count in range(x):
        for counts in range(y):
            tp.dot(20, random.choice(myListColor))
            tp.forward(50)

        # multiplying the space with the number of dot to begin new line
        tp.back(50 * y)
        # Direction of the drawing
        tp.left(90)
        tp.forward(50)
        # tp.back(50 * y)
        tp.right(90)


draw(10, 10)

# hide the turtle drawing pen
# tp.hideturtle()

t.exitonclick()
