Samplingrate = int(input()) 
Audiolengt = int(input()) 
Anzahlton = int(input()) 
Samplingtiefe = int(input()) 
Ergebnis = Samplingrate * Audiolengt * Anzahlton * Samplingtiefe #Hier  
Ergebnis/8000 #Der Output ist in Bytes
print(Ergebnis)
