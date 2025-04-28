
from board.game_board import *
from bot.bot_player import *
from board.setze_schiffe import *

def hat_schiffe(board):
    for zeile in board:
        for feld in zeile:
            if feld in SCHIFF_IDS:
                return True  # Es gibt noch mindestens ein Schiffsteil.
    return False  # Keine Schiffe mehr vorhanden.

# Funktion die die ganze Spielrunde steuert.
def fuehre_spielzuege_durch(board_spieler, board_bot, bot):
    Spiel = True 
    Spieler_am_Zug = True # Spieler beginnt mit dem ersten Zug.

    # Spiel läuft bis einer keine Schiffe mehr hat.
    while Spiel == True:
        zeige_board(board_spieler, verdeckt=False)
        if Spieler_am_Zug:  # Wenn der Spieler am Zug ist, passiert das.
            print("Spieler ist am Zug: ")
            zeige_board(board_bot, verdeckt=True)  # Zeigt das Bot-Board, aber die Schiffe sind verdeckt.

            # Ziel wird eingegeben und in Koordinaten umgewandelt.
            Zieleingabe = input("Gib deine Ziel-Koordinate ein (z.B. A5): ")
            x, y = dekodiere_koordinate(Zieleingabe)  # X = Zeile und Y = Spalte.

            # Überprüfen.
            if board_bot[x][y] in SCHIFF_IDS:  # Ja -> Treffer.
                print("Treffer!") 
                board_bot[x][y] = TREFFER
                Spieler_am_Zug = False
            elif board_bot[x][y] in [TREFFER, FEHLSCHUSS]:  # Schon abgeschossen -> Nichts.
                print("Feld bereits beschossen.")
            else:  # Nein -> Verfehlt.
                print("Verfehlt. :( ")
                board_bot[x][y] = FEHLSCHUSS
                Spieler_am_Zug = False

        else:  # Wenn der Bot am Zug ist, passiert das.
            print("Bot ist am Zug:")
            Schuss_Bot(board_spieler)  # Berechnet den Schuss.
            from bot.bot_player import schussposx, schussposy, boardtrackedshots
            x_b = schussposx
            y_b = schussposy

            # Getroffen?
            if board_spieler[x_b][y_b] in SCHIFF_IDS:  # Ja -> Treffer.
                print("Bot hat ein Treffer gemacht!")
                board_spieler[x_b][y_b] = TREFFER
                boardtrackedshots[x_b][y_b] = TREFFER  # Aktualisierung des Bot-Boards
                Spieler_am_Zug = True
            elif board_spieler[x_b][y_b] in [TREFFER, FEHLSCHUSS]:  # Feld schon beschossen -> Nichts.
                print("Bot hat versucht, ein Feld doppelt zu treffen.")
            else:  # Kein Treffer -> Verfehlt.
                print("Bot hat verfehlt.")
                board_spieler[x_b][y_b] = FEHLSCHUSS
                boardtrackedshots[x_b][y_b] = FEHLSCHUSS  # Aktualisierung des Bot-Boards
                Spieler_am_Zug = True

        # Hat der Spieler noch Schiffe und hat der Bot noch Schiffe, wenn nicht, dann hat einer der beiden gewonnen.
        if hat_schiffe(board_spieler) == False:
            print("Der Bot hat gewonnen!")
            Spiel = False 
        elif hat_schiffe(board_bot) == False:
            print("Du hast gewonnen!")
            Spiel = False

def main():
    global board_spieler, board_bot, boardtrackedshots
    board_spieler = initialisiere_board()
    board_bot = initialisiere_board()
    boardtrackedshots = initialisiere_board()  # Board zum Verfolgen der Bot-Schüsse

    zeige_board(board_spieler, verdeckt=False)
    
    setze_schiffe(board_spieler)
    setze_schiffe_durch_bot(board_bot)

    fuehre_spielzuege_durch(board_spieler, board_bot, Schuss_Bot)

main()
