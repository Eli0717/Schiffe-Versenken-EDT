from numpy import *     # Für Matrix notwendig

# Symbole definieren.
WASSER = "🌊"
SCHIFF_IDS = ["1", "2", "3", "4", "5"]  # ID für jedes Schiff
TREFFER = "🔥"
FEHLSCHUSS = "❌"

# Erstellung eines 10 * 10 Feldes, mit Wasser gefüllt und durch "array" in eine Matrix umgewandelt.
def initialisiere_board():
    return array([[WASSER for _ in range (10)]for _ in range (10)])

def zeige_board(board, verdeckt):
    # Spalten werden nummerriert, von 1-10. "join" verbindet Zahlen mit Leerzeichen. "f"{i+1:2}" Sorgt dafür, das die Zahlen immer 2 Zeichen lang sind.
    print("   " + " ".join(f"{i+1:2}" for i in range(10)))
    # Es wird nun jede Zeile durchgegangen.
    for i, zeile in enumerate(board):
        # Jedes Feld wird einzelnd abgearbeitet.
        zeilenanzeige = []
        for feld in zeile:
            if feld in SCHIFF_IDS: # Wenn es ein Schiff ist.
                if verdeckt: # Wen es verdeckt werden soll, zeigt es nur Wasser an.
                    zeilenanzeige.append(WASSER)
                else: # Sonst Schiff.
                    zeilenanzeige.append("🚢")
            elif feld == TREFFER:  # Wenn es ein Treffer war.
                zeilenanzeige.append(TREFFER)
            elif feld == FEHLSCHUSS:  # Wenn es ein Fehlschuss war.
                zeilenanzeige.append(FEHLSCHUSS)
            else: # Es ist kein Schiff.
                zeilenanzeige.append(feld)
        # Die Zeilen werden gedruckt und mit Buchstaben benannt.
        print(f"{chr(65+i)}  " + " ".join(zeilenanzeige))