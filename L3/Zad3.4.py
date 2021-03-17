def prostokat(q, w, e):
    if (q + w > e) and (q + e > w) and (w + e > q):
        if (q * q + w * w == e * e) or (q * q + e * e == w * w) or (e * e + w * w == q * q):
            print("Jest trojkat prostokatny")
        else:
            print("Nie jest trojkat prostokatny")
    else:
        print("Nie mozna zbudowac trojkat")


q = input("Wpisz q: ")
w = input("Wpisz w: ")
e = input("Wpisz e: ")
prostokat(q, w, e)
