## Einfache Listen mit Zufallszahlen
from random import randint

randomnumber = []
## Anzahl der Einträge
entry = 20
for i in range (entry):
	randomnumber.append(randint(0, 50))
print(randomnumber)
print("kleinster Wert:")
print(min(randomnumber))
print("größter Wert:")
print(max(randomnumber))
print("mittelwert der List:")
print(sum(randomnumber) / len(randomnumber))