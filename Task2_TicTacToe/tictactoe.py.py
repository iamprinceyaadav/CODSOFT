import math

def create_board():
    return [" " for _ in range(9)]

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return " " not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = create_board()
    print("=" * 40)
    print("   Welcome to Tic-Tac-Toe AI!")
    print("   You are X, AI is O")
    print("   Board positions:")
    print("   1 | 2 | 3")
    print("   4 | 5 | 6")
    print("   7 | 8 | 9")
    print("=" * 40)

    while True:
        print_board(board)

        # Human turn
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("1 se 9 ke beech number do!")
                elif board[move] != " ":
                    print("Ye jagah already li hui hai!")
                else:
                    break
            except ValueError:
                print("Sirf number likho!")

        board[move] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Congratulations! Aap jeet gaye!")
            break

        if is_board_full(board):
            print_board(board)
            print("Draw hai!")
            break

        print("AI soch raha hai...")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        print(f"AI ne position {ai_move + 1} choose ki!")

        if check_winner(board, "O"):
            print_board(board)
            print("AI jeet gaya! Better luck next time!")
            break

        if is_board_full(board):
            print_board(board)
            print("Draw hai!")
            break

    again = input("\nDobara khelna hai? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()