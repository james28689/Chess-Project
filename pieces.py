# pieces.py --- includes all class declarations for the various chess pieces
# TODO: - Clean up disgusting code in getMoves() for Pawn. Move Rook and Bishop movement to external functions for queen.

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
        possibleMoves = []

        standard = [-1,0]
        ifOccupied = [[-1,-1], [-1,1]]
        ifFirst = [-2,0]
        if self.colour == "black":
            standard[0] *= -1
            ifOccupied[0][0] *= -1
            ifOccupied[1][0] *= -1
            ifFirst[0] *= -1

        if self.pos[0] + standard[0] <= 7:
            if board[self.pos[0] + standard[0]][self.pos[1]] == None:
                possibleMoves.append([self.pos[0] + standard[0], self.pos[1]])
        
        for move in ifOccupied:
            proposedMove = [self.pos[0] + move[0], self.pos[1] + move[1]]
            if proposedMove[0] <= 7 and proposedMove[0] >= 0 and proposedMove[1] <= 7 and proposedMove[1] >= 0:
                if board[proposedMove[0]][proposedMove[1]] != None:
                    if board[proposedMove[0]][proposedMove[1]].colour != self.colour:
                        possibleMoves.append(proposedMove)
        
        if self.moveNo == 0:
            possibleMoves.append([self.pos[0] + ifFirst[0], self.pos[1] + ifFirst[1]])
        
        return possibleMoves
        


class Rook(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "r"

    def getMoves(self, board):
        return getRookMoves(self.pos, board, self.colour)
                

class Bishop(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "b"
    
    def getMoves(self, board):
        return getBishopMoves(self.pos, board, self.colour)

class Knight(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "n"
    
    def getMoves(self, board):
        possibleMoves = []
        allRelativeMoves = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1, -2], [-1, -2], [-2, -1]]

        for relativeMove in allRelativeMoves:
            newProposedPos = [self.pos[0] + relativeMove[0], self.pos[1] + relativeMove[1]]
            if not(newProposedPos[0] < 0 or newProposedPos[0] > 7 or newProposedPos[1] < 0 or newProposedPos[1] > 7):
                if board[newProposedPos[0]][newProposedPos[1]] == None:
                    possibleMoves.append(newProposedPos)
                else:
                    if board[newProposedPos[0]][newProposedPos[1]].colour != self.colour:
                        possibleMoves.append(newProposedPos)
        return possibleMoves

class Queen(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "q"
    
    def getMoves(self, board):
        return getRookMoves(self.pos, board, self.colour) + getBishopMoves(self.pos, board, self.colour)

class King(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "k"
    
    def getMoves(self, board):
        possibleMoves = getKingMoves(self.pos, board, self.colour, self.moveNo)

        allMoves = checkAllMoves(board, self.colour)

        for move in possibleMoves:
            if move in allMoves:
                possibleMoves.remove(move)

        print(possibleMoves)
        return possibleMoves


def getRookMoves(pos, board, colour):
    possibleMoves = []
    superSearching = True
    searching1 = True
    searching2 = True
    searching3 = True
    searching4 = True
    count = 1

    while superSearching:
        if not searching1 and not searching2 and not searching3 and not searching4:
            superSearching = False
        else:
            if searching1:
                if pos[0] - count < 0:
                    searching1 = False
                else:
                    if board[pos[0] - count][pos[1]] == None:
                        possibleMoves.append([pos[0] - count, pos[1]])
                    else:
                        if board[pos[0] - count][pos[1]].colour != colour:
                            possibleMoves.append([pos[0] - count, pos[1]])
                        searching1 = False
            if searching2:
                if pos[1] + count > 7:
                    searching2 = False
                else:
                    if board[pos[0]][pos[1] + count] == None:
                        possibleMoves.append([pos[0], pos[1] + count])
                    else:
                        if board[pos[0]][pos[1] + count].colour != colour:
                            possibleMoves.append([pos[0], pos[1] + count])
                        searching2 = False
            if searching3:
                if pos[0] + count > 7:
                    searching3 = False
                else:
                    if board[pos[0] + count][pos[1]] == None:
                        possibleMoves.append([pos[0] + count, pos[1]])
                    else:
                        if board[pos[0] + count][pos[1]].colour != colour:
                            possibleMoves.append([pos[0] + count, pos[1]])
                        searching3 = False
            if searching4:
                if pos[1] - count < 0:
                    searching4 = False
                else:
                    if board[pos[0]][pos[1] - count] == None:
                        possibleMoves.append([pos[0], pos[1] - count])
                    else:
                        if board[pos[0]][pos[1] - count].colour != colour:
                            possibleMoves.append([pos[0], pos[1] - count])
                        searching4 = False
            count += 1
    return possibleMoves

def getBishopMoves(pos, board, colour):
    possibleMoves = []
    superSearching = True
    searching1 = True
    searching2 = True
    searching3 = True
    searching4 = True
    count = 1

    while superSearching:
        if not searching1 and not searching2 and not searching3 and not searching4:
            superSearching = False
        else:
            if searching1:
                if pos[0] - count < 0 or pos[1] - count < 0:
                    searching1 = False
                else:
                    if board[pos[0] - count][pos[1] - count] == None:
                        possibleMoves.append([pos[0] - count, pos[1] - count])
                    else:
                        if board[pos[0] - count][pos[1] - count].colour != colour:
                            possibleMoves.append([pos[0] - count, pos[1] - count])
                        searching1 = False
            if searching2:
                if pos[0] - count < 0 or pos[1] + count > 7:
                    searching2 = False
                else:
                    if board[pos[0] - count][pos[1] + count] == None:
                        possibleMoves.append([pos[0] - count, pos[1] + count])
                    else:
                        if board[pos[0] - count][pos[1] + count].colour != colour:
                            possibleMoves.append([pos[0] - count, pos[1] + count])
                        searching2 = False
            if searching3:
                if pos[0] + count > 7 or pos[1] + count > 7:
                    searching3 = False
                else:
                    if board[pos[0] + count][pos[1] + count] == None:
                        possibleMoves.append([pos[0] + count, pos[1] + count])
                    else:
                        if board[pos[0] + count][pos[1] + count].colour != colour:
                            possibleMoves.append([pos[0] + count, pos[1] + count])
                        searching3 = False
            if searching4:
                if pos[0] + count > 7 or pos[1] - count < 0:
                    searching4 = False
                else:
                    if board[pos[0] + count][pos[1] - count] == None:
                        possibleMoves.append([pos[0] + count, pos[1] - count])
                    else:
                        if board[pos[0] + count][pos[1] - count].colour != colour:
                            possibleMoves.append([pos[0] + count, pos[1] - count])
                        searching4 = False
            count += 1
    return possibleMoves

def getKingMoves(pos, board, colour, moveNo):
    possibleMoves = []
    allRelativeMoves = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

    if moveNo == 0:
        allRelativeMoves.append([0,-2])
    
    for relativeMove in allRelativeMoves:
        newProposedPos = [pos[0] + relativeMove[0], pos[1] + relativeMove[1]]
        if not(newProposedPos[0] < 0 or newProposedPos[0] > 7 or newProposedPos[1] < 0 or newProposedPos[1] > 7):
            if board[newProposedPos[0]][newProposedPos[1]] == None:
                possibleMoves.append(newProposedPos)
            else:
                if board[newProposedPos[0]][newProposedPos[1]].colour != colour:
                    possibleMoves.append(newProposedPos)
    allRelativeMoves = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]
    return possibleMoves

def checkAllMoves(board, colour):
    allMoves = []
    for line in board:
        for piece in line:
            if piece != None:
                if piece.colour != colour:
                    if type(Piece) == type(King):
                        pieceMoves = getKingMoves(piece.pos, board, piece.colour, piece.moveNo)
                    else:
                        pieceMoves = piece.getMoves(board)
                    if len(pieceMoves) != 0:
                        for move in pieceMoves:
                            allMoves.append(move)
    return allMoves