# TODO Import the menu

from coffeeMenu import MENU, resources

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

question = input("What would you like? (espresso/latte/cappuccino): ").lower()

if question == 'report':
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    print(f"Money: ${account}")

elif question == 'off':
    print(f"Powering off the coffee machine... GoodBye!!!")
    exit()

question = input("What would you like? (espresso/latte/cappuccino): ").lower()


menu = MENU


def select(menu):
    print("Please insert coins.")


    money = input("Please insert coins.")
    return menu


select(menu)

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee


# print(MENU)
