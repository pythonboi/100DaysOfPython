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

    for item in myVariable:
        if item == getOrder:
            collectVariable = myVariable.get(item)
            print(collectVariable)

            getMenuItem = MenuItem(name=getMenu.menu[collectVariable].name, water=getMenu.menu, milk=getMenu.menu,
                                   coffee=getMenu.menu,
                                   cost=getMenu.menu[collectVariable].cost)

            print(getMenuItem.name)
            print(getMenuItem.cost)

            myMoney = getMenuItem.cost
            # print(myMoney)

    if getOrder == 'report':
        getCoffeeMaker.report()
        getMoneyMachine.report()

    elif getOrder != '':

        getMoneyMachine.make_payment(myMoney)

