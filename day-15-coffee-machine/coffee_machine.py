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


def check_resources(order):
    """Takes coffee order, checks current resources & return state of order"""
    current_water = resources['water']
    current_milk = resources['milk']
    current_coffee = resources['coffee']

    if order == "espresso":
        required_water = MENU[order]['ingredients']['water']
        required_coffee = MENU[order]['ingredients']['coffee']

        if current_water < required_water:
            print("Sorry there is not enough water.")
            return False
        elif current_coffee < required_coffee:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    else:
        required_water = MENU[order]['ingredients']['water']
        required_milk = MENU[order]['ingredients']['milk']
        required_coffee = MENU[order]['ingredients']['coffee']

        if current_water < required_water:
            print("Sorry there is not enough water.")
            return False
        elif current_milk < required_milk:
            print("Sorry there is not enough milk.")
            return False
        elif current_coffee < required_coffee:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True


def deduct_resources(order):
    """Deduct resources based on order"""
    current_water = resources['water']
    current_milk = resources['milk']
    current_coffee = resources['coffee']

    if order == "espresso":
        consumed_water = MENU[order]['ingredients']['water']
        consumed_coffee = MENU[order]['ingredients']['coffee']
        resources['water'] = current_water - consumed_water
        resources['coffee'] = current_coffee - consumed_coffee
    else:
        consumed_water = MENU[order]['ingredients']['water']
        consumed_milk = MENU[order]['ingredients']['milk']
        consumed_coffee = MENU[order]['ingredients']['coffee']
        resources['water'] = current_water - consumed_water
        resources['milk'] = current_milk - consumed_milk
        resources['coffee'] = current_coffee - consumed_coffee


def process_coins(order, quarter, dime, nickle, penny):
    """Takes coffee order, inserted coins and return order"""
    num_of_quarters = QUARTER * quarter
    num_of_dimes = DIME * dime
    num_of_nickles = NICKLE * nickle
    num_of_pennies = PENNY * penny
    total_coin_value = num_of_quarters + num_of_dimes + num_of_nickles + num_of_pennies
    order_cost = MENU[order]['cost']

    if total_coin_value >= order_cost:
        change = total_coin_value - order_cost
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {order} ☕. Enjoy!")
        deduct_resources(order)
        return order_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return


def report_resources():
    """Prints the current state of resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${current_money}")


# Constant variables
PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25

# Global variables
coffee_machine_on = True
make_order = False
current_money = 0

while coffee_machine_on:
    user_order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    # Check if coffee machine is ordered to be turned off
    if user_order == "off":
        coffee_machine_on = False
    # Check if coffee machine is reported to report current resources
    elif user_order == "report":
        report_resources()
        make_order = False
    # Otherwise, check if resources are available to make coffee
    else:
        make_order = check_resources(user_order)

    # Ask for coins, make coffee & deduct resources
    if make_order:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        sales = process_coins(user_order, quarters, dimes, nickles, pennies)
        current_money += sales
