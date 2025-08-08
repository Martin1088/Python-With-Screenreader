## verschachtelte Listen mit verschiedenen Datentypen
## Aufgaben zum auslesen 
sus = [
["Erna", 17, "A"],
["Ernie", 16, "S"],
["Heorge", 20, "D"],
["Gerda", 20, "S"],
["Merlin", 14, "D"]
]
print(sus)
## variablen 
total = 0
for i in sus:
	total = total +  i[1]
average = total / len(sus)
print(average)
## alle Systemintegratoren mit S in eine Liste
sys = []
for i in sus:
	if (i[2] == "S"):
		sys.append(i)
print("Alle Systemintegratoren:")
print(sys)
print(f"Alter: {sus[2][1]}")
print(f"Name: {sus[1][0]}")
