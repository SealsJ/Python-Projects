#Step 1: Prompt the User to give an input to be an X or an O
#Step 2: Display the 3x3 Grid and prompt player 1 to pick a spot
#Step 3: Check board if there is a winner or all spots are filled (Game Over)
#Step 4: Prompt player 2 the same as player 1 / repeat same validation of the board
#Step 5: Loop through these steps until there is a winner or a tie

#    0   1   2  <-- Acess the grid through a coordinate system
# 0  []  []  []
# 1  []  []  []
# 2  []  []  []

print("------Welcome to Tic-Tac-Toe!------")


#Creating while loop to keep prompting the user to put in a valid input
while True:
    playerOne = input("Please choose your character, X or O?: ").upper()

    if playerOne == "X" or playerOne == "O":
        print("Nice Choice!")
        print()
        break
    else:
        print("Please Enter a Valid Character!")
        continue

#Assigning Player 2 their character based on Player 1 choice
if playerOne == "X":
    playerTwo = "O"
else:
    playerTwo = "X"

#Creating the 3x3 Grid
grid = []
for row in range(3):
    grid.append([''] * 3)

#Establish a function that determines the validity of a player move
def valid(row, column):
    if not (row >= 0 and row < 3 and column >= 0 and column < 3):
        return False

    return grid[row][column] == ""

#Establih a function that will keep making player input until a valid move
def playerMove(character):
    validMove = False

    while not validMove:
        rowInput = int(input("Please pick a row: "))
        columnInput = int(input("Please pick a column: "))

        validMove = valid(rowInput, columnInput)
        if not validMove:
            print("Please enter a valid movement!")

    #player will represent the character they choose
    grid[rowInput][columnInput] = character

#Check the board to determine if there is a winner or board full
def checkHorizontal():
    for row in range(3):
        character = grid[row][0]
        if character == "":
            continue

        matches = 1
        for column in range(1, 3):
            if character == grid[row][column]:
                matches += 1

        if matches == 3:
            return True

    return False

def checkVertical():
    for column in range(3):
        character = grid[0][column]
        if character == "":
            continue

        matches = 1
        for row in range(1,3):
            if character == grid[row][column]:
                matches += 1

            if matches == 3:
                return True

        return False

def diagonal(row, column, increment):
    character = grid[row][column]
    if character == "":
        return False

    matches = 1
    for _ in range(2):
        row += increment
        column += increment
        if character == grid[row][column]:
            matches += 1

    return matches == 3

def checkDiagonal():
    return diagonal(0, 0, 1) or diagonal(0, 2, -1)

def checkGrid():
    return checkHorizontal() or checkVertical() or checkDiagonal()

def gridFull():
    for row in range(3):
        for column in range(3):
            if grid[row][column] == "":
                return False
    return True

#Creating the game loop for the code through a while loop / function
def ticTacToe():
    while True:
        for character in [playerOne, playerTwo]:
            playerMove(character)

            for row in range(3):
                print(grid[row])

            if checkGrid():
                print(character, "Wins Tic-Tac-Toe!")
                return

            if gridFull():
                print("Game Over!")
                return

ticTacToe()