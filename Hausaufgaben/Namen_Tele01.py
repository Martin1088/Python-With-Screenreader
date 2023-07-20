## Telefonnummer und Namen als test 
from random import randint

## Vorname, Nachname, Televonnummer
Adressliste = [
["Max","Mustermann",""],
["Eli", "Müller", ""],
["Ernie", "Talberg", ""],
["Tina", "Wegener", ""],
["Toni", "Klein", ""]
]
for i in Adressliste:
	print(i[0])
	print(i[1])
	for j in range(8):
		randomnumber =(str) (randint(0,9))
		i[2].append(randomnumber)
	print(i[2], end='\n')
print("Ende der Liste")