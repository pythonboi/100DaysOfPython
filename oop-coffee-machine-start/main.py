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

    # newMoneyRecieved = getMoneyMachine.money_received

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

            print(getMoneyMachine.money_received)
            # newMoneyRecieved += getMoneyMachine.money_received
            # print(newMoneyRecieved)
            print(getMoneyMachine.profit)

    # print("Printing outside")
    # newMoneyRecieved = getMoneyMachine.process_coins()
    # print(newMoneyRecieved)

    # myGet = getMenuItem

    if getOrder == 'report':
        getCoffeeMaker.report()
        getMoneyMachine.report()

    # elif getOrder != getMenu.find_drink(getOrder):
    #     getMenu.find_drink(getOrder)

    elif getCoffeeMaker.resources['water'] < myWater:

        getCoffeeMaker.is_resource_sufficient(getMenuItem)

    # elif getMoneyMachine.profit == 0 or getMoneyMachine.profit != 0:
    #     # newMoneyRecieved = 0
    #     # newMoneyRecieved += getMoneyMachine.money_received
    # #
    #     print("I am checking on without enough funds")
    #     getMoneyMachine.make_payment(myMoney)

    # elif getOrder == getOrder and getMoneyMachine.money_received == 0:
    #
    #     newMoneyRecieved = getMoneyMachine.process_coins()

    # print(newMoneyRecieved)

    # elif getOrder == getMenuItem.name and getMoneyMachine.profit <= getMoneyMachine.money_received:
    #     print("I am here")
    #     # else:
    #
    #     getMoneyMachine.make_payment(myMoney)
    #     # getCoffeeMaker.make_coffee(getMenuItem)

    # elif getOrder == getMenuItem.name and getMoneyMachine.profit >= getMenuItem.cost:
    #
    #     print('check me')
    #     print(getMenuItem.cost)
    #     print(getMoneyMachine.money_received, getMoneyMachine.profit)
    #     # getMoneyMachine.process_coins()
    #
    #     # getMoneyMachine.money_received(myMoney)
    #     getMoneyMachine.make_payment(myMoney)
    #     getCoffeeMaker.make_coffee(getMenuItem)

    # elif getMoneyMachine.make_payment(getMoneyMachine.money_received) <= getMoneyMachine.(getMenuItem.cost) and getMenuItem.cost:
    elif getMoneyMachine.make_payment(getMenuItem.cost): #<= getMenuItem.cost:

        # getOrder == getMenuItem.name
        # getMoneyMachine.profit <= getMenuItem.cost:
        # print("profit lower")
        # print(getMoneyMachine.profit)
        # getMoneyMachine.make_payment(myMoney)
        # print(getMoneyMachine.process_coins())
        #getMoneyMachine.make_payment(getMenuItem.cost)
        # print(getMoneyMachine.money_received)

        # if  > getMenuItem.cost:
        getCoffeeMaker.make_coffee(getMenuItem)

        # if getMoneyMachine.process_coins() < getMenuItem.cost:
        #     getMoneyMachine.make_payment(getMenuItem.cost)
        # myNewmoney = getMoneyMachine.process_coins()

        # if getMoneyMachine.process_coins(): #getMoneyMachine.make_payment(myMoney):
        #     #getMoneyMachine.make_payment(myMoney)
        #     print("I am reading this")
        #     getCoffeeMaker.make_coffee(getMenuItem)

    # else:
    #     print("check here")
