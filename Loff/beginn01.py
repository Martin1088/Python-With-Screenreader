## Anweisungen
print("Hello world")
name = input("Gebe deinen Namen ein!")
print(f"Willkommen{name}")
gut = "gut"
schlecht = "schlecht"
while True:
	print("Wie geht es dir ?")
	result = input("gut oder schlecht?")
	if result == gut:
		print("Das ist schön das es dir gut geht")
		break
	elif result == schlecht:
		print("Das tut mir Leid")
		break
	else:
		print("Gib gut oder Schlecht an!")
print("Bis zum nächsten Mal")