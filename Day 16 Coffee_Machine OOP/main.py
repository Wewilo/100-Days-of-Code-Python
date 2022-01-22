from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
make_coffee = CoffeeMaker()
machine = MoneyMachine()

while True:
    drinks = ['espresso','latte','cappuccino']
    choose = input(f'What would you like to drink {menu.get_items()}')

    if  choose == 'report':
        make_coffee.report()
        machine.report()
    elif choose == 'turn off':
        break
    elif choose in drinks:
        order = menu.find_drink(choose)
        if make_coffee.is_resource_sufficient(order) == True:
            if machine.make_payment(order.cost) == True:
                make_coffee.make_coffee(order)
        
    else:
        print("Invalid Data Please Try Again!")

