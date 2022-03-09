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


def check_resources(order_ingredients):
    """Accepts order ingredients and check if resources are available"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def deduct_resources(order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


def process_coins():
    """Accepts coins and returns the total value"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_coin_value = quarters + dimes + nickles + pennies
    return total_coin_value


def transaction_check(inserted_money, order_cost):
    """Checks provided money, compute the change & return True to start making coffee"""
    if inserted_money >= order_cost:
        change = inserted_money - order_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Global variables
is_coffee_machine_on = True
current_profit = 0

while is_coffee_machine_on:
    user_order = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    # Checks if 'hidden' commands have been issued
    if user_order == "off":
        # Turns off the coffee machine
        is_coffee_machine_on = False
    elif user_order == "report":
        # Print available resources & current profit
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {current_profit}")
    else:
        # Otherwise, take user order
        coffee_order = MENU[user_order]

        # Checks if available resources are sufficient to make the order
        if check_resources(coffee_order['ingredients']):
            # Receives and process payment in coins
            user_money = process_coins()

            # Checks if money received is sufficient, start making coffee
            if transaction_check(user_money, coffee_order['cost']):
                # Deduct ingredients from resources
                deduct_resources(coffee_order['ingredients'])
                print(f"Here is your {user_order} ☕. Enjoy!")
                # Record current profit
                current_profit += coffee_order['cost']