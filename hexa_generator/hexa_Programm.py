## hexa Dezimaler Übungsgsgenerator
import random

## Variablen 
qest = random.randint(1,65535)
choice = random.randint(0,1)
solution = ""
UserInput = ""
## Funktion zum bestimmen der Hexadezimalen Zahl
def HexaTranslator(number):
	hexa = ["A","B","C","D","E","F"]
	result = ""
	if number < 10:
		result = str(number)
	elif number >= 10:
		number = number - 10
		result = hexa[result]
	return result

## Hauptfunktion 
try:
	while UserInput != "q":
		print("Mit q wird das Programm beendet!")
		## hier kommt ><
		if choice == 0:
			Print("Errechne dir die HexadezimaleZahl aus:", quest,)