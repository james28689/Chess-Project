# pieces.py --- includes all class declarations for the various chess pieces

class Piece:
    def __init__(self, type, pos, colour):
        self.name = colour[0].lower() + type[0].upper()
        self.pos = pos
        self.colour = colour
        self.moveNo = 0

    def getName(self):
        return self.name
    
    def getMoves(self, board):
        # Non-implemented: - Implemented in child classes
        print("Why is this horrific text showing!!!")
        return []


class Pawn(Piece):
    def getMoves(self, board):
        possibleMoves = []

        if self.colour == "black":
            if board[self.pos[0]+1][self.pos[1]] == "--":
                possibleMoves.append([self.pos[0]+1, self.pos[1]])
            if self.moveNo == 0:
                if board[self.pos[0]+2][self.pos[1]] == "--":
                    possibleMoves.append([self.pos[0]+2, self.pos[1]])
            if board[self.pos[0]+1][self.pos[1]+1] != "--":
                possibleMoves.append([self.pos[0]+1, self.pos[1]+1])
            if board[self.pos[0]+1][self.pos[1]-1] != "--":
                possibleMoves.append([self.pos[0]+1, self.pos[1]-1])
        else:
            if board[self.pos[0]-1][self.pos[1]] == "--":
                possibleMoves.append([self.pos[0]-1, self.pos[1]])
            if self.moveNo == 0:
                if board[self.pos[0]-2][self.pos[1]] == "--":
                    possibleMoves.append([self.pos[0]-2, self.pos[1]])
            if board[self.pos[0]-1][self.pos[1]+1] != "--":
                possibleMoves.append([self.pos[0]-1, self.pos[1]+1])
            if board[self.pos[0]-1][self.pos[1]-1] != "--":
                possibleMoves.append([self.pos[0]-1, self.pos[1]-1])

        return possibleMoves

class Rook(Piece):
    def getMoves(self, board):
        print("Beep boop.")
