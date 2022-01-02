from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myVariable = {'latte': 0,
              'espresso': 1,
              'cappuccino': 2
              }

getMenu = Menu()

getCoffeeMaker = CoffeeMaker()
getMoneyMachine = MoneyMachine()


while True:

    getOrder = input(f"What would you like {getMenu.get_items()}: ")

    # print(getOrder)

    for item in myVariable:
        if item == getOrder:
            collectVariable = myVariable.get(item)
            # print(collectVariable)

            getMenuItem = MenuItem(name=getMenu.menu[collectVariable].name,
                                   water=getMenu.menu[collectVariable].ingredients['water'],
                                   milk=getMenu.menu[collectVariable].ingredients['milk'],
                                   coffee=getMenu.menu[collectVariable].ingredients['coffee'],
                                   cost=getMenu.menu[collectVariable].cost)

            print(getMenuItem.name)
            myName = getMenuItem.name
            print(getMenuItem.cost)
            myWater = getMenuItem.ingredients.get('water')
            myMilk = getMenuItem.ingredients.get('milk')
            myCoffee = getMenuItem.ingredients['coffee']

            myMoney = getMenuItem.cost
            # print(myMoney)
            # print(myWater, myMilk, myCoffee)
            #
            # print(f"I am here {getCoffeeMaker.resources}")
            # print(f"I am here second {getCoffeeMaker.resources['water']}")

    if getOrder == 'report':
        getCoffeeMaker.report()
        getMoneyMachine.report()

    # elif getOrder != getMenu.find_drink(getOrder):
    #     getMenu.find_drink(getOrder)

    elif getCoffeeMaker.resources['water'] < myWater:
        # print("This is not working")
        getCoffeeMaker.is_resource_sufficient(getMenuItem)

    elif getOrder != '':

        getMoneyMachine.make_payment(myMoney)

        getCoffeeMaker.make_coffee(getMenuItem)




