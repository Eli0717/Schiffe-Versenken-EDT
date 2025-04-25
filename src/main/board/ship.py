from board.game_board import *

OBEN = 1
RECHTS = 2
LINKS = 3
UNTEN = 4

Schifflängen = [5,4,3,3,2]

def setze_schiffe(board):
    for i in range(len(Schifflängen)):
        schifflänge = Schifflängen[i]
        schiff_id = SCHIFF_IDS[i]
        setze_nächstes_schiff(board, schifflänge, schiff_id)

def setze_nächstes_schiff(board, schifflänge: int, schiff_id: str):

    isStartPosMöglich = False
    while not isStartPosMöglich:
        koordinate = input("Nenne deine Koordinate für das Schiff mit der Länge " + str(schifflänge) + ": ")

        x,y = dekodiere_koordinate(koordinate)

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
            richtung = lese_int(1, 4, "In welche Richtung soll das Schiff zeigen? ")
        else:
            print("Hier kann kein Schiff platziert werden.")

    setze_schiff_in_board(board, x, y, richtung, schifflänge, schiff_id)
    zeige_board(board, False)

def kann_schiff_gesetzt_werden(board, x : int, y : int, richtung, schifflänge : int) -> bool:
    if x > 9 or x < 0 or y > 9 or y < 0:
        return False
    if richtung == LINKS:
        endpunkty = y - (schifflänge - 1)
        if endpunkty < 0:
            return False
        for i in range(schifflänge):
            if board[x][y-i] != WASSER:
                return False
    elif richtung == UNTEN:
        endpunktx = x + schifflänge - 1
        if endpunktx > 9:
            return False
        for i in range(schifflänge):
            if board[x+i][y] != WASSER:
                return False
    elif richtung == RECHTS:
        endpunkty = y + schifflänge - 1
        if endpunkty > 9:
            return False
        for i in range(schifflänge):
            if board[x][y+1] != WASSER:
                return False
    elif richtung == OBEN:
        endpunktx = x - (schifflänge - 1)
        if endpunktx < 0:
            return False
        for i in range(schifflänge):
            if board[x-i][y] != WASSER:
                return False
    return True

def setze_schiff_in_board(board, x : int, y : int, richtung: int, schifflänge : int, schiff_id: str):
    if richtung == LINKS:
        for i in range(schifflänge):
            board[x][y-i] = schiff_id
    elif richtung == UNTEN:
        for i in range(schifflänge):
            board[x+i][y] = schiff_id
    elif richtung == RECHTS:
        for i in range(schifflänge):
            board[x][y+i] = schiff_id
    elif richtung == OBEN:
        for i in range(schifflänge):
            board[x-i][y] = schiff_id



def dekodiere_koordinate(koordinatenString):
    x = koordinatenString[0]
    y = koordinatenString[1:3]
    y = int(y)
    y = y-1
    x = x.upper()

    if x == "A":
        x = 0
    elif x == "B":
        x = 1
    elif x == "C":
        x = 2
    elif x == "D":
        x = 3
    elif x == "E":
        x = 4
    elif x == "F":
        x = 5
    elif x == "G":
        x = 6
    elif x == "H":
        x = 7
    elif x == "I":
        x = 8
    elif x == "J":
        x = 9
    else:
        x = -1

    x = int(x)
    y = int(y)
    return x,y


def lese_int(erlaubterMinWert: int, erlaubterMaxWert: int, aufforderungsText: str) -> int:
    while True:
        eingabe = input(aufforderungsText)
        try:
            wert = int(eingabe)
            if erlaubterMinWert <= wert and wert <= erlaubterMaxWert:
                return wert
            else:
                print("Bitte eine Zahl zwischen " + erlaubterMinWert + " und " + erlaubterMaxWert + "eingeben.")
        except ValueError:
            print("Das war keine gültige Zahl.")

