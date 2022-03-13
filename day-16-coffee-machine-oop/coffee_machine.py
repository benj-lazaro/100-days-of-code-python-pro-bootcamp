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

    # If ordered beverage is available
    if coffee_order is not None:
        # Check if resources are available
        if coffee_maker.is_resource_sufficient(coffee_order):
            # Check if payment is sufficient
            if cash_register.make_payment(coffee_order.cost):
                # Make the ordered beverage
                coffee_maker.make_coffee(coffee_order)
    # Otherwise, check for hidden maintenance commands: off & report
    elif order == "off":
        # Turn off coffee maker
        is_coffee_machine_on = False
    elif order == "report":
        # Report on available resource & current profit
        coffee_maker.report()
        cash_register.report()
