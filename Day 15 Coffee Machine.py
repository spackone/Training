MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

while True:
    drink_type = input('What would you like? (espresso/latte/cappuccino): ',)
    
    def resource_check(res = drink_type):
        enough = bool
        water_needed = MENU[res]["ingredients"]["water"]
        water_availible = resources["water"]
        coffee_needed = MENU[res]["ingredients"]["coffee"]
        coffee_availible = resources["coffee"]
        milk_needed = MENU[res]["ingredients"]["milk"]
        milk_availible = resources["milk"]
        if water_needed > water_availible:
            statement = 'Sorry there is not enough water'
            enough = False
            return enough, statement
        elif coffee_needed > coffee_availible:
            statement = 'Sorry there is not enough coffee'
            enough = False
            return enough, statement
        elif milk_needed > milk_availible:
            statement = 'Sorry there is not enough milk'
            enough = False
            return enough, statement
        else: 
            enough = True
            statement = ''
            return enough, statement

    def resource_update(res = drink_type):
        stop = True
        total = 0
        while stop:
            quarters = int(input('How many quarters? '))
            dimes = int(input('How many dimes? '))
            nickels = int(input('How many nickels? '))
            pennies = int(input('How many pennies? '))
            money_due = MENU[res]["cost"]
            total += .25*quarters + .1*dimes + .05*nickels + .01*pennies
            if total < money_due:
                short = total - money_due
                proceed = input(f'You are short ${round(short, 2)}. \nWould you like to add more money? (y/n)')
                if proceed != 'y':
                    money_due = 0
                    return print(f'Here is your ${round(total, 2)} back. ')
                else:
                    continue
            else:
                resources["water"] -= MENU[res]["ingredients"]["water"]
                resources["coffee"] -= MENU[res]["ingredients"]["coffee"]
                resources["milk"] -= MENU[res]["ingredients"]["milk"]
                change = money_due - total
                print(f'${round(change, 2)} is your change. ')
                stop = False
        
        return money_due

    def report():
        print(f"""
            Water: {resources["water"]}ml
            Milk: {resources['milk']}ml
            Coffee: {resources['coffee']}ml
            Money: ${profit})
            """)
        return
        
    if drink_type == 'off':
        break
    elif drink_type == 'report':
        report()
        continue
    else:
        enough, statement = resource_check(drink_type)
        if enough == True:
            money_made = resource_update(drink_type)
            profit += money_made
            print(f'Here is your {drink_type}. Enjoy!')
        else:
            print(statement)
            
        






          
            
        






    


        