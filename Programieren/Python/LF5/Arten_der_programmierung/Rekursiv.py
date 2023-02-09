def fakultaet(multiplikator:int):
    if multiplikator <= 0:
        return 1

    else:
        Wert.insert(0,multiplikator)
        return multiplikator * fakultaet(multiplikator-1)

Wert=[]                     #Defintion der Variabeln
inputusr = int(input(""))

fakultaet(inputusr) #Aufruf der Funktion

print(Wert)