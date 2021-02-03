# pieces.py --- includes all class declarations for the various chess pieces
# TODO: - Clean up disgusting code in getMoves() for Pawn and Rook.

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
        print(self.pos)
        # Along - right then left
        searching = True
        count = 1
        while searching:
            xPos = self.pos[1] + count
            if xPos > 7 or xPos < 0:
                searching = False
                break
            
            if board[self.pos[0]][xPos] == None:
                print("Found move: ", self.pos[0], xPos)
                possibleMoves.append([self.pos[0], xPos])
                count += 1
            else:
                if board[self.pos[0]][xPos].colour != self.colour:
                    possibleMoves.append([self.pos[0], xPos])
                searching = False
        print("Finished 1", possibleMoves)

        searching2 = True
        count2 = 1
        while searching2:
            xPos = self.pos[1] - count2
            if xPos > 7 or xPos < 0:
                searching2 = False
                break

            if board[self.pos[0]][xPos] == None:
                print("Found move: ", self.pos[0], xPos)
                possibleMoves.append([self.pos[0], xPos])
                count2 += 1
            else:
                if board[self.pos[0]][xPos].colour != self.colour:
                    possibleMoves.append([self.pos[0], xPos])
                searching2 = False
        print("Finished 2", possibleMoves)

        # Down - up then down
        searching3 = True
        count3 = 1
        while searching3:
            yPos = self.pos[0] - count3
            if yPos > 7 or yPos < 0:
                searching3 = False
                break
            
            if board[yPos][self.pos[1]] == None:
                print("Found move: ", yPos, self.pos[1])
                possibleMoves.append([yPos, self.pos[1]])
                count3 += 1
            else:
                if board[yPos][self.pos[1]].colour != self.colour:
                    possibleMoves.append([yPos, self.pos[1]])
                searching3 = False
        print("Finished 3", possibleMoves)

        searching4 = True
        count4 = 1
        while searching4:
            yPos = self.pos[1] - count4
            if yPos > 7 or yPos < 0:
                searching4 = False
                break

            if board[yPos][self.pos[1]] == None:
                print("Found move: ", yPos, self.pos[1])
                possibleMoves.append([yPos, self.pos[1]])
                count4 += 1
            else:
                if board[yPos][self.pos[1]].colour != self.colour:
                    possibleMoves.append([yPos, self.pos[1]])
                searching4 = False
        print("Finished 4", possibleMoves)
        
        return possibleMoves