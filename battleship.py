# using random number generator again, this time for the placement of a ship
from random import randint

# 2-dimensional list for the battleship board
board = []

# uses for loop to create board
for x in range(0, 5):
    board.append(["O"] * 5)


# splits the list into spaces so it looks like a 5 x 5 grid
def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


# choosing the random row for the battleship
def random_row(board):
    return randint(0, len(board) - 1)


# choosing random column for the battleship
def random_col(board):
    return randint(0, len(board[0]) - 1)


# sets the random row and column to these variables
ship_row = random_row(board)
ship_col = random_col(board)


# loop for each of the user's turns
for turn in range(4):  # the player gets 4 turns
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))  # the player's guesses
    guess_col = int(input("Guess Col: "))

    # if the player guess right
    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "W"
        print("Congratulations! You sank my battleship!")
        print_board(board)
        break
    # if the player doesn't guess right
    else:
        # the guess is not on the board
        if guess_row not in range(5) or \
                guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        # the guess has been guessed already
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
            if range(4) == 4:
                print("Game Over")
        # the guess misses the battleship
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if range(4) == 4:
                print("Game Over")
        print_board(board)
