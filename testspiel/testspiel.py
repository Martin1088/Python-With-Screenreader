# Test Spiel
#eine Zahl muss erraten werden

geheimnis = 99
versuch = -1
zaehler = 0
while versuch != geheimnis:
    versuch = int(input("Raten Sie eine Ganzzahl: "))
    if versuch < geheimnis:
        print("zu klein")
    if versuch > geheimnis:
        print("zu groß")
    zaehler = zaehler + 1
print("Super, Sie haben es in ", zaehler, "Versuchen geschafft")
