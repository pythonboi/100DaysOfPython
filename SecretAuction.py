import replit
import os

from art import logo2
from replit import clear

print(logo2)

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

getHigh = ''

for check, val in auction.items():
    if val >= val:
        highVal = val
    print(highVal)
# highBid = auction.get(max(auction))

# print(f"The winner is  with a bid of {highBid}.")

# print(type(auction))
