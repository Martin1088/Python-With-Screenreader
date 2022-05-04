## geschachtelte Liste mit Einkäufen 
## Listeneinträge:
## Artikel, Nettobetrag, Merhwertsteuer(Prozent), Anzahlartikel
liste = [["Schokolade", 1, 5, 5],
["Toilettenpapier", 3, 16, 5],
["Kaffeemaschine", 90, 16, 1],
["Kaffee", 4, 5, 10],
["Tee gemischt", 6, 5, 5],
["Mikrowelle", 150, 16, 1],
["Tassen", 2, 16, 40]]
## Ausgabe der Artikel
print("=====")
## Variablen
mwst = 0
mwst_neu = 0
gesamt_mwst_alt = 0
gesamt_mwst_neu = 0
gesamt_wert_alt = 0
gesamt_wert_neu = 0
for i in liste:
	print(i[0])
	mwst = 0
	mwst =(i[2]/100) * i[1] * i[3]
	print("Die Mehrwertsteuer beträgt:", round(mwst, 2) ," Euro" )
	gesamt_mwst_alt = gesamt_mwst_alt + mwst 
	gesamt_wert_alt = gesamt_wert_alt + i[1]* i[3] + mwst
	## Neuer Betrag durch Mehrwert änderung
	if i[2] == 5:
		mwst_neu =(7/100) * i[1] * i[3]
		gesamt_mwst_neu = gesamt_mwst_neu + mwst_neu 
		gesamt_wert_neu = gesamt_wert_neu + i[1] * i[3] + mwst_neu
	elif i[2] == 16:
		mwst_neu =(19/100) * i[1] * i[3]
		gesamt_mwst_neu = gesamt_mwst_neu + mwst_neu 
		gesamt_wert_neu = gesamt_wert_neu + i[1] * i[3] + mwst_neu
	else:
		print("Mehrwertsteuer ist falsch")
## gesamte Werte 
print("Der gesamte Einkauf hat ", round(gesamt_wert_alt, 2) ," Euro gekostet")
print("Die gesamte Mehrwertsteuer beträgt: ", round(gesamt_mwst_alt, 2), "Euro ")
## Nere Werte 
print("====Neue====")
print("Der gesamte Einkauf hat ", round(gesamt_wert_neu, 2) ," Euro gekostet")
print("Die gesamte Mehrwertsteuer beträgt: ", round(gesamt_mwst_neu, 2), "Euro ")
