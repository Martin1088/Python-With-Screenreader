class Azubi:
    vorname: str
    name: str
    firma: str
    gehalt: int

    # def __init__(self, vorname, name, firma, gehalt):
        # self._vorname = vorname
        # self._name = name
        # self._firma = firma
        # self._gehalt = gehalt

    def __init__(self):
        self.vorname = ""
        self.name = ""
        self.firma = ""
        self.gehalt = 0

    def setName(self, nameIn: str):
        self.name = nameIn

    def setVorname(self, vornameIn: str):
        self.vorname = vornameIn

    def setGehalt(self, gehaltIn: int):
        if gehaltIn >= 400:
            self.gehalt = gehaltIn
        else:
            self.gehalt = 400

    def berechneAbschlussnote(self, notenIn: list):
        result: float = 0
        for note in notenIn:
            result += note
        result = result / len(notenIn)
        return result
    
    def setFirma(self, firmaIn: str):
        self.firma = firmaIn 

    def output(self):
        print(f"Name: {self.vorname} {self.name} \n Frima: {self.firma} \n Gehalt: {self.gehalt}")
    
## Ausgabe
#first = Azubi("Hans", "Peter", "SeuerOase", "3000")
#print(f"Name: {first._vorname} {first._name}\n Frima: {first._firma}\n Gehalt:{first._gehalt}")
second = Azubi()
second.setVorname("Clemens")
second.setName("Glücklich")
second.setFirma("Happy computer")
second.setGehalt(300)
second.output()
print(f"Abschlussnote: {second.berechneAbschlussnote([1, 4, 3, 2, 2])}")


