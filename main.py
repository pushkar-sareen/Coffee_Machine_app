from coffee_maker import *
from menu import *
from money_machine import *


cm = CoffeeMaker()
menu = Menu()
mm = MoneyMachine()


machine_is_on = True

while machine_is_on:
    choice = input(f"what would you like to have ?{menu.get_items()} ")
    if choice == "report":
        cm.report()
        mm.report()
    else:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            mm.process_coins()
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
        else:
            machine_is_on = False