from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

getMenu = Menu()
# getMenuItem = MenuItem()
getCoffeeMaker = CoffeeMaker()
getMoneyMachine = MoneyMachine()

# getMenu.get_items()

getOrder = input(f"What would you like {getMenu.get_items()}: ")

if getOrder == 'report':
    getCoffeeMaker.report()
    getMoneyMachine.report()

elif getOrder != '':
    getMoneyMachine.process_coins()


