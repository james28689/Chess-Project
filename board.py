# board.py --- includes any code related to the setup and monitoring of the board.
from pieces import Pawn

# REFACTORED:

class BoardController:
    def __init__(self):
        # Setups the board upon creation of the board controller. Once all pieces are implemented, simple strings will be replaced with children of the Piece object.

        self.board = [["--" for i in range(8)] for i in range(8)]

        for piece in self.board[1]:
            self.board[1][self.board[1].index(piece)] = Pawn(
                "pawn", [1, self.board[1].index(piece)], "black")
        for piece in self.board[6]:
            self.board[6][self.board[6].index(piece)] = Pawn(
                "pawn", [6, self.board[6].index(piece)], "white")

        self.board[0][0] = self.board[0][7] = "bR"
        self.board[0][1] = self.board[0][6] = "bN"
        self.board[0][2] = self.board[0][5] = "bB"
        self.board[0][3] = "bK"
        self.board[0][4] = "bQ"

        self.board[7][0] = self.board[7][7] = "wR"
        self.board[7][1] = self.board[7][6] = "wN"
        self.board[7][2] = self.board[7][5] = "wB"
        self.board[7][3] = "wK"
        self.board[7][4] = "wQ"
    
    def display(self):
        # Displays the board contained within the controller. Type checking to be removed once all pieces are implemented.

        for line in self.board:
            lineStr = ""
            for piece in line:
                if type(piece) == str:
                    lineStr += piece + " "
                else:
                    lineStr += piece.getName() + " "
            print(lineStr)
    
    def movePiece(self, piecePos):
        # Allows for the moving of pieces on the board.

        piece = self.board[piecePos[0], piecePos[1]]