class Fahrzeug:
    def __init__(self) -> None:
        self.__aktTankfuellung = 40
        self.__maxTankfuellung = 50
        self.__readerProAchse = 2

    __readerProAchse = 0

    __maxTankfuellung:float = 0

    __aktTankfuellung:float = 0

    def get_ReaderProAchse(self):
        return self.__readerProAchse

    def set_ReaderProAchse(self, value):
        self.__readerProAchse = value

    def get_AktTankfuellung(self):
        return f"{self.__aktTankfuellung} l"

    def set_AktTankfuellung(self, value):
        self.__aktTankfuellung = value
    
    def get_MaxTankfuellung(self):
        return f"{self.__maxTankfuellung} l"
    
    def set_MaxTankfuellung(self, value):
        self.__maxTankfuellung = value

    def fahren(self, km:int) -> bool:
        if self.__aktTankfuellung == 0:
            return False
        verbrauch = 6.4/100

        verbrauchStrecke = km * verbrauch

        if verbrauchStrecke < 0:
            return False
        
        self.set_AktTankfuellung((self.__aktTankfuellung - verbrauchStrecke))

        return True

    def Tanken(self,value) -> bool:
        if value > self.__maxTankfuellung or value+self.__aktTankfuellung > self.__aktTankfuellung or value <= 0:
            return False
        
        self.set_AktTankfuellung(value+self.__aktTankfuellung)
        return True

auto = Fahrzeug()
auto.fahren(100)
print(f"{auto.get_AktTankfuellung()}")
erfolg:bool = auto.Tanken(50)
if not erfolg:
    print("Tank zu Voll")
else:
    print("Erfolgreich getankt")

print(f"{auto.get_AktTankfuellung()}")