from gebaeude import Gebaeude

class Wohnhaus(Gebaeude):
    def __init__(self, ad, pr, bau, anzWo) -> None:
        super().__init__(ad, pr, bau)
        self.__anzahlWonungen = anzWo

    __anzahlWonungen = 0

    def get_daten(self):
        daten = "Adresse: " + super().__adresse +"\nl"\
        "Preis: " + super().__preis + "\nl" \
        "Baujahr: " + super().__baujahr + "\nl" \
        "Anzahl Wohnungen: " + self.__anzahlWonungen

        return daten
    
