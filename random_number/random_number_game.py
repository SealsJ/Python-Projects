#Create a pick the random number game, but each round the number changes, and reduces the list by certain amount

#Creating a function to contain the game
def random_number(): 
    #Ensuring User enters appropriate answer for first number
    while True: 
        try:
            numberOne = int(input("Choose a number for the bottom of the range. > "))
        except ValueError:
            print("Sorry, please enter a valid number.")
            #Return to the start of the loop
            continue
        else:
            break

    #Ensuring User enters appropriate answer for second number
    while True: 
        try:
            numberTwo = int(input("Choose a number for the top of the range. > "))
        except ValueError:
            print("Sorry, please enter a valid number.")
            #Return to the start of the loop
            continue
        #Needs a valid range, prompts User to try a new number
        if numberOne >= numberTwo:
            print("Please enter a greater number than your first number.")
        else:
            break

    #Creating a variable to hold the random number based on User's range
    import random        
    correctNumber = random.randrange(numberOne, numberTwo)

    #Ensuring User enters appropriate answer for first guess
    while True:
        try:
            guess = int(input("Enter your guess based on the range given. > "))
        except ValueError:
            print("Sorry, please enter a valid number.")
            #Return to the start of the loop
            continue
        else:
            break

    #Creating functionality for User to continue guessing for the number           
    while guess != correctNumber:
        if guess < correctNumber:
            print("That guess was lower than the correct number.")
            try:
                guess = int(input("Enter your guess based on the range given. > "))
            except ValueError:
                print("Sorry, please enter a valid number.")
                #Return to the start of the loop
                continue
        elif guess > correctNumber:
            print("That guess was higher than the correct number.")
            try:
                guess = int(input("Enter your guess based on the range given. > "))
            except ValueError:
                print("Sorry, please enter a valid number.")
                #Return to the start of the loop
                continue
        else:
            break

    print("You have guessed the correct number!")

#Calling the game to play
random_number()

#Asking User if they wish to play again
while True:
    replay = input("Would you like to play again? (Y/N) > ").upper()
    if replay == 'Y':
        random_number()
    elif replay == 'N':
        break
    else:
        print("Please enter Y or N.")
        continue

print("Thanks for Playing!"
