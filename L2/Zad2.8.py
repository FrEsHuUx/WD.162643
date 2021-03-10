lista = []
z = 0
while z < 10:
    a = int(input("Wprowadz liczbe: "))
    if a % 2 == 0:
        lista.append(a)
    z += 1
print("\n Parzyste liczby ", lista)
