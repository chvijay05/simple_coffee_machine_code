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
        "cost": 1.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 1.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_report(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"sorry we have less {i}")
            return False
    return True


def sum_coins(coffee, order):
    """ Gives the sum of inserted coins"""
    print("Please insert coins.")

    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes ?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_inserted = quarters + dimes + nickles + pennies
    if total_inserted >= coffee["cost"]:
        global profit
        profit += coffee["cost"]
        change = round(total_inserted - coffee["cost"], 2)
        print(f"Here is your change {change}.")
        print(f"Here is your {order}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def resource_reduction(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_on = True

while is_on:
    order = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"'water':{resources['water']}ml")
        print(f"'milk':{resources['milk']}ml")
        print(f"'coffee':{resources['coffee']}ml")
        print(f"'Money': £{profit}")
    else:
        drink = MENU[order]
        if resources_report(drink["ingredients"]):
            sum_coins(drink, order)
            resource_reduction(drink["ingredients"])
