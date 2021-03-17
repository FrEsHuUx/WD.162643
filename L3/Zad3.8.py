produkt = {
    "Mleko": 2.59,
    "Kawa": 22.99,
    "Sok": 4.99,
    "Baton": 2.99,
    "Pizza": 9.99
}


def lista(** lista):
    ile = len(produkt)
    suma = sum(produkt.values())
    print("Ilosc produktow:", ile)
    print("Cena produktow:", suma, "PLN")


lista()
