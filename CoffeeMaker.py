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

print(defaultWater, defaultMilk, defaultCoffee, account)

measurement = 'ml'
quantity = 'g'

# TODO create a question

waterRemains = resources['water']
milkRemains = resources['milk']
coffeeRemains = resources['coffee']


def selection(drinkType):
    global account

    global defaultWater
    global defaultMilk
    global defaultCoffee

    for checkDrink in MENU:
        if checkDrink == question:
            info = MENU.get(checkDrink)

            drinkCost = info['cost']

            if account != 0 and defaultWater < info['ingredients']['water']:

                print("Sorry there is not enough water.")
                break
            print("Please insert coins.")

            quartersCount = pyip.inputInt(prompt="how many quarters?: ")
            dimesCount = pyip.inputInt("how many dimes?: ")
            nicklesCount = pyip.inputInt("how many nickles?: ")
            penniesCount = pyip.inputInt("how many pennies?: ")

            thePrice = quartersCount * quarters + dimesCount * dimes + nicklesCount * nickles + penniesCount * pennies
            print(thePrice)

            if thePrice < drinkCost:
                print("Sorry that's not enough money. Money refunded. ")

            elif thePrice > drinkCost and question != 'espresso':

                account = drinkCost

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

                account = account + drinkCost

                print("I am here second")

                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = defaultWater - info['ingredients']['water']
                coffeeBalance = defaultCoffee - info['ingredients']['coffee']

                defaultWater = waterBalance

                defaultCoffee = coffeeBalance

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")

            elif account == 0 or question == 'espresso':

                account = drinkCost

                print('I am here')

                drinkChange = thePrice - drinkCost
                drinkDecimal = "{:.3}".format(drinkChange)

                waterBalance = waterRemains - info['ingredients']['water']
                coffeeBalance = coffeeRemains - info['ingredients']['coffee']

                defaultWater = waterBalance

                defaultCoffee = coffeeBalance

                print(f"Here is ${drinkDecimal} in change.")
                print(f"Here is your {question} ☕. Enjoy!")


while True:

    question = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if question != 'report':
        selection(drinkType=question)

    if account != 0 and question == 'report':
        print(f"Water: {defaultWater}{measurement}")
        print(f"Milk: {defaultMilk}{measurement}")
        print(f"Coffee: {defaultCoffee}{quantity}")

        print(f"Money: ${account}")

    elif account == 0 and question == 'report':
        print(f"Water: {defaultWater}{measurement}")
        print(f"Milk: {defaultMilk}{measurement}")
        print(f"Coffee: {defaultCoffee}{quantity}")
        print(
            f"Money: ${account}"
        )

    elif question == 'off':
        print(f"Powering off the coffee machine... GoodBye!!!")
        exit()

# TODO Report

# ToDO Check resources sufficient?

# Todo Process coins

# Todo Check transaction successful?

# Todo Make Coffee

