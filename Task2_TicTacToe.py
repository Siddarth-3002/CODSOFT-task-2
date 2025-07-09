def print_board(board):
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_win(board, player):
    win_pos = [
        [0,1,2],[3,4,5],[6,7,8], 
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    return any(all(board[i] == player for i in pos) for pos in win_pos)

def is_draw(board):
    return ' ' not in board

def minimax(board, is_max):
    if check_win(board, 'O'): return 1
    if check_win(board, 'X'): return -1
    if is_draw(board): return 0

    if is_max:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best

def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' '] * 9
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board(board)
        if check_win(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("Draw!")
            break

        print("AI's turn...")
        ai = best_move(board)
        board[ai] = 'O'
        print_board(board)
        if check_win(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("Draw!")
            break

if __name__ == "__main__":
    play_game()