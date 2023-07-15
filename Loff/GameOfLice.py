## Game life Unterricht

#*****************************************************************************************# Game of Life
# 5.5_AB_GameOfLife_05_HSS_E1FI_LO_Loesung
#
# Aufbau: Matrix von Kästchen die leer("tot") oder voll("lebt") sind
# 
# Regeln:
# 1) Der nächster Status eines Feldes ist von seinem aktuellen Status
# und dem der 8 Nachbarfelder abhängig
# 2) Wenn ein Feld tot (leer) ist und 3 lebende_Nachbarn hat
#    dann wird es geboren (lebt wieder)
# 3) Wenn ein Feld lebt und lebende_Nachbarn < 2
#    dann stirbt das Feld (dann leer)
# 4) wenn ein Feld lebt und lebende_Nachbarn = 2 oder 3
#    dann bleibt es leben
# 5) Wenn ein Feld lebt und lebende_Nachbarn > 3
#    dann stirbt das Feld (dann leer)
# 6) zu beachten: am Rand gibt es weniger Nachbarn!
#
# oder anders ausgedrückt("Life-2333"):
# * lebende Zelle stirbt <=> lebende_Nachbarn < 2 or lebende_Nachbarn > 3
# * tote Zelle lebt wieder <=> lebende_Nachbarn == 3 (mindestens 3 und maximal 3)
#
# Programmentwurf:
# i) Die Felder werden in einer geschachtelten Liste verwaltet
#     [[<erste Reihe>][<zweite Reihe>]...]
#     Jede Reihe ist eine Liste von Spaltenwerten.
# ii) Ob ein Feld lebt ist ein boolean Wert (True/False)
# iiia) Ausgabe erstmal mit print,
# iiib) Ausgabe später mit X auf Turtle.Screen (hübscher/beeindruckender anzuschauen)  
#
#*****************************************************************************************
 
from random import randint
import time
 
size = 5
current_Spielfeld = []
 
# erzeuge "Spielfeld"
def erzeuge_Anfangs_Spielfeld():
    
  for row in range(size):
      new_row = []
      for column in range(size):
        """ ausgedachtes Muster eingeben
        if row == 1 or (row == 2 and (column == 0 or column == 1)):
            new_row.append(True)
        else:
            new_row.append(False)
        """
        # Zufallswerte machen das Spiel interessanter
        if randint(0,1) == 1:
            new_row.append(True)
        else:
            new_row.append(False)
 
      current_Spielfeld.append(new_row)
      
 
def zeige_current_Spielfeld():
 
    #erstmal print statt turtle
    for row in range(size):
        zeile = ""
        for column in range(size):
            lebt = True
            lebt = current_Spielfeld[row][column]
            if lebt:
                 zeile = zeile + "X"
            else:
                zeile = zeile + "." # Punkt sieht man besser als Leerzeichen
        print(zeile)
 
 
def ermittle_next_Spielfeld():
    
    next_Spielfeld = []
    
    for row in range(size):
        new_row = []
        for column in range(size):
            lebende_Nachbarn = ermittle_lebende_nachbarn(row, column)
            current_Feld = current_Spielfeld[row][column]
            # print(f"curr/lebende nachbarn = {current_Feld}/{lebende_Nachbarn}")
            if current_Feld == False and lebende_Nachbarn == 3:
                new_row.append(True)
            elif current_Feld == True and lebende_Nachbarn < 2:
                new_row.append(False)
            elif current_Feld == True and (lebende_Nachbarn == 2 or lebende_Nachbarn == 3):
                new_row.append(True)
            elif current_Feld == True and lebende_Nachbarn > 3:
                new_row.append(False)
            else:
                # Tote mit weniger oder mehr als 3 Nachbarn bleiben tot
                new_row.append(False)
 
        # Ende der Bearbeitung der Spalten der Zeile row
        next_Spielfeld.append(new_row)
        
    return(next_Spielfeld)
    
 
