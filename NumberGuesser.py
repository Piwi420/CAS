import random

upper_lim = int(input("Set the Upper Limit\n> "))

x = upper_lim
guesses = 0
random_number = random.randint(0, x)

while True:

    user_guess = input("Make a guess\n> ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print("Please Type a Number")
        continue

    if user_guess > random_number:
        print("Too high!")
    if user_guess < random_number:
        print("Too Low!")
    if user_guess == random_number:
        print(f"You won! The number was {random_number}!")
        print(f"You got it in {guesses} guesses!")
        break
