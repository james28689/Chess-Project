from flask import Flask, Response
import json, time
from board import BoardController
from my_logging import Logger
from state_analysis import analyseBoard

app = Flask(__name__, static_url_path="/static")

boardController = BoardController()
logger = Logger()
turn = 0
whiteToPlay = True

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/getMoves/<piece>")
def getMoveForPiece(piece):
    labelsX = "abcdefgh"
    x = labelsX.index(piece[0])
    y = 8 - int(piece[1])
    moves = boardController.board[y][x].getMoves(boardController.board)
    movesAsStrings = []
    for move in moves:
        moveX = labelsX[move[1]]
        moveY = str(8 - move[0])
        movesAsStrings.append(f"{moveX}{moveY}")
    return json.dumps(movesAsStrings)

@app.route("/move/<move>")
def move(move):
    global whiteToPlay
    global turn

    formattedMove = move[0:2] + " " + move[2:4]
    if boardController.movePiece(formattedMove, whiteToPlay):
            if whiteToPlay:
                turn += 1
            logger.addLine(formattedMove, boardController.board, turn)
            whiteToPlay = not whiteToPlay
    
    analysis = analyseBoard(boardController.board)
    if analysis != "-":
        return analysis

    return "Done."

@app.route("/reset")
def reset():
    global whiteToPlay
    boardController.setBoard()
    whiteToPlay = True
    logger = Logger()
    return "Board reset."

def get_message():
    s = boardController.getBoard()
    time.sleep(0.2)
    return json.dumps(s)

@app.route("/stream")
def stream():
    def eventStream():
        while True:
            yield f"data: {get_message()}\n\n"
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()
