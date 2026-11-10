WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

board = [None,None,None,None,None,None,None,None,None]

def check_for_winner(board):
    for a, b, c in WINNING_LINES:
        if (board[a] == board[b] == board[c]) and (a != None):
            return True
    else:
        return False




def print_board(board):

    # Makes a separate 
    boardp = []
    for i in board:
        if i:
            boardp.append(i)
        else:
            boardp.append(" ")

    print("")
    print(f"[1] {boardp[0]} |[2] {boardp[1]} |[3] {boardp[2]} ")
    print(f"------+------+------")
    print(f"[4] {boardp[3]} |[5] {boardp[4]} |[6] {boardp[5]} ")
    print(f"------+------+------")
    print(f"[7] {boardp[6]} |[8] {boardp[7]} |[9] {boardp[8]} ")
    print("")



def checks_board_isnt_full(board):
    for i in board:
        if not i:
            return True
    return False




def main():
    board = [None,None,None,None,None,None,None,None,None]

    print_board(board)

    while checks_board_isnt_full(board):
        player_X = int(input("Player X, enter your position: "))
        board[player_X - 1] = "X" # type: ignore
        print_board(board)

        if check_for_winner(board):
            print("You've won!")


        player_O = int(input("Player Y, enter your position: "))
        board[player_O - 1] = "O" # type: ignore
        print_board(board)

main()






# Represent the board as a list named board containing nine elements. The first three elements represent the top row from left to right, the next three represent the middle row, and the last three represent the bottom row.
# A list index is the position used in the code, from 0 to 8. For example, the center cell has index 4.
# A cell number is the number the player sees and enters, from 1 to 9. It is one greater than the index, so the center cell is numbered 5.
# A cell value is the value stored in the list at that index. At the start of the game, all values are None. If player X chooses cell 5, store the value "X" at the corresponding position in the list.
# On every turn, construct the display from the list and print the board in its current state.
# In each cell, print its number in square brackets. If the cell value is truthy, print the player's symbol next to the brackets. Otherwise, leave a space there.
# For example, if the value at index 4 in the list is "X", display the center cell as [5] X. The number in brackets identifies the cell to choose; the symbol beside it shows what is stored there.