import random
lista = []
for x in range(0, 10):
    n = random.randint(0, 30)
    lista.append(n)

new_list = [x * 2 for x in lista]

file = open("pierwsze.txt", "w+")
file.write(str(new_list))
file.close()
