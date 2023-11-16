def bubbleSort(list):
    for i in range(len(list)):
        print(i + 1, "-ter Durchlauf:")
        print("Aktueller Stand: ", list)
        for j in range(len(list) -1):
            print("Vergleiche ", list[j], " und ", list[j+1])
            if list[j] > list[j+1]:
                print("Tausche ", list[j], " und ", list[j+1])
                x = list[j]
                list[j] = list[j+1]
                list[j+1] = x
    print("Sortierung abgeschlossen")
    return list

def quickBubbleSort(list):
    for i in range(len(list) - 1):
        print(i + 1, "-ter Durchlauf:")
        print("Aktueller Stand: ", list)
        print("In dieser Runde werden die ersten ", len(list) - i, " Einträge behandelt. Bei den letzten ", i, " Einträgen wird sich nichts mehr ändern.")
        for j in range(len(list) -1 - i):
            print("Vergleiche ", list[j], " und ", list[j+1])
            change = False
            if list[j] > list[j+1]:
                print("Tausche ", list[j], " und ", list[j+1])
                x = list[j]
                list[j] = list[j+1]
                list[j+1] = x
                change = True
        if not change:
            print("Es hat sich über die ganze Runde nichts mehr geändert. Wir können abbrechen, weil sich auch in weiteren Runden nichts mehr ändern wird.")
            return list
    print("Den letzten Durchlauf brauchen wir nicht, weil alle bis auf das erste Element richtig sortiert sind. Daraus folgt, dass auch das erste Element richtig sortiert ist.")
    return list

def insertionSort(list):
    print("Schritt 1:")
    newlist = []
    newlist.append(list[0])
    print("Das erste Element der alten Liste, ", list[0], ", bildet den Start der neuen Liste.")
    for i in range(1, len(list)):
        print("Aktueller Stand: ", newlist)
        print("Schritt ", i + 1, ":")
        element = list[i]
        print("Einzufügendes Element: ", element)
        for j in range(len(newlist) + 1):
            if j == len(newlist):
                print("Die Zahl ", element, " ist größer als alle bisher eingefügten Elemente. Daher kommt sie ans Ende der neuen Liste.")
                newlist.append(element)
            elif element <= newlist[j]:
                print(element, " ist kleiner als ", newlist[j], ". Einfügestelle gefunden.")
                newlist.insert(j, element) #Das größere Element und die Restliste wird dadurch nach hinten verschoben und das Element damit richtig eingefügt
                break #Der Rest der neuen Liste muss nicht mehr durchsucht werden, es kann direkt mit dem nächsten Element weitergemacht werden
            else:
                print(element, " ist größer als ", newlist[j])
    return newlist

def selectionSort(list):
    newlist = []
    for i in range(len(list)):
        print("Schritt ", i + 1, ":")
        min = list[0]
        print("Suche nach dem Minimum. Minimum wird zunächst auf das erste Element der Liste festgelegt: ", min, ". Durchsuche Liste nach kleinerem Minimum.")
        for j in range(1, len(list)):
            if list[j] < min:
                print(list[j], " ist kleiner als ", min, ". Minimum wird aktualisiert.")
                min = list[j]
            else:
                print(list[j], " ist größer als ", min)
        print("Endgültiges Minimum in dieser Runde gefunden: ", min)
        print("Hänge dieses Minimum ans Ende der neuen Liste an. Lösche es aus der alten Liste.")
        list.remove(min)
        newlist.append(min)
        print("Aktueller Stand: ", newlist)
    print("Abgeschlossen. Alte Liste vollständig geleert.")
    return newlist

