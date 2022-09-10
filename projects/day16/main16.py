# #attribute = variable that is associated with model object
# #object oriented programming
# #object = Class()
# from turtle import Turtle, Screen
# import another_module
#
# timmy = Turtle() #creates object
# #object.attribute calls an attribute
# print(timmy)
# timmy.shape("turtle") #changes object shape
# timmy.color("coral") #tap into object.method
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.canvheight #access attribute from object
# print(my_screen.canvheight)
#
# my_screen.exitonclick() #object.method
# #allows program to continue running until click

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
#object = class
is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items() #calls get item methods and saves string into options
    choice = input(f"What would you like? ({options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

