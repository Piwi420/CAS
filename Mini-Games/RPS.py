import random

def rock_paper_scissors():
    print("Let's play Rock, Paper, Scissors!")

    r = "rock"
    p = "paper"
    s = "scissors"
    all_choices = [r, p, s]

    user = input(f"Enter a choice ({r}, {p}, {s}): ")

    if user not in all_choices:
        print("Invalid Choice")
        return

    computer = random.choice(all_choices)

    print(f"User chose {user}, computer chose {computer}")

    if user == computer:
        print("Tie!")
    elif (user == r and computer == s) or (user == p and computer == r) or (user == s and computer == p):
        print("You Won!")
    else:
        print("You Lost!")