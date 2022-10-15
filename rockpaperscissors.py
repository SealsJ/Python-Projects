#importing random so that the computer randomly selects a choice of r, p, or s
import random

#creating a play function that allows the user to make their deicision
def play():
    user = input("Welcome to the game! Please make a selection. 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if win(user, computer):
        return 'You won!'

    return 'You Lost!'

#create a function to specify conditions for the user to win
def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r'):
        return True

print(play())
    
