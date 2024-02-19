class Gebaeude:

    def __init__(self, ad, pr, bau) -> None:
        self.__adresse = ad
        self.__preis = pr
        self.__baujahr = bau

    __adresse = ""

    __preis = 0.00

    __baujahr = 0

    def get_daten(self) -> str:
        return "Adresse: " + self.__adresse +"\nl"\
        "Preis: " + self.__preis + "\nl" \
        "Baujahr" + self.__baujahr