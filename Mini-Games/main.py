from GNT import guess_the_number
from RPS import rock_paper_scissors
from Wordle import Wordle
from connectFour import ConnectFour
from TTT import TTT

while True:
    txt = """"Mini Games!!!
    - Guess the number (1)
    - Rock, Paper, Scissors (2)
    - Wordle (3)
    - ConnectFour (4)
    - Tic Tac Toe (5)
Select a game (press q to quit): """
    value = input(txt)
    if value == "1":
        guess_the_number(100)
        # TODO: ask the user for second input for upper bound
    elif value == "2":
        rock_paper_scissors()
        #TODO: check against all possible cases, "rock smashes scissors"
    elif value == "3":
        game = Wordle()
        game.play()
    elif value == "4":
        game = ConnectFour()
        game.play()
    elif value == "5":
        game = TTT()
        game.play()
    elif value == "q":
        break
