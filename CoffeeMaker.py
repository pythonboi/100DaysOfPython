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

defaultWater = resources.get('water')
defaultMilk = resources['milk']
defaultCoffee = resources['coffee']

measurement = 'ml'
quantity = 'g'
# print(f"{defaultWater}{measurement}")

# TODO create a question

# def getReport(theWater, theMilk, theCoffee):
#     waterRemains = resources['water']
#     milkRemains = resources['milk']
#     coffeeRemains = resources['coffee']
#     return waterRemains, milkRemains, coffeeRemains
#
#
# # getReport(theWater=resources['water'], theMilk=resources['milk'], theCoffee=resources['coffee'])
#
# print(getReport(theWater=resources['water'], theMilk=resources['milk'], theCoffee=resources['coffee']))

waterRemains = resources['water']
milkRemains = resources['milk']
coffeeRemains = resources['coffee']


def selection(drinkType):
    print("Please insert coins.")

    for checkDrink in MENU:
        if checkDrink == question:
            info = MENU.get(checkDrink)
            # print(info['ingredients']['water'])
            drinkCost = info['cost']
            print(drinkCost)

            # if question == drinkType:
            quartersCount = pyip.inputInt(prompt="how many quarters?: ")
            dimesCount = pyip.inputInt("how many dimes?: ")
            nicklesCount = pyip.inputInt("how many nickles?: ")
            penniesCount = pyip.inputInt("how many pennies?: ")

            thePrice = quartersCount * quarters + dimesCount * dimes + nicklesCount * nickles + penniesCount * pennies
            print(thePrice)

            global account

            account = drinkCost

            if thePrice > drinkCost:
                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = waterRemains - info['ingredients']['water']
                milkBalance = milkRemains - info['ingredients']['milk']
                coffeeBalance = coffeeRemains - info['ingredients']['coffee']

                global defaultWater
                global defaultMilk
                global defaultCoffee

                defaultWater = waterBalance
                defaultMilk = milkBalance
                defaultCoffee = coffeeBalance

                # print(f"{waterBalance} {milkBalance} {coffeeBalance}")
                print(defaultWater)

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded. ")

    # getReport(getReport(theWater=resources['water'], theMilk=resources['milk'], theCoffee=resources['coffee']))


# print(f"{waterRemains} {milkRemains} {coffeeRemains}")


while True:

    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if account != 0 and question == 'report':
        print(f"Water: {defaultWater}{measurement}")
        print(f"Milk: {defaultMilk}{measurement}")
        print(f"Coffee: {defaultCoffee}{quantity}")
        print(f"Money: {account}")

    elif question == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${account}")

    elif question == 'off':
        print(f"Powering off the coffee machine... GoodBye!!!")
        exit()

    if question != 'report':
        selection(drinkType=question)

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee
