# pieces.py --- includes all class declarations for the various chess pieces
# TODO: - Clean up disgusting code in getMoves() for Pawn and Rook.

from typing import Set


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
        self.name = colour[0].lower() + "P"

    def getMoves(self, board):
        possibleMoves = []

        if self.colour == "black":
            try:
                if board[self.pos[0]+1][self.pos[1]] == None:
                    possibleMoves.append([self.pos[0]+1, self.pos[1]])
            except:
                pass
            try:
                if self.moveNo == 0:
                    if board[self.pos[0]+2][self.pos[1]] == None:
                        possibleMoves.append([self.pos[0]+2, self.pos[1]])
            except:
                pass
            try:
                if board[self.pos[0]+1][self.pos[1]+1] != None:
                    possibleMoves.append([self.pos[0]+1, self.pos[1]+1])
            except:
                pass
            try:
                if board[self.pos[0]+1][self.pos[1]-1] != None:
                    possibleMoves.append([self.pos[0]+1, self.pos[1]-1])
            except:
                pass
        else:
            try:
                if board[self.pos[0]-1][self.pos[1]] == None:
                    possibleMoves.append([self.pos[0]-1, self.pos[1]])
            except:
                pass
            try:
                if self.moveNo == 0:
                    if board[self.pos[0]-2][self.pos[1]] == None:
                        possibleMoves.append([self.pos[0]-2, self.pos[1]])
            except:
                pass
            try:
                if board[self.pos[0]-1][self.pos[1]+1] != None:
                    possibleMoves.append([self.pos[0]-1, self.pos[1]+1])
            except:
                pass
            try:
                if board[self.pos[0]-1][self.pos[1]-1] != None:
                    possibleMoves.append([self.pos[0]-1, self.pos[1]-1])
            except:
                pass

        return possibleMoves

class Rook(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "R"

    def getMoves(self, board):
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
                    if self.pos[0] - count < 0:
                        searching1 = False
                    else:
                        if board[self.pos[0] - count][self.pos[1]] == None:
                            possibleMoves.append([self.pos[0] - count, self.pos[1]])
                        else:
                            if board[self.pos[0] - count][self.pos[1]].colour != self.colour:
                                possibleMoves.append([self.pos[0] - count, self.pos[1]])
                            searching1 = False
                if searching2:
                    if self.pos[1] + count > 7:
                        searching2 = False
                    else:
                        if board[self.pos[0]][self.pos[1] + count] == None:
                            possibleMoves.append([self.pos[0], self.pos[1] + count])
                        else:
                            if board[self.pos[0]][self.pos[1] + count].colour != self.colour:
                                possibleMoves.append([self.pos[0], self.pos[1] + count])
                            searching2 = False
                if searching3:
                    if self.pos[0] + count > 7:
                        searching3 = False
                    else:
                        if board[self.pos[0] + count][self.pos[1]] == None:
                            possibleMoves.append([self.pos[0] + count, self.pos[1]])
                        else:
                            if board[self.pos[0] + count][self.pos[1]].colour != self.colour:
                                possibleMoves.append([self.pos[0] + count, self.pos[1]])
                            searching3 = False
                if searching4:
                    if self.pos[1] - count < 0:
                        searching4 = False
                    else:
                        if board[self.pos[0]][self.pos[1] - count] == None:
                            possibleMoves.append([self.pos[0], self.pos[1] - count])
                        else:
                            if board[self.pos[0]][self.pos[1] - count].colour != self.colour:
                                possibleMoves.append([self.pos[0], self.pos[1] - count])
                            searching4 = False
                count += 1
        return possibleMoves
                

class Bishop(Piece):
    def __init__(self, pos, colour):
        super().__init__(pos, colour)
        self.name = colour[0].lower() + "B"
    
    def getMoves(self, board):
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
                    if self.pos[0] - count < 0 or self.pos[1] - count < 0:
                        searching1 = False
                    else:
                        if board[self.pos[0] - count][self.pos[1] - count] == None:
                            possibleMoves.append([self.pos[0] - count, self.pos[1] - count])
                        else:
                            if board[self.pos[0] - count][self.pos[1] - count].colour != self.colour:
                                possibleMoves.append([self.pos[0] - count, self.pos[1] - count])
                            searching1 = False
                if searching2:
                    if self.pos[0] - count < 0 or self.pos[1] + count > 7:
                        searching2 = False
                    else:
                        if board[self.pos[0] - count][self.pos[1] + count] == None:
                            possibleMoves.append([self.pos[0] - count, self.pos[1] + count])
                        else:
                            if board[self.pos[0] - count][self.pos[1] + count].colour != self.colour:
                                possibleMoves.append([self.pos[0] - count, self.pos[1] + count])
                            searching2 = False
                if searching3:
                    if self.pos[0] + count > 7 or self.pos[1] + count > 7:
                        searching3 = False
                    else:
                        if board[self.pos[0] + count][self.pos[1] + count] == None:
                            possibleMoves.append([self.pos[0] + count, self.pos[1] + count])
                        else:
                            if board[self.pos[0] + count][self.pos[1] + count].colour != self.colour:
                                possibleMoves.append([self.pos[0] + count, self.pos[1] + count])
                            searching3 = False
                if searching4:
                    if self.pos[0] + count > 7 or self.pos[1] - count < 0:
                        searching4 = False
                    else:
                        if board[self.pos[0] + count][self.pos[1] - count] == None:
                            possibleMoves.append([self.pos[0] + count, self.pos[1] - count])
                        else:
                            if board[self.pos[0] + count][self.pos[1] - count].colour != self.colour:
                                possibleMoves.append([self.pos[0] + count, self.pos[1] - count])
                            searching4 = False
                count += 1
        print(possibleMoves)
        return possibleMoves
