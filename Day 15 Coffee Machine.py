MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

drink_type = input('What would you like? (espresso/latte/cappuccino): ',)

def resource_check(res = drink_type):
    enough = bool
    water_needed = MENU[res["ingredients"["water"]]]
    water_availible = resources["water"]
    coffee_needed = MENU[res["ingredients"["coffee"]]]
    coffee_availible = resources["coffee"]
    milk_needed = MENU[res["ingredients"["milk"]]]
    milk_availible = resources["milk"]
    if water_needed > water_availible:
        statement = 'Sorry there is not enough water'
        enough = False
        return statement, enough
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
        return enough

proceed, response = resource_check(drink_type)
    
if proceed == False:
    print(response)
    #exit while loop


def money_tracker(res = drink_type):
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    money_due = MENU[res["cost"]]
    total = .25*quarters + .1*dimes + .05*nickels + .01*pennies
    if total < money_due:
        short = total - money_due
        proceed = input('You are short ${short}. \nWould you like to add more money? (y/n)')
        if proceed == 'y':
            
        



profit = 0


if drink_type == 'off':
    print('Nice doing business with you')
elif drink_type == 'report':
    print()
elif drink_type == 'espresso':
    resource_check(drink_type)
    


        