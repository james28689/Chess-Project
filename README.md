# Python Chess Engine
A chess engine made entirely from scratch in Python.

Can be played using either the terminal by running main.py, or through a web browser on http://localhost:5000 by running app.py (requires Flask).

- Pieces are represented with an individual class for each piece. Their main role is to find possible moves for the piece, using the getMoves() function.
- Board contained within a BoardController class, which controls the moving of pieces and the displaying of the board.

##  Feature List:
- [x] Basic board creation.
- [x] Controll board with BoardController class.
- [x] Create Piece class and child classes for each piece type.
- [x] Piece Movement -
    - [x] Pawn
    - [x] Rook
    - [x] Bishop
    - [x] Knight
    - [x] Queen
    - [x] King
- [x] Logging -
    - [x] Create Logger class.
    - [x] Create log files with name of date and time.
    - [x] Store moves using standard algabraic notation (SAN).
- [x] Front End -
    - [x] Setup basic Flask app.
    - [x] Interface BoardController with Flask
    - [x] Create static HTML, JS, and CSS files.
    - [x] Allow fetch requests to Flask to call movePiece() and getMoves(). 
    - [x] Draw board with JS and p5.js
    - [x] Display pieces with p5.js
    - [x] Detect mouse clicks and show possible moves.
    - [x] Allow pieces to be moved on browser.
- [ ] Thoroughly check front end.
- [ ] 'Improve'/Implement the taking of pieces
- [ ] Add advanced rules -
    - [ ] Castling
    - [ ] En passant
- [ ] State analysis -
    - [x] Check for checkmate.
    - [ ] Check for stalemate.
- [ ] Integrate state analysis with front end.

## Known Errors:
- [x] Pawns can take own colour.
- [x] King piece can be taken.