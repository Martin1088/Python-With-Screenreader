
a: int= int(input("Number  "))
b: int = int(input("Number to divide"))
count: int = a

while count >= 0:
    rest: int = a % b
    result = count / b
    count = result - b
    print(f"{a} / {b} = {result} Rest {rest}")


