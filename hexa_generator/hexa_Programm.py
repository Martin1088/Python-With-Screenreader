## hexa Dezimaler Übungsgsgenerator
import random

## Variablen 
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
		result = str(hexa[number])
	return result

## Hauptfunktion 
while UserInput != "q":
	## Variablen mit Zufallszahl werden aufgerufen
	quest = random.randint(1,65535)
	choice = random.randint(0,1)
	print("Mit q wird das Programm beendet!")
	## hier kommt die Umrechnung in Hexadezimalzahl 
	if quest >= 4096:
		Indexfour =int (quest / 4096)
		solution = HexaTranslator(Indexfour)
		rest = int(quest % 4096)
	if rest >= 256:
		Indextree = int(rest / 256) 
		solution = solution + HexaTranslator(Indextree)
		rest = int(rest % 256)
	if rest >= 16:
		Indextwo = int(rest / 16)
		solution = solution + HexaTranslator(Indextwo)
		rest = int(rest % 16)
	if rest < 15 and rest >= 0:
		Indexone = rest
		solution = solution + HexaTranslator(Indexone)
	print("Umrechnung war Erfolgreich")
	## Zufällig wird immer eine Hexa oder Deximal Zahl abgefragt 
	
	if choice == 0:
		print("Errechne dir die HexadezimaleZahl aus:", quest,)
		UserInput = input("gebe die Hexa Buchstaben immer groß an und keine leer Zeichen.")
		questString = str(quest) ## die Dezimalzahl wird für den Vergleich in einen String umgewandelt
		if UserInput == "q":
			continue
		if UserInput == solution:
			print("Die Zahl ", quest, " ergibt hexa ", solution, " ist Richtig!")
		else:
			print("Die Zahl ist falsch: ", UserInput, " ", solution)
	elif choice == 1:
		print("Berechne die Dezimalzahl: ", solution)
		UserInput = input("gebe den Wert ein:")
		questString = str(quest) ## die Dezimalzahl wird für den Vergleich in einen String umgewandelt
		if UserInput == "q":
			continue
		if UserInput == questString:
			print("Die Zahl ist richtig!")
		else:
			 print("Die Zahl ist falsch: ", UserInput, " ", quest)
			
