# Importing logo and replit
import replit
import os

from art import logo2
from replit import clear

print(logo2)

print("Welcome to the Secret Auction program")

# Create a an empty dictionary for auction
auction = {}

# create a variable for name and bid
name = input("What is your name?: ").title()
bid = int(input("What is your bid?: $"))

# create a key and value from the name and bid entry from the user
auction[name] = name
auction[name] = bid

# create a while loop
while True:

    question = input("Are there any other bidders? Type 'yes' or 'no.' ").lower()
    # check/verify if the user answer yes
    if question == "yes":
        replit.clear()
        # os.system('cls')
        # clear()
        name = input("What is your name?: ").title()
        bid = int(input("What is your bid?: $"))
        auction[name] = name
        auction[name] = bid
    # check if user answer no
    elif question == "no":
        print("GoodBye")
        break
    else:
        print("Answer 'yes' or 'no'")

# create an empty list to gather all the value for the dictionary
getHigh = []

# create an empty integer for validating the highest bid or amount
hNum = int()

# create a for loop to check through the dictionary and get the key and value dictionary
for check, val in auction.items():
    getHigh.append(val)
    for name in getHigh:
        if name > hNum:
            hNum = name
    if val == hNum:
        dKey = check

# Print the result from key and value from the dictionary
print(f"The winner is {dKey} with a bid of {hNum}.")
