##Eingabe zweier Zahlen diese werden adiert 
numberOne = 0
numberTwo = 0
def ReadNumber():
	try:
		number = int(input("Geben Sie eine Ganzzahl ein: "))
		return number
	except ValueError:
		print("Dies ist keine gültige Ganzzahl!")
		
## Hauptfunktion 
numberOne = ReadNumber()
numberTwo = ReadNumber()
result = numberOne + numberTwo
print("Die beiden Zahlen ergeben: " ,result)
	