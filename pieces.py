# pieces.py --- includes all class declarations for the various chess pieces
from moves import getPawnMoves, getRookMoves, getBishopMoves, getKnightMoves, getKingMoves, checkAllMoves, removeKingTake

class Piece:
    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour
        self.moveNo = 0
        self.name = "xx"

    def getName(self):
        return self.name
    
    def getMoves(self, board):
        # Non-implemented: - Implemented in child classes
        print("Why is this horrific text showing!!!")
        return []


class Pawn(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "p"

    def getMoves(self, board):
        possibleMoves = getPawnMoves(self.pos, board, self.colour, self.moveNo)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)
        return possibleMoves

class Rook(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "r"

    def getMoves(self, board):
        possibleMoves = getRookMoves(self.pos, board, self.colour)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)
        return possibleMoves
                

class Bishop(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "b"
    
    def getMoves(self, board):
        possibleMoves = getBishopMoves(self.pos, board, self.colour)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)
        return possibleMoves

class Knight(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "n"
    
    def getMoves(self, board):
        possibleMoves = getKnightMoves(self.pos, board, self.colour)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)
        return possibleMoves

class Queen(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "q"
    
    def getMoves(self, board):
        possibleMoves = getRookMoves(self.pos, board, self.colour) + getBishopMoves(self.pos, board, self.colour)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)
        return possibleMoves

class King(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "k"
    
    def getMoves(self, board):
        possibleMoves = getKingMoves(self.pos, board, self.colour, self.moveNo)
        possibleMoves = removeKingTake(board, self.colour, possibleMoves)

        allMoves = checkAllMoves(board, self.colour)

        for move in possibleMoves:
            if move in allMoves:
                possibleMoves.remove(move)
    
        return possibleMoves