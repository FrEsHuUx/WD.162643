def ciag(* liczba):
    iloczyn = 1
    for i in range(0, liczba[2]):
        mnozenieele = liczba[0]*liczba[1]
        iloczynele = mnozenieele
        iloczyn *= iloczynele
    return iloczyn


print(ciag(2, 4, 3))
