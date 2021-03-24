class NaZakupy:
    ilosc = None
    cena_jed = None
    nazwa_produktu = None
    jednostka_miary = None

    def __init__(self, ilosc, cena_jed, nazwa_produktu, jednostka_miary):
        self.ilosc = ilosc
        self.cena_jed = cena_jed
        self.nazwa_produktu = nazwa_produktu
        self.jednostka_miary = jednostka_miary

    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.cena_jed, self.jednostka_miary)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        rownanie = self.ilosc * self.cena_jed
        print(('%(z1).2f %(z2)s kosztuje %(z3).2f' %
               {'z1': self.ilosc, 'z2': self.nazwa_produktu, 'z3': rownanie}))


nazakupy = NaZakupy(5, 3.60, "Beczkowe Mocne - Wiśnia", "szt")
nazakupy.wyswietl_produkt()
nazakupy.ile_produktu()
nazakupy.ile_kosztuje()
