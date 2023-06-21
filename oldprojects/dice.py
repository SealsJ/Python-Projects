#Use the random function so that it'll choose a random side of the dice
import random

#Created a dice function that'll call roll the dice and give a random number
def dice():
    #While loop to eliminate random or unexpected user inputs
    while True:
        roll = input("Do you want to roll the dice?(Y or N): ").lower() #.lower to simplify user inputs
        if roll == "y":
            diceSides = [1, 2, 3, 4, 5, 6]
            randomSide = random.choice(diceSides)
            randomSideTwo = random.choice(diceSides)
            print(f"You rolled a {randomSide} on the first die and your second die was a {randomSideTwo}.")
        elif roll == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please input a valid choice!")

#Calling the dice function so the user can play the game
dice()
