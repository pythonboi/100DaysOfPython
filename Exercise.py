# a = 5
# b = a += 2
# print(a)

# hard = True
#
# while hard:
#     print("we move")
#     break

#
# live = 6
# num = 0
#
# for count in range(live):
#     if num < live:
#         live -= 1
#         print(live)
#
# # print(live)

def greet(city, name, location):
    print("Hello ", end='')
    print("World")
    print(f"I live in {city} and my name is {name}, you can find me in {location} ")


greet(location="canada", name="hafeez", city="Toronto")


# Write your code below this line 👇
def paint_calc(height, width, cover):
    numbOfCans = (height * width) / coverage
    print(round(numbOfCans))


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
