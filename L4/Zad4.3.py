tekst = "Młody Ryszard Kalisz z kielonem\n"
tekst2 = "W chuja walisz, to tam są drzwi\n"
tekst3 = "Wyjdź z ziomalami\n"

with open("trzecie.txt", "w+") as plik:
    plik.write(tekst)
    plik.write(tekst2)
    plik.write(tekst3)

with open("trzecie.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
