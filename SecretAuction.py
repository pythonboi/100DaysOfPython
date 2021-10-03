# import replit

from art import logo2
from replit import clear

print(logo2)

print("Welcome to the Secret Auction program")

auction = {}

print(type(auction))

collect = ''

name = input("What is your name?: ").title()
bid = int(input("What is your bid?: $"))

while True:

    question = input("Are there any other bidders? Type 'yes' or 'no.' ").lower()

    auction[name] = name
    auction[name] = bid

    if question == "yes":
        clear()
        # replit.clear()
    elif question == "no":
        print("GoodBye")
        exit()

print(type(auction))

# auction.update(name=bid)

print(auction)
print(collect)

# print(f"The winner is {name} with a bid of {bid}.")
