from Einwohner import *

class Adel(Einwohner):
    def __init__(self) -> None:
        super().__init__()

    def steuer(self):
        result = int(self.einkommen / self.amounttax)
        if result <= 20:
            return 20
        return result

