def getPawnMoves(pos, board, colour, moveNo):
    possibleMoves = []

    standard = [-1,0]
    ifOccupied = [[-1,-1], [-1,1]]
    ifFirst = [-2,0]
    if colour == "black":
        standard[0] *= -1
        ifOccupied[0][0] *= -1
        ifOccupied[1][0] *= -1
        ifFirst[0] *= -1

    if pos[0] + standard[0] <= 7:
        if board[pos[0] + standard[0]][pos[1]] == None:
            possibleMoves.append([pos[0] + standard[0], pos[1]])
    
    for move in ifOccupied:
        proposedMove = [pos[0] + move[0], pos[1] + move[1]]
        if proposedMove[0] <= 7 and proposedMove[0] >= 0 and proposedMove[1] <= 7 and proposedMove[1] >= 0:
            if board[proposedMove[0]][proposedMove[1]] != None:
                if board[proposedMove[0]][proposedMove[1]].colour != colour:
                    possibleMoves.append(proposedMove)
    
    if moveNo == 0:
        possibleMoves.append([pos[0] + ifFirst[0], pos[1] + ifFirst[1]])
    
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

def getKnightMoves(pos, board, colour):
    possibleMoves = []
    allRelativeMoves = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1, -2], [-1, -2], [-2, -1]]

    for relativeMove in allRelativeMoves:
        newProposedPos = [pos[0] + relativeMove[0], pos[1] + relativeMove[1]]
        if not(newProposedPos[0] < 0 or newProposedPos[0] > 7 or newProposedPos[1] < 0 or newProposedPos[1] > 7):
            if board[newProposedPos[0]][newProposedPos[1]] == None:
                possibleMoves.append(newProposedPos)
            else:
                if board[newProposedPos[0]][newProposedPos[1]].colour != colour:
                    possibleMoves.append(newProposedPos)
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
                    if piece.getName()[1] == "k":
                        pieceMoves = getKingMoves(piece.pos, board, piece.colour, piece.moveNo)
                    else:
                        pieceMoves = piece.getMoves(board)
                    if len(pieceMoves) != 0:
                        for move in pieceMoves:
                            allMoves.append(move)
    return allMoves

def removeKingTake(board, colour, moves):
    position = []
    for rank in board:
        for piece in rank:
            if piece != None:
                if piece.getName()[1] == "k":
                    if piece.colour != colour:
                        position = piece.pos
    
    if position in moves:
        moves.remove(position)
    return moves