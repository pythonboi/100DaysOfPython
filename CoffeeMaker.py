# TODO Import the menu

from coffeeMenu import MENU, resources
import pyinputplus as pyip

account = 0

# variable for all the money accepting

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

# Price of drink

espresso = float(1.50)
latte = float(2.50)
cappuccino = float(3.00)


# TODO create a question

def selection(drinkType):
    print("Please insert coins.")

    if question == drinkType:
        quartersCount = pyip.inputInt(prompt="how many quarters?: ")
        dimesCount = pyip.inputInt("how many dimes?: ")
        nicklesCount = pyip.inputInt("how many nickles?: ")
        penniesCount = pyip.inputInt("how many pennies?: ")

        thePrice = quartersCount * quarters + dimesCount * dimes + nicklesCount * nickles + penniesCount * pennies
        print(thePrice)

        if thePrice > espresso:

            print(f"Here is {}")


while True:

    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if question == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${account}")

    elif question == 'off':
        print(f"Powering off the coffee machine... GoodBye!!!")
        exit()

    if question != 'report':
        selection(drinkType=question)

    # if question == 'espresso':
    #     print("Please insert coins.")

menu = MENU

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee


# print(MENU)
