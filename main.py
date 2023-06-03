# Tic Tac Toe

# Function to print the board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def check_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic Tac Toe!")

    while not game_over:
        print_board(board)

        # Get the current player's move
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter the row number (1-3): ")) - 11
        col = int(input("Enter the column number (1-3): ")) - 1

        # Check if the chosen position is valid
        if board[row][col] != " ":
            print("Invalid move! That position is already taken.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_over = True
        # Check if the board is full (a tie)
        elif check_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

    print("Game over!")

# Start the game
play_game()
