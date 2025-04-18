# Programm-Ablauf
# 1. Beide Boerds leer initialisieren
# 2. Schiffe plazieren
# 3. Bot: Schiffe plazieren
# 4. Boards anzeigen
# 5. Spielen
# 5.1 Schießen
# 5.2 Schuss auswerten
# 5.3 Boards aktualisieren
# 5.4 Spielende feststellen
from board.game_board import *
from board.ship import *

def main():
    board1 = initialisiere_board()
    board2 = initialisiere_board()
    zeige_board(board1, True)
    setze_schiffe(board1)

    #setze_schiffe_durch_bot(board2)
    #fuehre_spielzuege_durch(board1, board2)

main()