def ermittle_lebende_nachbarn(row, column):
    # ...machen wir später für current_Spielfeld
    
    rc = 0 # der Rückgabewert (return code) wird of mit rc definiert
    """ hier sind 2 Lösungsvarianten, Sie sollten beide verstehen
    Variante 1
    """
    if row == 0: # erste Zeile
        if column == 0: # Ecke links oben
            # prüfe alle 3 Nachbarn
            if current_Spielfeld[row-1][column]: rc = rc + 1
            if current_Spielfeld[row][column+1]: rc = rc + 1
            if current_Spielfeld[row-1][column+1]: rc = rc + 1
            
        elif column == size-1: # Ecke rechts oben
            # prüfe alle 3 Nachbarn
            if current_Spielfeld[row+1][column]: rc = rc + 1
            if current_Spielfeld[row][column-1]: rc = rc + 1
            if current_Spielfeld[row+1][column-1]: rc = rc + 1
            
        else: # oberer Rand ohne Ecken
            # prüfe alle 5 Nachbarn
            if current_Spielfeld[row][column-1]: rc = rc + 1
            if current_Spielfeld[row+1][column-1]: rc = rc + 1
            if current_Spielfeld[row+1][column]: rc = rc + 1
            if current_Spielfeld[row+1][column+1]: rc = rc + 1
            if current_Spielfeld[row][column+1]: rc = rc + 1
            
    elif column == 0:  # erste Spalte (obere Ecke haben wir schon)
      
        if row == size-1: # Ecke unten links
            # prüfe alle 3 Nachbarn
            if current_Spielfeld[row-1][column]: rc = rc + 1
            if current_Spielfeld[row-1][column+1]: rc = rc + 1
            if current_Spielfeld[row][column+1]: rc = rc + 1
            
        else: # linker Rand ohne Ecken
            # prüfe alle 5 Nachbarn
            if current_Spielfeld[row-1][column]: rc = rc + 1
            if current_Spielfeld[row-1][column+1]: rc = rc + 1
            if current_Spielfeld[row][column+1]: rc = rc + 1
            if current_Spielfeld[row+1][column+1]: rc = rc + 1
            if current_Spielfeld[row+1][column]: rc = rc + 1
            
    elif row == size-1: # letzte Zeile (linke Ecke haben wir schon)
      
        if column == size-1: # rechte, untere Ecke
            # prüfe alle 3 Nachbarn
            if current_Spielfeld[row][column-1]: rc = rc + 1
            if current_Spielfeld[row-1][column-1]: rc = rc + 1
            if current_Spielfeld[row-1][column]: rc = rc + 1
            
        else: # unterer Rand ohne Ecken
            # prüfe alle 5 Nachbarn
            if current_Spielfeld[row][column-1]: rc = rc + 1
            if current_Spielfeld[row-1][column-1]: rc = rc + 1
            if current_Spielfeld[row][column]: rc = rc + 1
            if current_Spielfeld[row-1][column-1]: rc = rc + 1
            if current_Spielfeld[row][column+1]: rc = rc + 1
            
    elif column == size-1: # letzte Spalte (die Ecken haben wir schon)
            # rechter Rand ohne Ecken
            # prüfe alle 5 Nachbarn
            if current_Spielfeld[row-1][column]: rc = rc + 1
            if current_Spielfeld[row-1][column-1]: rc = rc + 1
            if current_Spielfeld[row][column-1]: rc = rc + 1
            if current_Spielfeld[row+1][column-1]: rc = rc + 1
            if current_Spielfeld[row+1][column]: rc = rc + 1
            
    else: # Innenfeld
        # prüfe alle 8 Nachbarn
        if current_Spielfeld[row-1][column]: rc = rc + 1
        if current_Spielfeld[row+1][column]: rc = rc + 1
        if current_Spielfeld[row-1][column-1]: rc = rc + 1
        if current_Spielfeld[row][column-1]: rc = rc + 1
        if current_Spielfeld[row+1][column-1]: rc = rc + 1
        if current_Spielfeld[row-1][column+1]: rc = rc + 1
        if current_Spielfeld[row][column+1]: rc = rc + 1
        if current_Spielfeld[row+1][column+1]: rc = rc + 1        
 
    """ kompakte Variante 2:
    rc = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            cur_row = row + i
            cur_col = column + j
            if cur_row < size and cur_row >= 0 and cur_col < size and cur_col >= 0:
                if i == 0 and j == 0:
                    # eigenes feld, nix machen
                    rc = rc + 0
                else:
                    if current_Spielfeld[cur_row][cur_col]: rc = rc + 1
    """
    
    return(rc)   
     
    
# main/Hauptprogramm
 
#spielbereich = turtle.Screen()
#spielbereich.title("Spiel des Lebens/Game of Life")
#spielbereich.setup(width=size*20, height=size*20)
 
print("*******************************************")
print("* Game of Life/Spiel des Lebens")
print("*******************************************")
try:
  size = int(input(" Wie groß soll das Spielfeld-Quadrat sein? "))
  # ab einer Größe von 10 wird es interessant :-)
  max_generation = int(input("Wieviele Generationen sollen angezeigt werden? 0 = unbegrenzt(bis zum manuellen Abbruch): "))
except ValueError:
  print("Bitte nur ganze Zahlen > 0 eingeben!")
 
erzeuge_Anfangs_Spielfeld()
generation = 0
 
# Die Schleife ist entweder endlos, oder hört nach der Erzeugung/Ausgabe der eingebenen Generationen auf
while generation < max_generation or max_generation == 0: 
    print(f"******************* Generation: {generation }")
    zeige_current_Spielfeld()
    current_Spielfeld = ermittle_next_Spielfeld()
    generation = generation + 1
    time.sleep(0.5) # ohne eine Pause sieht man in der print-Ausgabe nur fliegende Zeichen...
