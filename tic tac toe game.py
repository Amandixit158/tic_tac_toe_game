# Tic Tac Toe Game

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Main function
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while moves < 9:
        # Prompt player for their move
        print(f"Player {players[current_player]}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        # Validate move
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)
            moves += 1

            # Check for a winner
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                return

            # switch to the other player
            current_player = 1 - current_player
        else:
            print("Invalid move, try again.")

    print("It's a draw!")

# run the game
if __name__ == "__main__":
    tic_tac_toe()