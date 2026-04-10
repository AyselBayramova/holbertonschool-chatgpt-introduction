#!/usr/bin/python3

def print_board(board):
    """
    Prints the current Tic-Tac-Toe board in a readable format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Checks if there is a winner in the Tic-Tac-Toe game.
    Returns True if a player has won, otherwise False.
    """

    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check reverse diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    Handles player input and game flow.
    """

    # Create empty 3x3 board
    board = [[" "]*3 for _ in range(3)]

    player = "X"  # Player X starts first

    # Continue game until there is a winner
    while not check_winner(board):
        print_board(board)

        # Get player move
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

        # Check if cell is empty
        if board[row][col] == " ":
            board[row][col] = player

            # Switch player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    # Final board and winner message
    print_board(board)
    print("Player " + player + " wins!")


# Start the game
tic_tac_toe()
