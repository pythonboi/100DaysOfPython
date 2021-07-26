import random

names = input("Please enter all names: ")

nameList = names.split(", ")

print(nameList)

n = len(nameList)

nm = random.randint(0, 6)

print(f"{nameList[nm].title()} is going to buy the meal today!")
