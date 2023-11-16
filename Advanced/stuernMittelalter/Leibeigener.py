from Bauer import *

class Leibeigener(Bauer):
    def __init__(self) -> None:
        super().__init__()

    def steuer(self):
        result = int(self.einkommen / self.amounttax)
        if result <= 12:
            return 0
        return result

