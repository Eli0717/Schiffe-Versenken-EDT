from numpy import *     # Für Matrix notwendig
board = array([[None] * 11] * 11)   # 11 x 11 Matrix
print(board)
for i in range(1,11):
    board[0][i] = i     # 1. Zeile und i-te Spalte wird mit i ersetzt

board[1][0] = "a"
board[2][0] = "b"
board[3][0] = "c"
board[4][0] = "d"
board[5][0] = "e"
board[6][0] = "f"
board[7][0] = "g"
board[8][0] = "h"
board[9][0] = "i"
board[10][0] = "j"
board[0][0] = ""
for i in range (1,11):
    for j in range (1,11):
        board[i][j] = "O"
        
# Ausgabe Zeile für Zeile mit Tabulatoren für bessere Lesbarkeit
for row in board:
    print("\t".join(map(str, row)))  # Alle Werte zu Strings machen und mit Tab trennen