def mergeSort(list):
    print("Starte neue Funktion. Dieser Aufruf der Funktion hat folgende Liste erhalten: ", list)
    if len(list) == 1:
        print("Diese Funktion hat als Liste nur eine Zahl erhalten. Sie ist also schon fertig und kann diese Liste einfach unverändert zurückgeben.")
        return list
    print("Die Liste soll in zwei möglichst gleichgroße Teillisten zerlegt werden.")
    print("Die Länge der Liste ist ", len(list), ", und ", len(list), " geteilt durch zwei (ohne Nachkommaanteil) ist ", len(list) // 2)
    print("Wir spalten die Liste also an dieser Stelle.")
    first = list[:len(list) // 2]
    second = list[len(list) // 2:]
    print("Erste Liste: ", first)
    print("Zweite Liste: ", second)
    firstSort = mergeSort(first)
    secondSort = mergeSort(second)
    print("Die zwei rekursiven Funktionen haben beide ihr Ergebnis zurückgegeben. Wir befinden uns nun wieder in einer höheren Funktion.")
    print("Zur Übersicht: Wir sind jetzt wieder in der Funktion mit den folgenden beiden Teillisten:")
    print("Erste Liste: ", first)
    print("Zweite Liste: ", second)
    print("Die Listen wurden nun also rekursiv bearbeitet und sehen jetzt wie folgt aus: ")
    print("Erste Liste: ", firstSort)
    print("Zweite Liste: ", secondSort)
    print("Es ist nun also garrantiert, dass die beiden Teillisten jeweils richtig sortiert sind. Nun wollen wir diese beiden Teillisten zusammenbauen.")
    print("Wir vergleichen jetzt (wegen der Vorsortierung) also immer nur das erste Element beider Listen und fügen das jeweils kleinere hinten an.")
    newlist = []
    while True:
        if firstSort == []:
            print("Die erste Liste ist jetzt ganz leer. Den Rest der zweiten können wir jetzt also einfach komplett hinten dranpacken ohne weitere Berechnungen.")
            newlist = newlist + secondSort
            break
        if secondSort == []:
            print("Die zweite Liste ist jetzt ganz leer. Den Rest der zweiten können wir jetzt also einfach komplett hinten dranpacken ohne weitere Berechnungen.")
            newlist = newlist + firstSort
            break
        elif firstSort[0] < secondSort[0]:
            print(firstSort[0], " ist kleiner als ", secondSort[0])
            newlist.append(firstSort[0])
            firstSort.pop(0)
        else:
            print(firstSort[0], " ist größer als ", secondSort[0])
            newlist.append(secondSort[0])
            secondSort.pop(0)
        print("Aktueller Stand: ", newlist)
    print("Jetzt sind beide Teillisten aufgebraucht. Das Ergebnis lautet: ", newlist, ". Es wird jetzt zurückgegeben")
    return newlist

def quickSort(list):
    print("Starte neue Funktion. Dieser Aufruf der Funktion hat folgende Liste erhalten: ", list)
    if len(list) == 1:
        print("Diese Funktion hat als Liste nur eine Zahl erhalten. Sie ist also schon fertig und kann diese Liste einfach unverändert zurückgeben.")
        return list
    if len(list) == 0:
        print("Diese Funktion hat eine komplett leere Liste erhalten. Sie ist also schon fertig und kann diese Liste einfach unverändert zurückgeben.")
        return list
    print("Zunächst muss ein zufälliges Pivotelement gewählt werden. Wähle hier als Beispiel ganz einfach das erste Element der Liste")
    pivot = list[0]
    print("Pivotelement: ", pivot)
    lesser = []
    equal = []
    greater = []
    print("Jetzt erstellen wir drei neue Listen und ordnen unsere ursprüngliche Liste in die drei neuen ein, je nach dem, ob das Element kleiner, gleich oder größer als das Pivot ist.")
    for element in list:
        if element < pivot:
            print(element, " ist kleiner als ", pivot)
            lesser.append(element)
        elif element == pivot:
            print(element, " ist gleich ", pivot)
            equal.append(element)
        else:
            print(element, " ist größer als ", pivot)
            greater.append(element)
    print("Unsere drei Listen sind fertig:")
    print("Liste mit kleineren Elementen: ", lesser)
    print("Liste mit gleichen Elementen: ", equal)
    print("Liste mit größeren Elementen: ", greater)
    print("Diese drei Listen werden jetzt per Rekursion wieder an drei gleiche quicksort-Funktionen weitergegeben.")
    lesserSort = quickSort(lesser)
    equalSort = quickSort(equal)
    greaterSort = quickSort(greater)
    print("Die drei rekursiven Funktionen haben alle ihr Ergebnis zurückgegeben. Wir befinden uns nun wieder in einer höheren Funktion.")
    print("Zur Übersicht: Wir sind jetzt wieder in der Funktion mit den folgenden Teillisten:")
    print("Liste mit kleineren Elementen: ", lesser)
    print("Liste mit gleichen Elementen: ", equal)
    print("Liste mit größeren Elementen: ", greater)
    print("Die Listen wurden nun also rekursiv bearbeitet und sehen jetzt wie folgt aus: ")
    print("Liste mit kleineren Elementen: ", lesserSort)
    print("Liste mit gleichen Elementen: ", equalSort)
    print("Liste mit größeren Elementen: ", greaterSort)
    print("Es ist nun also garrantiert, dass alle Teillisten jeweils richtig sortiert sind. Nun wollen wir diese Teillisten zusammenbauen.")
    print("Im Gegensatz zu Mergesort wissen wir hier nicht nur, dass die Teillisten sortiert sind.")
    print("Wir wissen zusätzlich noch, dass alle Elemente in der Kleiner-Liste kleiner sind als die in der Gleich-Liste.")
    print("Auch wissen wir, dass die Elemente der Gleich-Liste kleiner sind als die in der Größer-Liste.")
    print("Das heißt also, wir können komplett ohne Berechnungen in einer einzigen Zeile die drei Listen zu einer neuen zusammenbauen, indem wir sie einfach hintereinandersetzen.")
    newlist = lesserSort + equalSort + greaterSort
    print("Die fertige Liste lautet: ", newlist, ". Sie wird nun zurückgegeben")
    return newlist

active = True
print("Beispielerklärer für Sortieralgorithmen")
print("Folgende Algorithmen kannst du mit eigenen Beispielen ausprobieren:")
print("- Naives Bubblesort mit dem Kürzel naivebubble")
print("- Schlaues Bubblesort mit dem Kürzel fastbubble")
print("- Insertionsort mit dem Kürzel insertion")
print("- Selectionsort mit dem Kürzel selection")
print("- Mergesort mit dem Kürzel merge")
print("- Quicksort mit dem Kürzel quick")
print("Tippe einfach das Kürzel, dann eine Leertaste und dann, jeweils von einem Leerzeichen getrennt, verschiedene Zahlen, die deine Liste bilden sollen.")
print("Beispiel: naivebubble 1 3 2 5 7")
while active:
    command = input(">").lower()
    commandList = command.split(" ")
    for i in range(1, len(commandList)):
        commandList[i] = int(commandList[i])
    if commandList[0] == "quit":
        active = False
    elif commandList[0] == "naivebubble":
        commandList.pop(0)
        print("Ergebnis: ", bubbleSort(commandList))
    elif commandList[0] == "fastbubble":
        commandList.pop(0)
        print("Ergebnis: ", quickBubbleSort(commandList))
    elif commandList[0] == "insertion":
        commandList.pop(0)
        print("Ergebnis: ", insertionSort(commandList))
    elif commandList[0] == "selection":
        commandList.pop(0)
        print("Ergebnis: ", selectionSort(commandList))
    elif commandList[0] == "merge":
        commandList.pop(0)
        print("Ergebnis: ", mergeSort(commandList))
    elif commandList[0] == "quick":
        commandList.pop(0)
        print("Ergebnis: ", quickSort(commandList))
    else:
        print("Eingabe ungültig")