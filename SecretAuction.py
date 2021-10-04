import replit
import os

from art import logo2
from replit import clear

# print(logo2)

print("Welcome to the Secret Auction program")

auction = {}

name = input("What is your name?: ").title()
bid = int(input("What is your bid?: $"))

auction[name] = name
auction[name] = bid

while True:

    question = input("Are there any other bidders? Type 'yes' or 'no.' ").lower()

    if question == "yes":
        replit.clear()
        # os.system('cls')
        # clear()
        name = input("What is your name?: ").title()
        bid = int(input("What is your bid?: $"))
        auction[name] = name
        auction[name] = bid

    elif question == "no":
        print("GoodBye")
        break
    else:
        print("Answer 'yes' or 'no'")

print(auction)

getHigh = []

hNum = int()

for check, val in auction.items():
    getHigh.append(val)
    for name in getHigh:
        if name > hNum:
            hNum = name
for m, n in auction.items():
    if n == hNum:
        dKey = m
print(getHigh)

print(hNum)

print(f"The winner is {dKey} with a bid of {hNum}.")

# print(type(auction))
