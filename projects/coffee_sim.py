#create code for a coffee machine
#3 hot flavors, espresso, latte, cappuccino
#coin operates
#initialize dictionary
coffee_on = True
water = 10000
coffee = 500
milk = 10000
profit = 0
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

def is_resource_sufficient(order_ingredients):
    """returns true when order can be made, else false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            return True #true

def process_coins():
    """returns total calculated from coins inserted"""
    print(f"Please instert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def is_transaction_succesful(money_recieved, drink_cost):
    """return true when payment is accepted, else false"""
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost #bc profit is a global in local scope
        change = round(money_recieved - drink_cost, 2) #round to 2 decimal places
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money...")
        return False #return must be last in function

def make_coffee(drink_name, order_ingredients):
    """deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}  ")


while coffee_on:
    choice = input("What type of coffee would you like, espresso, latte, or cappuccino. Enter 'off' to turn the machine off. Would you like to print resources? Select 'report'.")
    if choice == "off":
        coffee_on == False
    elif choice == "report":
        print(f"Water: {resources['water']}ml. ")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins() #returns output and saves in payment
            is_transaction_succesful(payment, drink["cost"]) #pass through function
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"]) #transction is succesful and resources are sufficient

        print(drink)




#print report of coffee machine resources