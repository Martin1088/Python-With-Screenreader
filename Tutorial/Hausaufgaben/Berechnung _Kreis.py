## Berechnen von des Volumens und Umfang
import math
print(math.pi)
r = [4.0 , 7.1, 18.5]
print(r)
print(type(r[0]))
## Umfang der Kreise
print("Die Umfänge der kreise sind:")
for i in r:
	U = 2 * (math.pi) * i
	print(U, end=" /")
print("")
## Berechnung der Flächen 
print("Die Flächen der Kreise sind")
for i in r:
	F = (math.pi) * ( i ** 2)
	print(F, end=" /")
print("")
## Berechnung des Volumensder Kugel
print("Die Volumen der Kugeln sind: ")
for i in r:
	V = 4/3 * (math.pi) * (i ** 3)
	print(V, end=" /")

