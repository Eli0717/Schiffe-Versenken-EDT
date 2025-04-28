# Importiert alle Funktionen und Konstanten aus dem Modul game_board
from board.game_board import *

# Definition von Richtungen als Konstanten
OBEN = 1
RECHTS = 2
LINKS = 3
UNTEN = 4

# Liste der Schiffslängen, die gesetzt werden sollen
Schifflängen = [5,4,3,3,2]

# Funktion, um alle Schiffe auf dem Spielfeld zu platzieren
def setze_schiffe(board):
    for i in range(len(Schifflängen)):  # Gehe durch alle Schiffslängen
        schifflänge = Schifflängen[i]    # Hole aktuelle Schiffslänge
        schiff_id = SCHIFF_IDS[i]        # Hole die zugehörige Schiff-ID
        setze_nächstes_schiff(board, schifflänge, schiff_id)  # Setze das Schiff auf dem Board

# Funktion, um ein einzelnes Schiff zu setzen
def setze_nächstes_schiff(board, schifflänge: int, schiff_id: str):
    isStartPosMöglich = False  # Flag, ob Startposition möglich ist
    while not isStartPosMöglich:  # Wiederholen bis eine gültige Startposition gefunden ist
        koordinate = input("Nenne deine Koordinate für das Schiff mit der Länge " + str(schifflänge) + ": ")
        
        x,y = dekodiere_koordinate(koordinate)  # Umwandeln der Eingabe in Koordinaten
        
        # Prüfen, ob das Schiff in den vier Richtungen gesetzt werden kann
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

        # Falls eine Position gefunden wurde, Richtung auswählen
        if isStartPosMöglich:
            richtung = lese_int(1, 4, "In welche Richtung soll das Schiff zeigen? ")
        else:
            print("Hier kann kein Schiff platziert werden.")  # Fehlermeldung falls ungültig

    # Setzt das Schiff auf dem Board in die gewählte Richtung
    setze_schiff_in_board(board, x, y, richtung, schifflänge, schiff_id)
    zeige_board(board, False)  # Zeigt das aktuelle Board an

# Funktion, um zu überprüfen, ob ein Schiff auf dem Board platziert werden kann
def kann_schiff_gesetzt_werden(board, x : int, y : int, richtung, schifflänge : int) -> bool:
    # Überprüfen, ob die Startkoordinate innerhalb des Spielfelds liegt
    if x > 9 or x < 0 or y > 9 or y < 0:
        return False
    
    # Überprüfen der Richtung LINKS
    if richtung == LINKS:
        endpunkty = y - (schifflänge - 1)  # Endpunkt der Platzierung
        if endpunkty < 0:
            return False
        for i in range(schifflänge):
            if board[x][y-i] != WASSER:  # Überprüfen, ob die Felder frei sind
                return False
    
    # Überprüfen der Richtung UNTEN
    elif richtung == UNTEN:
        endpunktx = x + schifflänge - 1
        if endpunktx > 9:
            return False
        for i in range(schifflänge):
            if board[x+i][y] != WASSER:
                return False
    
    # Überprüfen der Richtung RECHTS
    elif richtung == RECHTS:
        endpunkty = y + schifflänge - 1
        if endpunkty > 9:
            return False
        for i in range(schifflänge):
            if board[x][y+i] != WASSER:
                return False
    
    # Überprüfen der Richtung OBEN
    elif richtung == OBEN:
        endpunktx = x - (schifflänge - 1)
        if endpunktx < 0:
            return False
        for i in range(schifflänge):
            if board[x-i][y] != WASSER:
                return False
    
    return True  # Falls alle Prüfungen bestanden sind, kann das Schiff gesetzt werden

# Funktion, die das Schiff endgültig auf dem Board platziert
def setze_schiff_in_board(board, x : int, y : int, richtung: int, schifflänge : int, schiff_id: str):
    # Je nach Richtung wird das Schiff entsprechend in das Board eingetragen
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

# Funktion zur Umwandlung der Benutzerkoordinate (z.B. "A1") in x- und y-Werte
def dekodiere_koordinate(koordinatenString):
    x = koordinatenString[0]           # Buchstabe für die Zeile
    y = koordinatenString[1:3]         # Zahl für die Spalte
    y = int(y)
    y = y-1                            # Spaltennummerierung anpassen (0-basiert)
    x = x.upper()                      # Buchstabe in Großbuchstabe umwandeln

    # Buchstabe in Zahl umwandeln (A=0, B=1, ..., J=9)
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
        x = -1  # Ungültige Eingabe

    x = int(x)
    y = int(y)
    return x,y  # Rückgabe der umgewandelten Koordinaten

# Funktion zum Einlesen einer Ganzzahl innerhalb eines erlaubten Bereichs
def lese_int(erlaubterMinWert: int, erlaubterMaxWert: int, aufforderungsText: str) -> int:
    while True:  # Solange wiederholen bis gültige Eingabe erfolgt
        eingabe = input(aufforderungsText)
        try:
            wert = int(eingabe)  # Versuche, die Eingabe in eine Zahl zu verwandeln
            if erlaubterMinWert <= wert and wert <= erlaubterMaxWert:
                return wert  # Rückgabe der gültigen Zahl
            else:
                print("Bitte eine Zahl zwischen " + str(erlaubterMinWert) + " und " + str(erlaubterMaxWert) + " eingeben.")
        except ValueError:
            print("Das war keine gültige Zahl.")  # Fehlermeldung bei ungültiger Eingabe