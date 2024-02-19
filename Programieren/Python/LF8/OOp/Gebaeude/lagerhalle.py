from gebaeude import Gebaeude

class Lagerhalle(Gebaeude):
    def __init__(self, ad, pr, bau, lagfl) -> None:
        super().__init__(ad, pr, bau)
        self.lagerflaeche = lagfl

    lagerflaeche = 0.0

    def get_daten(self) -> str:
        return "Adresse: " + self.__adresse +"\nl"\
        "Preis: " + self.__preis + "\nl" \
        "Baujahr: " + self.__baujahr + "\nl" \
        "Lagerflaeche: " + self.lagerflaeche