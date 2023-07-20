# Test framework
# abfrage des Rechenzeichen und Kontrolle der Ausgaben

def test_addition():
    result = addition(5, 5)
    assert (result == 10), "Result is false"
    print("Successful!")

def addition(numberOne, numberTwo):
    return numberOne + numberTwo

def test_subtraction():
    result = subtraction(10,4)
    assert (result == 6), "result is False"
    print("Sucessful")

def subtraction(numberTree, numberFour):
    return numberTree - numberFour

def test_multiplication():
    result = multiplication(4,6)
    assert (result == 24), "result is false"
    print("Successful!")

def multiplication(numberFive, numberSix):
    return numberFive * numberSix

def test_division():
    result = division(4,2)
    assert (result == 2), "result is false"
    print("Successful!")

def division(numberSeven, numberEight):
    return numberSeven / numberEight

# Taschenrechner
def menu():
	do
