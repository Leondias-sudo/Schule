Samplingrate = float(input("Samplingrate: ")) 
Audiolengt = float(input("Audiolänge: ")) 
Anzahlton = float(input("Anzahlton: ")) 
Samplingtiefe = float(input("Samplingtiefe: "))
Einheit = input("Einheit: ")
Ergebnis = Samplingrate * Audiolengt * Anzahlton * Samplingtiefe # Hier wird alles zusammen gerechnet
float(Ergebnis) # Umwandlung in eine Kommazahl um ein genaues Ergebnis zu ermitteln 
if Einheit != "":   
    if Einheit == "Bit":
        print(Ergebnis,"Bit")

    Ergebnis = Ergebnis / 8

    if Einheit == "Btyte":
        print(Ergebnis,"Bt")

    Ergebnis = Ergebnis / 1000

    if Einheit == "Kilobyte":
        print(Ergebnis,"Kb")

    Ergebnis = Ergebnis / 1000

    if Einheit == "Megabyte":
        print(Ergebnis,"Mb")

    Ergebnis = Ergebnis / 1000

    if Einheit == "Gigabyte":
        print(Ergebnis,"Gb")

    Ergebnis = Ergebnis / 1000

    if Einheit =="Terabyte":
        print(Ergebnis,"Tb")

else: 

    i = 0

    if Ergebnis <= 1000:
        print(Ergebnis,"Bit")

    Ergebnis = Ergebnis / 8

    while True:

        i = i + 1
        
        if Ergebnis <= 1000:    #Hier wird die Einheit bestimmt
            if i == 1:
                print(Ergebnis,"Bt")

            if i == 2:
                print(Ergebnis,"Kb")
            
            if i == 3:
                print(Ergebnis,"Mb")

            if i == 4:
                print(Ergebnis,"Gb")

            if i == 5:
                print(Ergebnis,"Tb")
            if i >5:
                print("Das Dlc ist bald erhältlich")
            break
                

        Ergebnis = Ergebnis / 1000