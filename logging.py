# logging.py --- all code related to the logging of the game
from os import listdir

class Logger:
    def __init__(self):
        sortedfiles = sorted(listdir("logs/"), key = lambda x: int(x[3:-4]))
        print(sortedfiles)
        if len(sortedfiles) > 0:
            self.filename = f"logs/log{str(int(sortedfiles[-1][3:-4])+1)}.txt"
        else:
            self.filename = f"logs/log1.txt"
        
    
    def addLine(self, move, board, moveNo):
        labelsX = "abcdefgh"
        x = labelsX.index(move[3])
        y = 8 - int(move[4])

        pieceName = board[y][x].name[1].upper()
        if pieceName == "P":
            pieceName = ""

        with open(self.filename, "a") as f:
            f.write(f"{str(moveNo)}. {pieceName}{move[3:5]}\n")