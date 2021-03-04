a = input('wprowadz liczbe a: ')
b = input('wprowadz liczbe b: ')

a = int(a)
b = int(b)

if a > b:
    print('liczba ' + str(a) + ' jest wieksza')
elif a < b:
    print('liczba ' + str(b) + ' jest wieksza')
else:
    print("liczba sa rowne")
