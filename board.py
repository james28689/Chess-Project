# board.py --- includes any code related to the setup and monitoring of the board.
from pieces import *


def setupBoard():
    board = [["--" for i in range(8)] for i in range(8)]

    for piece in board[1]:
        board[1][board[1].index(piece)] = Pawn(
            "pawn", [1, board[1].index(piece)], "black")
    for piece in board[6]:
        board[6][board[6].index(piece)] = Pawn(
            "pawn", [6, board[6].index(piece)], "white")

    board[0][0] = board[0][7] = "bR"
    board[0][1] = board[0][6] = "bN"
    board[0][2] = board[0][5] = "bB"
    board[0][3] = "bK"
    board[0][4] = "bQ"

    board[7][0] = board[7][7] = "wR"
    board[7][1] = board[7][6] = "wN"
    board[7][2] = board[7][5] = "wB"
    board[7][3] = "wK"
    board[7][4] = "wQ"

    return board


def displayBoard(board):
    for line in board:
        lineStr = ""
        for piece in line:
            if type(piece) == str:
                lineStr += piece + " "
            else:
                lineStr += piece.getName() + " "
        print(lineStr)
