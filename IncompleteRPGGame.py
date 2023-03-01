import math
import random

user_name = input("Please enter a Username: ")
balance = 0
inventory = ""




print("""
    type help for commands
""")

command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("""
        farm - farms mobs
        shop - opens shop
        bal - displays your balance
        inv - opens your inventory
        back - returns you to last gui
        """)

    elif command == "farm":
        drops = ["Eye ball", "Tongue", "Animal's Leg"]
        drop1 = random.choice(drops)
        drop2 = random.choice(drops)
        print(f"You went farming and received: {drop1}, {drop2}")

        # drop3 = f"{drop1}, "
        # drop4 = f"{drop2}, "
        # inventory += drop3
        # inventory += drop4
        if inventory == "":
            inventory = f"{drop1}, {drop2}"
        else:
            inventory = ", ".join([inventory, drop1, drop2])

    elif command == "shop":
        print("""
        Item:                   Sell Price:         Buy Price:
        Eye Ball                $10                 $20
        Tongue                  $12                 $24
        Animal's Leg            $20                 $40
        
        Type "s" to sell
        Type "b" to buy
        """)
        command = ""

    elif command == "bal":
        print(balance)

    elif command == "inv":
        if inventory == "":
            print("You have not farmed yet.")
        else:
            print(f"Contents: {inventory}")
    if command == "b":
        prompt = "What would you like to buy: "
        balls = "How many Eye ball(s) would you like to buy?"

        sellItem = input(prompt)
    elif input == "Eye Ball":
        print(balls)

    elif command == "s":
        print("What would you like to sell: ")








