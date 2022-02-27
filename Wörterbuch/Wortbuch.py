## Englisches Wörterbuch als Test 
## Test für Datei einlesen 

woerter = {} ##leeres Dictionary für das Qörterbuch 
counter = 0 ##Zählt die Anzahl an Zeilen bzw 
wrong = 0 ##Anzahl der Ungültigen Zeilen
fobj = open("Fachenglisch.txt","r")
for line in fobj:
	counter += 1
	line = line.strip()
	name = line.split(" - ")
	if len(name) == 2 and (name[0].count(",") == 0 and name[1].count(",") == 0):
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
	
	