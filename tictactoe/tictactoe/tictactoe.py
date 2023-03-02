"""
Tic Tac Toe Player
"""
import copy
import math

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
    counterOfX = 0
    counterOfO = 0

    for i in range(0,len(board)):
        for j in range (0,len(board[0])):
            if board[i][j] == X:
                counterOfX +=1
            elif board[i][j] == O:
                counterOfO +=1

    if counterOfX > counterOfO :
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None

    # check column
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None

    # check diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
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
    else:
        if player(board) == X:
            bestValue , bestMove = max_value(board)
            return bestMove
        else:
            bestValue ,bestMove = min_value(board)
            return bestMove

def max_value(board):

    if terminal(board):
        return [utility(board), None]

    alpha = float('-inf')
    move = None
    for action in actions(board):
        val, max_act = min_value(result(board , action))
        if val > alpha:
            alpha = val
            move = action
            if alpha == 1:
                return alpha , move
    return alpha , move

def min_value(board):

    if terminal(board):
        return [utility(board), None]

    beta = float('inf')
    move = None
    for action in actions(board):
        val, min_act = max_value(result(board, action))
        if val < beta:
            beta = val
            move = action
            if beta == -1:
                return beta, move
    return beta, move



