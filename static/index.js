url = "http://0.0.0.0:5000";

labelsX = ["a", "b", "c", "d", "e", "f", "g", "h"];
labelsY = ["1", "2", "3", "4", "5", "6", "7", "8"];

pieces = ["p", "r", "b", "n", "q", "k"];

player = "white";

pieceSelected = false;
selected = "";

jsBoard = [];
highlightedSquares = [];
yellowHighlightSquare = "";

function move(move) {
    fetch(url + "/move/" + move)
        .then(response => response.text())
        .then((response) => {
            if (response != "Done.") {
                alert(response);
            }
        })
    player = player === "white" ? "black" : "white";
}

function getMoves(piece) {
    possibleMoves = [];
    fetch(url + "/getMoves/" + piece)
        .then(response => response.json())
        .then(data => {
            for (i = 0; i < data.length; i++) {
                possibleMoves.push(data[i])
            }
        });
        return possibleMoves
}

function drawBoard(imgs, board) {
    clear();

    count = 0;
    for (y = 0; y <= 8; y++) {
        for (x = 0; x <= 8; x++) {
            if (count % 2 == 0) {
                fill(255);
            } else {
                fill(167);
            }

            currentSquareFilling = labelsX[x] + labelsY[7-y];
            if (highlightedSquares.includes(currentSquareFilling)) {
                fill(0, 255, 0);
            }
            if (currentSquareFilling == yellowHighlightSquare) {
                fill(255, 255, 0);
            }

            rect(x * width / 8, y * height / 8, width / 8, height / 8);
            count++;
        }
    }

    for (y = 0; y <= 7; y++) {
        for(x = 0; x <= 7; x++) {
            if (board[y][x] != "--") {
                image(imgs[board[y][x]], width/8 * x, height/8 * y, width/8, height/8)
            }
        }
    }
}

function resetBoard() {
    fetch(url + "/reset");
    yellowHighlightSquare = "";
    highlightedSquares = [];
    player = "white";
    drawBoard();
}

function mouseClicked() {
    currentSquare = labelsX[Math.floor(mouseX/100)] + labelsY[7-Math.floor(mouseY/100)]
    currentSquareIndex = [8-parseInt(currentSquare[1]), labelsX.indexOf(currentSquare[0])]
    print(currentSquareIndex)
    
    if(!(pieceSelected)) {
        if (jsBoard[currentSquareIndex[0]][currentSquareIndex[1]] != "--") {
            if (jsBoard[currentSquareIndex[0]][currentSquareIndex[1]][0] === player[0]) {
                selected = currentSquare;
                yellowHighlightSquare = currentSquare;
                possibleMoves = getMoves(selected);
                highlightedSquares = possibleMoves;
                pieceSelected = true
            }
        }
    } else {
        if (highlightedSquares.includes(currentSquare)) {
            print("Attempting move...")
            move(`${selected}${currentSquare}`);
            selected = "";
            pieceSelected = false;
            highlightedSquares = [];
            yellowHighlightSquare = "";
            // drawBoard(imgs, jsBoard);
        } else {
            if (jsBoard[currentSquareIndex[0]][currentSquareIndex[1]][0] === player[0]) {
                selected = currentSquare;
                possibleMoves = getMoves(selected);
                highlightedSquares = possibleMoves;
                yellowHighlightSquare = currentSquare;
            }
        }
    }
}

imgs = {}

function startup() {
    var eventSource = new EventSource(`${url}/stream`)
    eventSource.onmessage = (e) => {
        board = e.data
        board = board.substring(1, board.length-1)
        
        jsBoard = [];
        lines = board.split("/");
        for (i = 0; i <= 8; i++) {
            strline = lines[i].split(".");
            strline.pop();
            jsBoard.push(strline);
        }
        jsBoard.pop();

        drawBoard(imgs, jsBoard)
    }
}

function setup() {
    createCanvas(800, 800);
    
    for (i=0; i < pieces.length; i++) {
        imgs["w"+pieces[i]] = loadImage("/static/assets/w" + pieces[i] + ".png")
        imgs["b"+pieces[i]] = loadImage("/static/assets/b" + pieces[i] + ".png")
    }

}