# die Fakultät von einer Zahl bilden

while True:
	number = int(input("Geben Sie eine Ganzzahl: "))
	if number < 0:
		print("negative Zahlen sind nicht möglich!")
		continue
	result =1
	for i in range(2, number+1):
		result = result * i
		print(result)
	print("Das Ergebnis ist: ", result)
	break
		