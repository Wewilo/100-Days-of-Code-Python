import data

#Main Program I added some functionality to handle wrong data.
def order():
        choose = ""
        coffee_types = ['espresso','latte','cappuccino']
        while choose != "quit":
            choose = input("What would you like to drink (Espresso/Latte/Cappuccino): ").lower()
            if choose == 'report':
                return report()
            elif choose in coffee_types:
                return check_resource(choose)
            elif choose != 'quit':
                print("Wrong Data! Please try again!")

#to display all current ingredients.
def report():
    for iter1,iter2 in data.resources.items():
        print(iter1,iter2)
    return order()

#it will check your choose input and compare your coffee's ingredients to resource's ingredients and if it is less than resource's ingredients it will run pay function
#otherwise it will give an error message and run order function
def check_resource(choose):
    chosen_coffee = data.MENU[choose]['ingredients']

    if choose == 'espresso':
        if chosen_coffee['water'] <= data.resources['water'] and chosen_coffee['coffee'] <= data.resources['coffee']:
            return pay(choose,chosen_coffee)
        elif  data.resources['water'] < chosen_coffee['water']:
            print("Sorry There is not enough Water!")
            return order()
        elif  data.resources['coffee'] < chosen_coffee['coffee']:
            print("Sorry There is not enough Coffee!")
            return order()
        else:
            print("Something Went Wrong Please Try Again!")
            return order()

    elif choose == 'latte':
        if chosen_coffee['water'] <= data.resources['water'] and chosen_coffee['coffee'] <= data.resources['coffee'] and chosen_coffee['milk'] <= data.resources['milk']:
            return pay(choose,chosen_coffee)
        elif data.resources['water'] < chosen_coffee['water']:
            print("Sorry There is not enough Water!")
            return order()
        elif data.resources['milk'] < chosen_coffee['milk']:
            print("Sorry There is not enough Milk!")
            return order()
        elif  data.resources['coffee'] < chosen_coffee['coffee']:
            print("Sorry There is not enough Coffee!")
            return order()
        else:
            print("Something Went Wrong Please Try Again!")
            return order()

    elif choose == 'cappuccino':
        if chosen_coffee['water'] <= data.resources['water'] and chosen_coffee['coffee'] <= data.resources['coffee'] and chosen_coffee['milk'] <= data.resources['milk']:
            return pay(choose,chosen_coffee)
        elif data.resources['water'] < chosen_coffee['water']:
            print("Sorry There is not enough Water!")
            return order()
        elif data.resources['milk'] < chosen_coffee['milk'] :
            print("Sorry There is not enough Milk!")
            return order()
        elif data.resources['coffee'] < chosen_coffee['coffee']:
            print("Sorry There is not enough Coffee!")
            return order()
        else:
            print("Something Went Wrong Please Try Again!")
            return order()
        
        
#It asks to insert money,if it will enough money to buy coffee it will add coffee cost to your account and run decrease_ingredients function.It will decrease ingredients
#from your resource
def pay(choose,chosen_coffee):
    print("Plese Intert Coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    cost = data.MENU[choose]['cost']
    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    change = total - cost

    if total > cost:
        data.resources['money'] += cost
        decrease_ingredients(choose,chosen_coffee)
        print(f'Here is {change:.2f} in change')
        print(f'Here is your {choose} Enjoy!')
        return order()
    elif total < cost:
        print(f"Sorry that's not enough money!\nInserted Money = {total:.2f}\n{choose} price = {cost:.2f}\nMoney refunded")
        return order()
    elif total == cost:
        data.resources['money'] += cost
        print(f'Here is your {choose} Enjoy!')
        return order()


#If the customer inserted enough money it will decrease resources.
def decrease_ingredients(choose,chosen_coffee):
    if choose == 'espresso':
        data.resources['water'] -= chosen_coffee['water']
        data.resources['coffee'] -= chosen_coffee['coffee']
    elif choose == 'latte':
        data.resources['water'] -= chosen_coffee['water']
        data.resources['coffee'] -= chosen_coffee['coffee']
        data.resources['milk'] -= chosen_coffee['milk']
    elif choose == 'cappuccino':
        data.resources['water'] -= chosen_coffee['water']
        data.resources['coffee'] -= chosen_coffee['coffee']
        data.resources['milk'] -= chosen_coffee['milk']

order()