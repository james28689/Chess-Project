url = "http://localhost:5000"

labelsX = ["a", "b", "c", "d", "e", "f", "g", "h"];
labelsY = ["1", "2", "3", "4", "5", "6", "7", "8"];

pieces = ["p", "r", "b", "n", "q", "k"]

whiteToPlay = true

pieceSelected = false
selected = ""

highlightedSquares = []

function move(move) {
    fetch(url + move)
    whiteToPlay.toggle()
}

function getMoves(piece) {
    fetch(url + "/getMove/" + piece)
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

            currentSquare = labelsX[x] + labelsY[7-y];
            if (highlightedSquares.includes(currentSquare)) {
                fill(0, 255, 0);
            }

            rect(x * width / 8, y * height / 8, width / 8, height / 8);
            count++;
        }
    }

    jsBoard = [];
    lines = board.split("/");
    for (i = 0; i <= 8; i++) {
        strline = lines[i].split(".");
        strline.pop();
        jsBoard.push(strline);
    }
    jsBoard.pop();

    print(jsBoard);

    for (y = 0; y <= 7; y++) {
        for(x = 0; x <= 7; x++) {
            if (jsBoard[y][x] != "--") {
                image(imgs[jsBoard[y][x]], width/8 * x, height/8 * y, width/8, height/8)
            }
        }
    }
}

function mouseClicked() {
    currentSquare = labelsX[Math.floor(mouseX/100)] + labelsY[7-Math.floor(mouseY/100)]
    
    if(!(pieceSelected)) {
        pieceSelected = true
        selected = currentSquare
        highlightedsquares = getMoves(selected)

    }
}

imgs = {}

function startup() {
    var eventSource = new EventSource("/stream")
    eventSource.onmessage = (e) => {
        board = e.data
        board = board.substring(1, board.length-1)

        drawBoard(imgs, board)
    }
}

function setup() {
    createCanvas(800, 800);
    
    for (i=0; i < pieces.length; i++) {
        imgs["w"+pieces[i]] = loadImage("/static/assets/w" + pieces[i] + ".png")
        imgs["b"+pieces[i]] = loadImage("/static/assets/b" + pieces[i] + ".png")
    }

}