Samplingrate = float(input("Samplingrate: ")) 
Audiolengt = float(input("Audiolänge: ")) 
Anzahlton = float(input("Anzahlton: ")) 
Samplingtiefe = float(input("Samplingtiefe: "))
Einheit = input("Einheit: ") 
Ergebnis = Samplingrate * Audiolengt * Anzahlton * Samplingtiefe 
float(Ergebnis)
teilwert = 1000
teilwertbyte = 8
float(teilwertbyte)
float(teilwert)
if Einheit != "":
    if Einheit == "Bit":
        print(Ergebnis,"Bit")

    Ergebnis=Ergebnis/teilwertbyte
    if Einheit == "Btyte":
        print(Ergebnis,"Byte")

    Ergebnis=Ergebnis/teilwert

    if Einheit == "Kilobyte":
        print(Ergebnis,"Kb")

    Ergebnis=Ergebnis/teilwert

    if Einheit == "Megabyte":
        print(Ergebnis,"Mb")

    Ergebnis=Ergebnis/teilwert

    if Einheit == "Gigabyte":
        print(Ergebnis,"Gb")

    Ergebnis=Ergebnis/teilwert

    if Einheit =="Terabyte":
        print(Ergebnis,"Tb")
else:
    if Ergebnis <= teilwert:
        print(Ergebnis,"Bit")

    Ergebnis=Ergebnis/teilwertbyte

    if Ergebnis<= teilwert:
        print(Ergebnis,"Byte")

    while Ergebnis >= teilwert:
        Ergebnis = Ergebnis/teilwertbyte
        if Ergebnis <= teilwert:
            print(Ergebnis)
            break
        
