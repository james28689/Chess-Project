# main.py --- contains main run loop and basic variable declarations (including state monitoring)

from pieces import *
from board import *

whiteToPlay = True
board = setupBoard()
Running = True

while Running:
    print(" ")
    print("-------------------------")
    print(" ")
    displayBoard(board)
    print(" ")
    if whiteToPlay:
        print("White to play")
    else:
        print("Black to play")
    move = input("Make a move (Q -> quit, I -> info): ")

    if move == "Q" or move == "q":
        Running = False
    elif move == "I" or move == "i":
        print("A move consists of 3 parts: the piece type, it's current position, and your requested position.")
        print(
            "An example move would be: e2 e4 - where the piece at e2 moves to e4")
    else:
        labelsX = "abcdefgh"
        x1 = labelsX.index(move[0])
        y1 = 8 - int(move[1])

        x2 = labelsX.index(move[3])
        y2 = 8 - int(move[4])

        board[y1][x1].move(
            board, [y2, x2])
        whiteToPlay = not whiteToPlay

# e2 -> 46 -> 64
