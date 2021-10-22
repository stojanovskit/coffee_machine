MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def machine(start2):
    """Make the coffee"""
    resources["water"] -= MENU[start2]["ingredients"]["water"]
    resources["milk"] -= MENU[start2]["ingredients"]["milk"]
    resources["coffee"] -= MENU[start2]["ingredients"]["coffee"]
    print(f"Here is your {start2} ☕️. Enjoy!")
    bootup()


def pay(start):
    """Process payment"""
    print("Please insert coins")
    quarters = float(input('how many quarters?: '))
    dimes = float(input('how many dimes?: '))
    nickels = float(input('how many nickels?: '))
    pennies = float(input('how many pennies?: '))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    # print(total)
    if total > MENU[start]["cost"]:
        change = total - MENU[start]["cost"]
        resources["money"] += MENU[start]["cost"]
        print(f"Here is ${round(change,2)} in change.")
        machine(start)
    elif MENU[start]["cost"] == total:
        resources["money"] += MENU[start]["cost"]
        machine(start)
    else:
        print(total)
        print("Sorry that's not enough money. Money refunded.")
        bootup()


def check(start1):
    """Check if there are enough ingredients inside the machine """
    # start1=str("\"" + start1 + "\"")
    # print(start1)
    if MENU[start1]["ingredients"]["water"] > resources["water"]:
        print("Insufficient watter")
    elif MENU[start1]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient milk")
    elif MENU[start1]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient coffee")
    else:
        pay(start1)


def bootup():
    """ Startup the machine and take orders"""
    start = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if start == 'off':
        print("Coffee machine shutting down")
    elif start == 'report':
        print(
            f'''             
                 Water: {resources["water"]} 
                 Milk: {resources["milk"]} 
                 Coffee: {resources["coffee"]}
                 Money: ${resources["money"]}'''
        )
        bootup()
    else:
        check(start)


bootup()
