WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

board = ["X",None,None,"X",None,None,"X",None,None]

def check_for_winner(board):
    for a, b, c in WINNING_LINES:
        if (board[a] == board[b] == board[c]) and (board[a] != None):
            return True
    else:
        return False

print(check_for_winner(board))