"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for board_row in range(3):
            for board_col in range(3):
                if board[board_row][board_col] is EMPTY:
                    possible_actions.add((board_row, board_col))
    return possible_actions

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    deep_copy = copy.deepcopy(board)
    i, j = action
    if deep_copy[i][j] is not EMPTY:
        raise ValueError("Invalid action: Cell already occupied.")
    deep_copy[i][j] = player(board)
    return deep_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    

    
    





if __name__ == "__main__":
    print("\nTesting winner function:")
    # No winner
    board = initial_state()
    print("Winner (should be None):", winner(board))

    # Row win
    board_row = [[X, X, X], [O, O, EMPTY], [EMPTY, EMPTY, EMPTY]]
    print("Winner (should be X):", winner(board_row))

    # Column win
    board_col = [[O, X, EMPTY], [O, X, EMPTY], [O, EMPTY, X]]
    print("Winner (should be O):", winner(board_col))

    # Diagonal win
    board_diag = [[X, O, O], [EMPTY, X, EMPTY], [O, EMPTY, X]]
    print("Winner (should be X):", winner(board_diag))

    # Anti-diagonal win
    board_anti = [[X, X, O], [X, O, EMPTY], [O, EMPTY, EMPTY]]
    print("Winner (should be O):", winner(board_anti))
    
    
   