from numpy import array, zeros     # Für Matrix notwendig
import random as r 
from board.game_board import *
from board.setze_schiffe import *


boardtrackedshots = initialisiere_board() # Board zum verfolgen eigener Schüsse.
boardprob = zeros((10, 10), dtype = int) # 10*10 Array, wo der Bot Wahrscheinlichkeiten speichert.

def setze_schiffe_durch_bot(board): # Schiffe werden gesetzt.
    for i in range(len(Schifflängen)): # Jede Länge wird durchgegangen.
        schifflänge = Schifflängen[i]
        schiff_id = SCHIFF_IDS[i]
        setze_nächstes_schiff(board, schifflänge, schiff_id) # Schiffslänge und Schiffs-ID werden der Funktion gegeben um jedes Schiff einzelnd zu setzen.

def setze_nächstes_schiff(board, schifflänge: int, schiff_id: str):
    isStartPosMöglich = False # Suche nach Position die geht.
    while not isStartPosMöglich:
        x, y = r.randint(0, 9), r.randint(0, 9)  # Zufällige auswahl von Koordinaten.

        # Von da werden alle Richtungen geprüft, ob man in die Richtung das Schiff setzten kann.
        # Wenn man es setzen kann, wird die Richtung bei möglichen Richtungen gemerkt.
        mögliche_richtungen = []
        if kann_schiff_gesetzt_werden(board, x, y, OBEN, schifflänge):
            mögliche_richtungen.append(OBEN)
        if kann_schiff_gesetzt_werden(board, x, y, RECHTS, schifflänge):
            mögliche_richtungen.append(RECHTS)
        if kann_schiff_gesetzt_werden(board, x, y, LINKS, schifflänge):
            mögliche_richtungen.append(LINKS)
        if kann_schiff_gesetzt_werden(board, x, y, UNTEN, schifflänge):
            mögliche_richtungen.append(UNTEN)

        if mögliche_richtungen: # Wen mögliche Richtungen existieren.
            isStartPosMöglich = True # Start ist möglich.

            # Zufällige Richtung und dann Platzierung des Schiffes.
            richtung = r.choice(mögliche_richtungen)
            setze_schiff_in_board(board, x, y, richtung, schifflänge, schiff_id)

# Variablen für den Schuss-Bot.
treffer_positionen = []  # Trefferpositionen sammeln, die bisher waren.
finden = True            # Ob der Bot suchen oder versenken soll.

# Koordinaten für den nächsten Schuss.
schussposx = 0
schussposy = 0

def finde_Schiff():
    global schussposx, schussposy, boardtrackedshots, boardprob, schussposx, schussposy

    boardprob.fill(0)  # Reset der Wahrscheinlichkeitstabelle

    # Für jede Schiffslänge wird bei jedem Feld nach Rechts und Unten geschaut, ob es passt.
    for schifflänge in Schifflängen:
        for i in range(10):
            for j in range(10):
                if boardtrackedshots[i][j] == WASSER:  # Nur Felder, die noch nicht beschossen wurden.
                    for richtung in [RECHTS, UNTEN]:
                        if kann_schiff_gesetzt_werden(boardtrackedshots, i, j, richtung, schifflänge):
                            # Wenn es passt wird die Wahrscheinlichkeit für das Schiff bei dem Feld erhöht.
                            for l in range(schifflänge):
                                if richtung == RECHTS and j + l < 10:
                                    if boardtrackedshots[i][j + l] == WASSER:
                                        boardprob[i][j + l] += 1
                                elif richtung == UNTEN and i + l < 10:
                                    if boardtrackedshots[i + l][j] == WASSER:
                                        boardprob[i + l][j] += 1

    # Auswählen des Feldes mit der höchsten Wahrscheinlichkeit, wen mehrere wird es zufällig gemacht.
    höchste_wahrscheinlichkeit = boardprob.max()
    kandidaten = [(i, j) for i in range(10) for j in range(10) if boardprob[i][j] == höchste_wahrscheinlichkeit and boardtrackedshots[i][j] == WASSER]

    if kandidaten:  # Wenn es Kandidaten gibt.
        schussposx, schussposy = r.choice(kandidaten)
        print(f"Bot schießt auf: {chr(65+schussposx)}{schussposy+1}")
    else:
        print("Es gibt keine gültigen Felder zum Abschießen.")



def senke_Schiff(board_spieler):
    global finden, treffer_positionen, boardtrackedshots, schussposx, schussposy

    if len(treffer_positionen) < 2:
        x, y = treffer_positionen[-1]
        richtungen = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        nachbarn = []  # Liste von möglichen Nachbarn
        for dx, dy in richtungen:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if boardtrackedshots[nx][ny] == WASSER:
                    nachbarn.append((nx, ny))

        if nachbarn:
            # Zufälliges unbeschossenes Nachbarfeld auswählen
            nx, ny = r.choice(nachbarn)
            print(f"Bot schießt auf: {chr(65+nx)}{ny+1}")

            if board_spieler[nx][ny] in SCHIFF_IDS:
                boardtrackedshots[nx][ny] = TREFFER
                treffer_positionen.append((nx, ny))
            else:
                boardtrackedshots[nx][ny] = FEHLSCHUSS
        else:
            # Keine Nachbarn mehr? Dann zurück ins Suchen
            finden = True
            treffer_positionen.clear()

    else:
        x1, y1 = treffer_positionen[0]
        x2, y2 = treffer_positionen[1]

        if x1 == x2:
            treffer_positionen.sort(key=lambda pos: pos[1])
            links = (x1, y1 - 1)
            rechts = (x2, y2 + 1)
            angrenzend = [links, rechts]
        else:
            treffer_positionen.sort(key=lambda pos: pos[0])
            oben = (x1 - 1, y1)
            unten = (x2 + 1, y2)
            angrenzend = [oben, unten]

        nachbarn = []
        for nx, ny in angrenzend:
            if 0 <= nx < 10 and 0 <= ny < 10:
                if boardtrackedshots[nx][ny] == WASSER:
                    nachbarn.append((nx, ny))

        if nachbarn:
            nx, ny = r.choice(nachbarn)
            print(f"Bot schießt auf: {chr(65+nx)}{ny+1}")

            if board_spieler[nx][ny] in SCHIFF_IDS:
                boardtrackedshots[nx][ny] = TREFFER
                treffer_positionen.append((nx, ny))
            else:
                boardtrackedshots[nx][ny] = FEHLSCHUSS
        else:
            # Schiff möglicherweise versenkt, neue Suche starten
            finden = True
            treffer_positionen.clear()

# Hauptfunktion, die entscheidet, ob man sucht oder versenkt.
def Schuss_Bot(board_spieler):
    global finden, treffer_positionen, schussposx, schussposy

    if finden: # Wen wir suchen müssen, wird die Wahrscheinlichkeit ausgerechnet.
        finde_Schiff()
        # Dann auf die ermittelte Position feuern.
        if board_spieler[schussposx][schussposy] in SCHIFF_IDS:
            boardtrackedshots[schussposx][schussposy] = TREFFER
            treffer_positionen.append((schussposx, schussposy))
            finden = False  # Wechsle in "Versenken"-Modus.
        else: # Bei Fehlschuss muss man weiter suchen.
            boardtrackedshots[schussposx][schussposy] = FEHLSCHUSS
    else: # Schon Treffer vorhanden, dann versuchen wir das Schiff zu versenken.
        senke_Schiff(board_spieler)