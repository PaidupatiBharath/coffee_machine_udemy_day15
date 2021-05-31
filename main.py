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
    "money": 0,
}


def resource_sufficient(flavor):
    current_resources = {"water": (resources["water"] - MENU[flavor]["ingredients"]["water"]),
                         "milk": (resources["milk"] - MENU[flavor]["ingredients"]["milk"]),
                         "coffee": (resources["coffee"] - MENU[flavor]["ingredients"]["coffee"])}
    for _ in current_resources:
        if current_resources[_] < 0:
            print(f"Sorry there is not enough {_}")
            return False
        else:
            return True


def update_resource(flavor):
    resources["water"] -= MENU[flavor]["ingredients"]["water"]
    resources["milk"] -= MENU[flavor]["ingredients"]["milk"]
    resources["coffee"] -= MENU[flavor]["ingredients"]["coffee"]


def check_transaction(coins, flavor):
    change = coins - MENU[flavor]["cost"]
    if change < 0:
        print("Sorry that's not enough money. Money refunded")
    elif change > 0:
        print(f"Here is ${round(change, 2)} dollars in change")
        resources["money"] += MENU[flavor]["cost"]
        update_resource(flavor)
        print(f"Here is your {flavor}. Enjoy!")
    elif change == 0:
        resources["money"] += MENU[flavor]["cost"]
        update_resource(flavor)
        print(f"Here is your {flavor}. Enjoy!")


def process_coins(quarter, dime, nickle, pennie):
    total_value = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01)
    return total_value


end = False
while not end:
    user_input = input("What would you like? (espresso/latte/cappuccino) : ")
    if user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue
    elif user_input == "off":
        print("Turning off for Maintenance")
        end = True
        continue
    elif resource_sufficient(user_input):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total_coins = process_coins(quarters, dimes, nickles, pennies)
        check_transaction(total_coins, user_input)


# Check on : https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py
