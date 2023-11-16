a: int = int(input("Number "))
count = 2
rest: int = int(a /2 )
prim: int = 0
while count <= rest:
    result = a % count
    if result == 0:
        print(f"{count} is possible")
        prim = prim + 1
    count = count + 1

if prim == 0:
    print("{a} is a prime number")

