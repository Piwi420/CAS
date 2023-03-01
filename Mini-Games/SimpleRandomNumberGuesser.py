import random


secret_number = random.randint(1, 10)
life = 0
chances = 3

while life < chances:
    guess = int(input("Guess: "))
    life += 1
    if guess == secret_number:
        print("You won!")
        life = 3
    elif life < chances:
        print("Try again!")
    else:
        print(f"You lost!, the number was {secret_number}")

