from numpy import *     # Für Matrix notwendig
import random as r 
from board.game_board import *
from board.ship import *
def setze_schiffe_durch_bot(board)
    def setze_nächstes_schiff(board, schifflänge: int): # definiert setze nächstes Schiff neu, um mit zufallsvariablen zu arbeiten
    
        isStartPosMöglich = False
        while not isStartPosMöglich:
            x,y = r.randint(1,10), r.randint(1,10) # zufällige position
    
            if kann_schiff_gesetzt_werden(board, x, y, OBEN, schifflänge):
                isStartPosMöglich = True
                print(str(OBEN) + ": OBEN")
            if kann_schiff_gesetzt_werden(board, x, y, RECHTS, schifflänge):
                isStartPosMöglich = True
                print(str(RECHTS) + ": RECHTS")
            if kann_schiff_gesetzt_werden(board, x, y, LINKS, schifflänge):
                isStartPosMöglich = True
                print(str(LINKS) + ": LINKS")
            if kann_schiff_gesetzt_werden(board, x, y, UNTEN, schifflänge):
                isStartPosMöglich = True
                print(str(UNTEN) + ": UNTEN")
    
            if isStartPosMöglich:
                richtung = random.choice([  
                    richtung for richtung in [OBEN, RECHTS, LINKS, UNTEN]
                    if kann_schiff_gesetzt_werden(board, x, y, richtung, schifflänge)
                ])    # zufällige auswahl der möglichen richtungen
    
            else:
                print("Hier kann kein Schiff platziert werden.")
    
        setze_schiff_in_board(board, x, y, richtung, schifflänge)
        zeige_board(board, False)


def wo_kann_ein_Schiff_hin(board, x : int, y : int, richtung, schifflänge : int) -> bool:
    if x > 9 or x < 0 or y > 9 or y < 0:
        return False
    if richtung == LINKS:
        endpunkty = y - (schifflänge - 1)
        if endpunkty < 0:
            return False
        for i in range(schifflänge):
            if board[x][y-i] == TREFFER:
                return False
            if board[x][y-i] == FEHLSCHUSS:
                return False
    elif richtung == UNTEN:
        endpunktx = x + schifflänge - 1
        if endpunktx > 9:
            return False
        for i in range(schifflänge):
            if board[x+i][y] == TREFFER:
                return False
            if board[x+i][y] == FEHLSCHUSS:
                return False
    elif richtung == RECHTS:
        endpunkty = y + schifflänge - 1
        if endpunkty > 9:
            return False
        for i in range(schifflänge):
            if board[x][y+i] == TREFFER:
                return False
            if board[x][y+i] == FEHLSCHUSS:
                return False
    elif richtung == OBEN:
        endpunktx = x - (schifflänge - 1)
        if endpunktx < 0:
            return False
        for i in range(schifflänge):
            if board[x-i][y] == TREFFER:
                return False
            if board[x-i][y] == FEHLSCHUSS:
                return False
    return True


def finde_Schiff():
    global schussposx, schussposy
    for schifflänge in Schifflängen:   # alle Längen 
        for i in range (10):         # alle in x Richtung
            for j in range (10):     # alle in y Richtung
                for k in range (2):  # alle Richtungen
                    if k == 0:
                        richtung = UNTEN
                    if k == 1:
                        richtung = RECHTS

                    
                    if wo_kann_ein_Schiff_hin(boardtrackedshots, i, j, richtung, schifflänge):
                        for l in range(schifflänge):
                            if richtung == RECHTS:
                                boardprob[i][j + l] += 1
                            elif richtung == UNTEN:
                                boardprob[i + l][j] += 1
                            elif richtung == LINKS:
                                boardprob[i][j - l] += 1
                            elif richtung == OBEN:
                                boardprob[i - l][j] += 1


    zwischenvariabl = 0
    zwischenvarpositionen = []
    endergebnissx = 0
    endergebnissy = 0

    for x in range (10):
        for y in range (10):
            if boardprob[x][y] > zwischenvariabl:
                zwischenvariabl = boardprob[x][y]
                zwischenvarpositionen.clear()
                zwischenvarpositionen.append((x,y))
            elif boardprob[x][y] == zwischenvariabl:
                zwischenvarpositionen.append((x,y))

    auswahl = r.choice(zwischenvarpositionen)
    endergebnissx, endergebnissy = auswahl
    print (zwischenvarpositionen)
    print(endergebnissx,endergebnissy)
    schussposx = endergebnissx
    schussposy = endergebnissy

    


treffer_position = []  # Globale Variable, merken wo der Treffer war
finden = True            # Ob der Bot suchen oder versenken soll

def senke_Schiff():
    global finden, treffer_positionen

    # Wenn weniger als 2 Treffer: normal angrenzende Felder probieren
    if len(treffer_positionen) < 2:
        x, y = treffer_positionen[-1]
        richtungen = [(-1,0), (0,1), (1,0), (0,-1)]  # (dx, dy)
        
        for dx, dy in richtungen:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if boardtrackedshots[nx][ny] == WASSER:
                    print(f"Schieße auf {nx}, {ny}")
                    if board2[nx][ny] == SCHIFF:
                        boardtrackedshots[nx][ny] = TREFFER
                        treffer_positionen.append((nx, ny))
                    else:
                        boardtrackedshots[nx][ny] = FEHLSCHUSS
                    return
    else:
        # Mehrere Treffer: Richtung bestimmen
        x1, y1 = treffer_positionen[0]
        x2, y2 = treffer_positionen[1]

        if x1 == x2:
            # Schiff liegt horizontal → gleiche Zeile
            treffer_positionen.sort(key=lambda pos: pos[1])  # sortiere nach y
            links = (treffer_positionen[0][0], treffer_positionen[0][1] - 1)
            rechts = (treffer_positionen[-1][0], treffer_positionen[-1][1] + 1)
            
            for nx, ny in [links, rechts]:
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if boardtrackedshots[nx][ny] == WASSER:
                        print(f"Schieße auf {nx}, {ny}")
                        if board2[nx][ny] == SCHIFF:
                            boardtrackedshots[nx][ny] = TREFFER
                            treffer_positionen.append((nx, ny))
                        else:
                            boardtrackedshots[nx][ny] = FEHLSCHUSS
                        return
        else:
            # Schiff liegt vertikal → gleiche Spalte
            treffer_positionen.sort(key=lambda pos: pos[0])  # sortiere nach x
            oben = (treffer_positionen[0][0] - 1, treffer_positionen[0][1])
            unten = (treffer_positionen[-1][0] + 1, treffer_positionen[-1][1])
            
            for nx, ny in [oben, unten]:
                if 0 <= nx < 10 and 0 <= ny < 10:
                    if boardtrackedshots[nx][ny] == WASSER:
                        print(f"Schieße auf {nx}, {ny}")
                        if board2[nx][ny] == SCHIFF:
                            boardtrackedshots[nx][ny] = TREFFER
                            treffer_positionen.append((nx, ny))
                        else:
                            boardtrackedshots[nx][ny] = FEHLSCHUSS
                        return
    
    # Wenn keine Felder mehr offen sind: Schiff fertig
    finden = True
    treffer_positionen.clear()


def Schuss_Bot():
    global finden, treffer_positionen, schussposx, schussposy 
    if finden:
        finde_Schiff()
        if board2[schussposx][schussposy] == SCHIFF:
            boardtrackedshots[schussposx][schussposy] = TREFFER
            finden = False
            treffer_positionen = [(schussposx, schussposy)]
        else:
            boardtrackedshots[schussposx][schussposy] = FEHLSCHUSS
    else:
        senke_Schiff()
