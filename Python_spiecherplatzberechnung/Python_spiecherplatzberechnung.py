Samplingrate = float(input("Samplingrate: ")) 
Audiolengt = float(input("Audiolänge: ")) 
Anzahlton = float(input("Anzahlton: ")) 
Samplingtiefe = float(input("Samplingtiefe: "))
Einheit = input("Einheit: ")
Ergebnis = Samplingrate * Audiolengt * Anzahlton * Samplingtiefe # Hier wird alles zusammen gerechnet
float(Ergebnis) # Umwandlung in eine Kommazahl um ein genaues Ergebnis zu ermitteln 
if Einheit != "":   # Wenn man eine Einheit Vorgibt dann

    if Einheit == "Bit":
        print(Ergebnis,"Bit")

    Ergebnis=Ergebnis/8

    if Einheit == "Btyte":
        print(Ergebnis,"Byte")

    Ergebnis=Ergebnis/1000

    if Einheit == "Kilobyte":
        print(Ergebnis,"Kb")

    Ergebnis=Ergebnis/1000

    if Einheit == "Megabyte":
        print(Ergebnis,"Mb")

    Ergebnis=Ergebnis/1000

    if Einheit == "Gigabyte":
        print(Ergebnis,"Gb")

    Ergebnis=Ergebnis/1000

    if Einheit =="Terabyte":
        print(Ergebnis,"Tb")

else:   #Sonst wird bis das kleiner gleich 1000 gerechnet und die passende Einheit festgelegt

    i = 0

    if Ergebnis <= 1000:
        print(Ergebnis,"Bit")

    Ergebnis=Ergebnis/8

    while Ergebnis >= 1000:

        Ergebnis = Ergebnis/1000

        i= i + 1
        
        if Ergebnis <= 1000:    #Hier wird die Einheit bestimmt
            if i == 1:
                print(Ergebnis,"By")

            if i == 2:
                print(Ergebnis,"Kb")
            
            if i == 3:
                print(Ergebnis,"Mb")

            if i == 4:
                print(Ergebnis,"Gb")

            if i == 5:
                print(Ergebnis,"Tb")
            if i >5:
                print(Ergebnis,"ich war zu faul")
            break