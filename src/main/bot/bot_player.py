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
    
boardtrackedshots = array([[WASSER for _ in range(10)] for _ in range(10)])   # 10 x 10 Matrix
def finde_schuss():                                                           # auf Warscheinlichkeit basiertes "guessen"
    boardprob = array([[0 for _ in range(10)] for _ in range(10)])
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
    zwischenvariable = 0
    endergebnissx = 0
    endergebnissy = 0

    for x in range (10):
        for y in range (10):
            if boardprob[x][y] > zwischenvariable:
                endergebnissx = y + 1
                endergebnissy = x + 1
                zwischenvariable = boardprob[x][y]
    
    print(endergebnissx,endergebnissy)                            #GUESS
    boardtrackedshots[endergebnissx][endergebnissy] = FEHLSCHUSS

def senke_Schiff():    # falls treffer gefallen ist, suche den rest vom Schiff und senke ihn
    print (0)
    # in bearbeitung

finden = True
def Schuss():        # fassenwechsel zwischen suchen und senken
    if finden == True:
        finde_Schiff()
    else:
        senke_Schiff()

    #Muss wissen ob wir grade getroffen haben, wenn ja dann senke_Schiff, wenn nein dann finde_Schiff

