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
