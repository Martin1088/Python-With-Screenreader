## Beispiel für while Schleife 

co2_wert = GetValue()
nochmal = True

while nochmal:
	if co2_wert < 1000:
		print("Alles Okay")
		co2_wert GetValue()
		nochmal = True
	if co2_wert >= 1000:
		print("Bitte Fenster auf")
		nochmal =False
	co2_wert = GetValue()
print("Ende")
