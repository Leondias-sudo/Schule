Zahl = 50
i=1
a = list
while i != Zahl:
    if Zahl<=1:
        print(f"{Zahl} ist keine Primzahl")
        break

    if Zahl == 2:
        print(f"{Zahl} ist keine Primzahl")
        break

    if i%2 == 0:
        print(f"{i} ist keine Primzahl") 
    else:
        print(f"{i} ist eine Primzahl")

    i=i+1

    