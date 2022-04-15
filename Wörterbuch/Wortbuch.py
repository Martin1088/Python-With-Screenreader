## Englisches Wörterbuch als Test 
## Test für Datei einlesen 
## Funktion zum aussortieren 
def caseForLine(name):
	case01 = len(name) == 2 
	case02 = "," not in name[0:1] and "," not in name[0:1] and ";" not in name[0:1] and "(" not in name[0:1]
	if case01 and case02:
		return True
	else:
		return False
		
## Hauptfunktion
woerter = {} ##leeres Dictionary für das Wörterbuch 
counter = 0 ##Zählt die Anzahl an Zeilen bzw 
wrong = 0 ##Anzahl der Ungültigen Zeilen

fobj = open("Fachenglisch.txt","r")
for line in fobj:
	counter += 1
	line = line.strip()
	name = line.split(" - ")
	
	if caseForLine(name):
		woerter[name[1]] = name[0]
	else:
		wrong += 1
		print("Die Zeile", counter, "ist Ungültig")
fobj.close
print("Das einlesen war Erfolgreich")
print("Es sind ", wrong, "Ungültige Zeilen mit Fehlern")
fobj = open("Ergebnis.txt", "w")
for i in woerter:
	fobj.write("{} {}\n".format(i,woerter[i]))
fobj.close
	
	