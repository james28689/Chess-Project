from pieces import Piece
from moves import getPawnMoves, getRookMoves, getBishopMoves, getKnightMoves, getKingMoves, checkAllMoves

def analyseBoard(board):
    whiteCheckmate = findCheckmate(board, "white")
    blackCheckmate = findCheckmate(board, "black")

    stalemate = findStalemate(board)

    if whiteCheckmate:
        return "Checkmate - white wins!"
    if blackCheckmate:
        return "Checkmate - black wins!"
    if stalemate:
        return "Stalemate - draw"
    
    return "-"

def findCheckmate(board, colour):
    oppositeColour = "black" if colour == "white" else "white"

    king = Piece([0,0], colour)
    for rank in board:
        for piece in rank:
            if piece != None:
                if piece.getName()[1] == "k":
                    if piece.colour == oppositeColour:
                        king = piece
    allMoves = getMovesIncludingKing(board)
    if len(king.getMoves(board)) == 0 and king.pos in allMoves:
        return True
    else:
        return False

def findStalemate(board):
    if len(checkAllMoves(board, "white")) == 0:
        return True
    if len(checkAllMoves(board, "black")) == 0:
        return True
    return False

def getMovesIncludingKing(board):
    moves = []
    for rank in board:
        for piece in rank:
            if piece != None:
                type = piece.getName()[1]
                if type == "p":
                    moves.append(getPawnMoves(piece.pos, board, piece.colour, piece.moveNo))
                if type == "r":
                    moves.append(getRookMoves(piece.pos, board, piece.colour))
                if type == "b":
                    moves.append(getBishopMoves(piece.pos, board, piece.colour))
                if type == "n":
                    moves.append(getKnightMoves(piece.pos, board, piece.colour))
                if type == "q":
                    moves.append(getRookMoves(piece.pos, board, piece.colour) + getBishopMoves(piece.pos, board, piece.colour))
                if type == "k":
                    moves.append(getKingMoves(piece.pos, board, piece.colour, piece.moveNo))
    
    formattedMoves = []
    for moveList in moves:
        for move in moveList:
            formattedMoves.append(move)
    
    return formattedMoves