slownik = {2: 's', 'ab': 'df', 3.4: 45, 2: 3}
print(slownik)

slownik['klucz'] = 'wartosc'
slownik[6] = 2
print(slownik)

print(slownik[6])
print(slownik['ab'])

slownik.pop(6)
print(slownik)

print(slownik.keys())
print(slownik.values())

del slownik[2]
print(slownik)

