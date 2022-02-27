## For Schleife
liste = [1,2,3,4,]
for i in liste:
	print(i)

name = "Python"
for i in name:
	print(i)
number = 10
for i in range(number,0,-1):
	print(i)
	
hexa = ["A", "B", "C", "D", "E", "F"]
for i in range(0,256,16):
	print(i, " ",end='')
	if i < 160:
		result = int(i/16)
		print(result, "0_16")
	elif i >= 160:
		result = (i/16)-10
		result = int(result)
		print(hexa[result],"0_16")
		