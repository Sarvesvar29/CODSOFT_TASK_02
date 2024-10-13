import math
print("Welcome to Tic-Tac-Toe!")
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def check_winner(board, player):
    for row in board:
        if all([s == player for s in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1  # AI wins
    elif check_winner(board, 'X'):
        return -1  # Human wins
    elif is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            r, c = move
            board[r][c] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[r][c] = ' '
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            r, c = move
            board[r][c] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[r][c] = ' '
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        r, c = move
        board[r][c] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[r][c] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'

    while True:
        print_board(board)
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = human_player
                    break
                else:
                    print("Cell is already occupied!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers between 0 and 2.")

        if check_winner(board, human_player):
            print_board(board)
            print("You win!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        print("AI's turn...")
        r, c = ai_move(board)
        board[r][c] = ai_player

        if check_winner(board, ai_player):
            print_board(board)
            print("AI wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tac_toe()
