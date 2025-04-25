from numpy import *     # Für Matrix notwendig

WASSER = "🌊"
SCHIFF_IDS = ["1", "2", "3", "4", "5"]  # ID für jedes Schiff
# SCHIFF = "🚢"
TREFFER = "🔥"
FEHLSCHUSS = "❌"

board1 = array([[None] * 10] * 10)   # 10 x 10 Matrix
board2 = array([[None] * 10] * 10)   # 10 x 10 Matrix

def initialisiere_board():
    return array([[WASSER] * 10] * 10)

def zeige_board(board, verdeckt):
    # TODO: gibt das Board mit Rahmen und Zeilen- (A-J) und Spalten- (1-10) Bezeichungen aus
    # Wenn "verdeckt", dann sollen die Schiffe als Wasser gezeigt werden
    print(board)