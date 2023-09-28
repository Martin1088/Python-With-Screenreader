def calc(km, benzin):
    return float(benzin / km * 100)

print("Benrinverbrauch berechnen:")
distance: int = int(input("Länge der Strecke"))
benzin: int = int(input("Menge des Benzin"))
print(f"Durchschnittlicher Verbrauch {calc(distance, benzin)} in Liter")

