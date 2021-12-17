# TODO Import the menu

from coffeeMenu import MENU, resources


account = 0

# TODO create a question

question = input("What would you like? (espresso/latte/cappuccino): ").lower()

if question == 'report':
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    print(f"Money: ${account}")

elif question == 'off':
    print(f"Powering off the coffee machine... GoodBye!!!")
    exit()



menu = MENU


def select(menu):
    money = input("Please insert coins.")
    return menu


select(menu)

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee


# print(MENU)
