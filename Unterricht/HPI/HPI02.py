# 2 Woche des Kurses 


liste = [2,44, 7,8,11,27,0]
print(liste)
wert = max(liste)
print("Groesster Wert:", wert)
liste.sort()
print("Die sortierte Liste: ",liste)
satz = "dies ist ein Test"
print(satz.count("t"))
## Ausgabe von importierten Daten
##import sys
##sys.path.append("\daten")
##from daten import alter
##print(alter)
import daten
print(daten.alter)
print(daten.namen_liste)
for i in daten.alter:
	if i < 20:
		print("Haus Regenbogen")
	elif i > 20:
		print("Haus Sonnenschein")
