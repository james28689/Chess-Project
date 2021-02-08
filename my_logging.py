# logging.py --- all code related to the logging of the game
import datetime

class Logger:
    def __init__(self):
        self.filename = f"logs/log{str(datetime.datetime.now())}.txt"
        
    
    def addLine(self, move, board, moveNo):
        labelsX = "abcdefgh"
        x = labelsX.index(move[3])
        y = 8 - int(move[4])

        pieceName = board[y][x].name[1].upper()
        if pieceName == "P":
            pieceName = ""

        with open(self.filename, "a") as f:
            f.write(f"{str(moveNo)}. {pieceName}{move[3:5]}\n")