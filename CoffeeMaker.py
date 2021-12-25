# TODO Import the menu

from coffeeMenu import MENU, resources
import pyinputplus as pyip

account = 0

# variable for all the money accepting

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

defaultWater = resources.get('water')
defaultMilk = resources['milk']
defaultCoffee = resources['coffee']

print(defaultWater, defaultMilk, defaultCoffee)

measurement = 'ml'
quantity = 'g'
# print(f"{defaultWater}{measurement}")

# TODO create a question

waterRemains = resources['water']
milkRemains = resources['milk']
coffeeRemains = resources['coffee']


def selection(drinkType):
    global account

    global defaultWater
    global defaultMilk
    global defaultCoffee

    # account = drinkCost

    # print(defaultWater, defaultMilk, defaultCoffee)

    for checkDrink in MENU:
        if checkDrink == question:
            info = MENU.get(checkDrink)
            # print(info)
            # print(info['ingredients']['water'])
            drinkCost = info['cost']
            # print(drinkCost)

            if account != 0 and defaultWater < info['ingredients']['water']:
                # print(defaultWater)
                print("Sorry there is not enough water.")
                break
            print("Please insert coins.")
            # if question == drinkType:
            quartersCount = pyip.inputInt(prompt="how many quarters?: ")
            dimesCount = pyip.inputInt("how many dimes?: ")
            nicklesCount = pyip.inputInt("how many nickles?: ")
            penniesCount = pyip.inputInt("how many pennies?: ")

            thePrice = quartersCount * quarters + dimesCount * dimes + nicklesCount * nickles + penniesCount * pennies
            print(thePrice)

            # Paste here

            # global account

            # account = drinkCost

            if thePrice < drinkCost:
                print("Sorry that's not enough money. Money refunded. ")

            elif thePrice > drinkCost and question != 'espresso':

                account = drinkCost

                # if thePrice > drinkCost:

                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = waterRemains - info['ingredients']['water']
                # milkBalance = milkRemains - info['ingredients']['milk']
                milkBalance = milkRemains - info['ingredients'].get('milk')
                print(milkBalance)
                coffeeBalance = coffeeRemains - info['ingredients']['coffee']

                defaultWater = waterBalance
                defaultMilk = milkBalance
                defaultCoffee = coffeeBalance

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")

            elif account != 0 and question == 'espresso':

                account = drinkCost

                print("I am here second")

                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = waterRemains - info['ingredients']['water']
                coffeeBalance = coffeeRemains - info['ingredients']['coffee']

                # Pick it up from here. if code does not work return it back from the next line of

                # print(defaultWater, defaultMilk, defaultCoffee)

                # global defaultWater
                # global defaultMilk
                # global defaultCoffee

                defaultWater = waterBalance
                # defaultMilk = milkBalance
                defaultCoffee = coffeeBalance

                # print(defaultWater, defaultMilk, defaultCoffee)

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")
                # print(defaultWater)

            elif account == 0 or question == 'espresso':

                account = drinkCost

                print('I am here')

                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = waterRemains - info['ingredients']['water']
                coffeeBalance = coffeeRemains - info['ingredients']['coffee']

                # Pick it up from here. if code does not work return it back from the next line of

                # print(defaultWater, defaultMilk, defaultCoffee)

                # global defaultWater
                # global defaultMilk
                # global defaultCoffee

                defaultWater = waterBalance
                # defaultMilk = milkBalance
                defaultCoffee = coffeeBalance

                # print(defaultWater, defaultMilk, defaultCoffee)

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")
                # print(defaultWater)

            # elif account != 0 and defaultWater < info['ingredients']['water']:
            #     print(defaultWater)
            #     print("Sorry there is not enough water.")


def noMilk():
    pass


while True:

    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # if account == 0 or account != 0 and question == 'espresso':
    #     noMilk()

    if question != 'report':
        selection(drinkType=question)

    if account != 0 and question == 'report':
        print(f"Water: {defaultWater}{measurement}")
        print(f"Milk: {defaultMilk}{measurement}")
        print(f"Coffee: {defaultCoffee}{quantity}")
        # account = account +
        print(f"Money: {account}")

    elif account == 0 and question == 'report':
        print(f"Water: {defaultWater}{measurement}")
        print(f"Milk: {defaultMilk}{measurement}")
        print(f"Coffee: {defaultCoffee}{quantity}")
        print(
            f"Money: {account}"
        )
        # print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        # print(f"Money: ${account}")

    elif question == 'off':
        print(f"Powering off the coffee machine... GoodBye!!!")
        exit()

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee


# elif account != 0 and question == 'espresso':
