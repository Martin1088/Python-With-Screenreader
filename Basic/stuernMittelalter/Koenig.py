from Einwohner import *

class Koenig(Einwohner):
    def __init__(self) -> None:
        super().__init__()

    def steuer(self):
        return self.einkommen

