from abc import ABC, abstractmethod


class Einwohner(ABC):
    einkommen: int
    amounttax: int

    def __init__(self):
        self.einkommen: int = 0
        self.amounttax: int = 10

    def zuVersteuerndesEinkommen(self):
        return self.einkommen

    def steuer(self):
        result = int(self.einkommen / self.amounttax)
        if result <= 1:
            return 1
        return result

    def setEinkommen(self, einkommenIn):
        self.einkommen = einkommenIn
