from menu_items import MENU
from art import Image, Description

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
    "money": 0,
}

choice = ""

coins = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(choice):
    if choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        return True
    elif choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        return True
    elif choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False
        return True
    else:
        print("Invalid choice. Please try again.")
        return False

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def check_transaction(type, coins):
    if coins < MENU[type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif coins > MENU[type]["cost"]:
        change = coins - MENU[type]["cost"]
        print(f"Here is your change: ${change:.2f}")
        return True
    else:
        return True

def deduct_resources(type):
    resources["water"] -= MENU[type]["ingredients"]["water"]
    resources["milk"] -= MENU[type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[type]["ingredients"]["coffee"]

end_coffee_maker = False

while not end_coffee_maker:
    print(Image)
    print(Description)
    choice = input("Type an option from the menu: ").lower()

    if choice == "off":
        print("Turning off the coffee machine...")
        end_coffee_maker = True
    elif choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            coins = insert_coins()
            if check_transaction(choice, coins):
                resources["money"] += MENU[choice]["cost"]
                deduct_resources(choice)
                print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("Invalid choice. Please try again.")