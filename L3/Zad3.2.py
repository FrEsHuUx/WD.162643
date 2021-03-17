import random
lista1 = [random.random() for x in range(10)]
lista2 = [x for x in lista1 if not (x % 2)]

print(lista1)
print(lista2)

del lista1
del lista2
