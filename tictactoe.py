gameOver = False
placeHolders = ["", "", "", "", "", "", "", "", ""]
# initializing global variables
# if game is over or not and placeholders to place on the grid

possibleWins = [
# array of all the possible wins: vertical, horizontal, and diagonal
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def displayBoard(placeholders):
# function to draw the board
    grid = [ # placing the values of X or O in the grid
        [placeholders[0], placeholders[1], placeholders[2]],
        [placeholders[3], placeholders[4], placeholders[5]],
        [placeholders[6], placeholders[7], placeholders[8]]
    ]
    
    for i in range(len(grid)):
        print(grid[i]) # print grid like a 2D array

def changePlayer(currentplayer):
# function to change the player
    if currentplayer == "X": return "O" # if X then O
    if currentplayer == "O": return "X" # if O then X
    
def checkWin(currentplayer): 
# function to check for a win, draw, or to continue
    roundWon = False
    global gameOver # get global variable to change
    for i in range(len(possibleWins)):
        winCheck = possibleWins[i] # going through each possible wins
        cellA = placeHolders[winCheck[0]]
        cellB = placeHolders[winCheck[1]]
        cellC = placeHolders[winCheck[2]]
        # initialize all three positions of each possible win
        
        if cellA == "" or cellB == "" or cellC == "":
        # if any of the cells are empty: continue
            continue
        if (cellA == cellB) and (cellB == cellC):
        # if all three cells in one row/column/diagonal have the same value: round won
            roundWon = True
            break
    if roundWon: # if there is a winner
        print(f"{currentplayer}'s has won!")
        print("")
        displayBoard(placeHolders)
        gameOver = True
    elif "" not in placeHolders: # if there is no winner and all placeholders are filled: draw
        print("It's a draw.")
        print("")
        displayBoard(placeHolders)
        gameOver = True
    else: # else: continue game
        changePlayer(currentplayer)
    
def game():
# main game function
    print("Welcome To Tic Tac Toe!")
    print("")
    currentPlayer = "X" # define player to start game
    while not gameOver: # loop while game is not over
        displayBoard(placeHolders) # display board
        print("")
        correctMove = False # check for correct move made by player
        while not correctMove:
            print("It is " + currentPlayer + "'s Turn.")
            row = int(input("Pick a row (1 - 3): ")) - 1
            column = int(input("Pick a column (1 - 3): ")) - 1
            print("") # ask player to place their move
            index = (3 * row) + column # get the index of move
            if placeHolders[index] == "": # if player makes correct move
                placeHolders[index] = currentPlayer # update placeholders list
                correctMove = True
                checkWin(currentPlayer) # check win after move is made
                currentPlayer = changePlayer(currentPlayer) # reset current player to change
            else: # player makes incorrect move
                print("That spot is already occupied. Try again.")
                print("")

if __name__ == "__main__":
    game()