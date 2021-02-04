# board.py --- includes any code related to the setup and monitoring of the board.
from pieces import Knight, Piece, Pawn, Rook, Bishop

# REFACTORED:

class BoardController:
    def __init__(self):
        # Setups the board upon creation of the board controller. Once all pieces are implemented, simple strings will be replaced with children of the Piece object.

        self.board = [[None for i in range(8)] for i in range(8)]

        for piece in self.board[1]:
            self.board[1][self.board[1].index(piece)] = Pawn([1, self.board[1].index(piece)], "black")
        for piece in self.board[6]:
            self.board[6][self.board[6].index(piece)] = Pawn([6, self.board[6].index(piece)], "white")

        self.board[0][0] = Rook([0, 0], "black")
        self.board[0][7] = Rook([0, 7], "black")
        self.board[0][1] = Knight([0, 1], "black") # black knight
        self.board[0][6] = Knight([0, 6], "black") # black knight
        self.board[0][2] = Bishop([0, 2], "black") # black bishop
        self.board[0][5] = Bishop([0, 5], "black") # black bishop
        self.board[0][3] = Piece([0, 3], "black") # black king
        self.board[0][4] = Piece([0, 4], "black") # black queen

        self.board[7][0] = Rook([7, 0], "white")
        self.board[7][7] = Rook([7, 7], "white")
        self.board[7][1] = Knight([7, 1], "white") # white knight
        self.board[7][6] = Knight([7, 6], "white") # white knight
        self.board[7][2] = Bishop([7, 2], "white") # white bishop
        self.board[7][5] = Bishop([7, 5], "white") # white bishop
        self.board[7][3] = Piece([7, 3], "white") # white king
        self.board[7][4] = Piece([7, 4], "white") # white queen
    
    def display(self):
        # Displays the board contained within the controller. Type checking to be removed once all pieces are implemented.

        for line in self.board:
            lineStr = ""
            for piece in line:
                if piece == None:
                    lineStr += "-- "
                else:
                    if type(piece) == str:
                        lineStr += piece + " "
                    else:
                        lineStr += piece.getName() + " "
            print(lineStr)
    
    def movePiece(self, move, whiteToPlay):
        # Allows for the moving of pieces on the board.

        labelsX = "abcdefgh"
        x1 = labelsX.index(move[0])
        y1 = 8 - int(move[1])

        x2 = labelsX.index(move[3])
        y2 = 8 - int(move[4])

        posDown = y1
        posAlong = x1

        newPosDown = y2
        newPosAlong = x2

        neededColor = "white" if whiteToPlay else "black"

        if type(self.board[posDown][posAlong]) == str:
            print("This cannot be moved, this piece type has not yet been created.")
        else:
            if [newPosDown, newPosAlong] in self.board[posDown][posAlong].getMoves(self.board) and self.board[posDown][posAlong].colour == neededColor:
                self.board[posDown][posAlong].pos = [newPosDown, newPosAlong]
                self.board[newPosDown][newPosAlong] = self.board[posDown][posAlong]
                self.board[posDown][posAlong] = None
            else:
                print("Invalid move.")