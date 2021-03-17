dictionary = {
    "Woda": "l",
    "Jablka": "kg",
    "Banany": "kg",
    "Baton": "szt",
    "Chleb": "szt",
    "Pizza": "szt"
    }
lista1 = [key for (key, value) in dictionary.items() if value == 'sztuki']
print(lista1)
