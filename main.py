# main.py --- contains main run loop and basic variable declarations (including state monitoring)
from board import BoardController
from logging import Logger

whiteToPlay = True
boardController = BoardController()
logger = Logger()
turn = 0
Running = True

while Running:
    print(" ")
    print("-------------------------")
    print(" ")
    boardController.display()
    print(" ")
    if whiteToPlay:
        print("White to play")
    else:
        print("Black to play")
    move = input("Make a move (Q -> quit, I -> info): ")

    if move == "Q" or move == "q":
        Running = False
    elif move == "I" or move == "i":
        print("A move consists of 3 parts: the piece's current position, and your requested position.")
        print(
            "An example move would be: e2 e4 - where the piece at e2 moves to e4")
    else:
        if boardController.movePiece(move, whiteToPlay):
            if whiteToPlay:
                turn += 1
            logger.addLine(move, boardController.board, turn)
            whiteToPlay = not whiteToPlay

