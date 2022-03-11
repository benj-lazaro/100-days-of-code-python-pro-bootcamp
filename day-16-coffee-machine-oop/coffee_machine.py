# Import modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Global variables
is_coffee_machine_on = True

# Instantiate objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
cash_register = MoneyMachine()

while is_coffee_machine_on:
    # Get user's order
    order = str(input(f"What would you like? ({menu.get_items()}): ")).lower()

    # Check for existence of preferred hot beverage
    coffee_order = menu.find_drink(order)

    # Check for hidden maintenance commands "report" & "off"
    if order == "off":
        # Turn off coffee maker
        is_coffee_machine_on = False
    elif order == "report":
        # Produce report on available resource & profit
        coffee_maker.report()
        cash_register.report()
    elif coffee_order:
        # Check if resources available to accommodate the order
        if coffee_maker.is_resource_sufficient(coffee_order):
            # Check if payment is sufficient
            if cash_register.make_payment(coffee_order.cost):
                # Make ordered coffee drink
                coffee_maker.make_coffee(coffee_order)
