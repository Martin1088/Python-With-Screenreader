## Berechnen der Mehrwertsteuer 

def TaxCalculater(netto, percent):
	brutto  = netto + (netto/100) * percent
	return brutto
	
## Hauptfunktion 
while Tru:
	print("willkommen zum Mehrwertsteuer Rechner!")
	print("1.Merwertsteuer mit 7%. \n 2.Merwertsteuer mit %19. \n 3. Beende das Programm.\n")
	number = int(input("Geben Sie eine Zahl ein siehe oben zwischen 1-3!"))
	if number == 1:
		netto = float(input("Geben Sie Ihren Netto Betrag ein: "))
		brutto = TaxCalculater(netto, 7)
		print("Die Merhwertsteuer aus 7% ist: ", brutto, "Euro")
	if number == 2:
		netto = float(input("Geben Sie Ihren Netto Betrag ein: "))
		brutto = TaxCalculater(netto, 19)
		print("Die Merhwertsteuer aus 19% ist: ", brutto, "Euro")
	if number == 3:
		print("Das Program wird beendet")
		break