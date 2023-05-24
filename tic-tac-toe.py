import os

# clear the terminal screen
def clear_screen():
    os.system('clear')

# draw the board
def draw_board(board):
    clear_screen()
    print("  {} | {} | {}".format(board[0], board[1], board[2]))
    print("-----------")
    print("  {} | {} | {}".format(board[3], board[4], board[5]))
    print("-----------")
    print("  {} | {} | {}".format(board[6], board[7], board[8]))

# check for a winning condition
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True

    return False

# check if the board is full
def is_board_full(board):
    return all(cell != " " for cell in board)

# player input
def get_player_input(board, player):
    while True:
        move = input("Player {}, enter your move (1-9): ".format(player))
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Please try again.")

# main game function
def play_game():
    board = [" "] * 9
    current_player = "X"
    game_over = False

    while not game_over:
        draw_board(board)
        move = get_player_input(board, current_player)
        board[move] = current_player

        if check_win(board, current_player):
            draw_board(board)
            print("Player {} wins!".format(current_player))
            game_over = True
        elif is_board_full(board):
            draw_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

# start
play_game()
