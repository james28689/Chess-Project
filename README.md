### Python Chess Engine
A chess engine made entirely from scratch in Python.

- Pieces are represented with an individual class for each piece. Their main role is to find possible moves for the piece, using the getMoves() function.
- Board contained within a BoardController class, which controls the moving of pieces and the displaying of the board.

##  Feature List:
- [x] Basic board creation.
- [x] Piece Movement -
    - [x] Pawn
    - [x] Rook
    - [x] Bishop
    - [x] Knight
    - [x] Queen
    - [x] King
- [ ] Graphics with Pygame or p5.js
- [ ] State analysis -
    - [ ] Check for checkmate.
    - [ ] Check for stalemate.