# Zahlen raten leicht gemacht
# Python Programm zum einarbeiten

mystery = 4 # Hier wird die zu erratene Zahl vestgelegt 
guess = 0 # Variable Zahl für den Input
counter = -1 # zählen der Rateversuche 
while guess != mystery:
	print("Raten Sie eine Zahl zwischen 0 und 20!")
	guess = int(input("Geben Sie eine Ganzzahl ein:"))
	if guess > mystery:
		print("Die Zahl ist zu groß")
	elif guess < mystery:
		print("die Zahl ist zu klein!")
	connter = counter + 1

print(f"Die Zahl ist {mystery} es wurden {counter} Versuche benötigt!")