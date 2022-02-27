print("Hallo")
print("Dies ist ein Test")
print("Hier testen wir die Eingabe!")
while (True):
    try:
        number = int(input("Geben Sie eine Zahl ein!"))
        break
    except ValueError:
        print("Dies ist keine gültige Ganzzahl!")
print(f"Es ist die Nummer {number}")   