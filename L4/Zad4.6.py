class Robaczek:
    x = 3
    y = 3
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def pokaz_gdzie_jestes(self):
        return print("pozycja x = ", self.x, "pozycja y =", self.y)

    def idz_w_gore(self, ile_krokow):
        self.ile_krokow = ile_krokow
        ile_w_gore = self.ile_krokow * self.krok
        self.y += ile_w_gore

    def idz_w_dol(self, ile_krokow):
        self.ile_krokow = ile_krokow
        ile_w_dol = self.ile_krokow * self.krok
        self.y -= ile_w_dol

    def idz_w_lewo(self, ile_krokow):
        self.ile_krokow = ile_krokow
        ile_w_lewo = self.ile_krokow * self.krok
        self.x -= ile_w_lewo

    def idz_w_prawo(self, ile_krokow):
        self.ile_krokow = ile_krokow
        ile_w_prawo = self.ile_krokow * self.krok
        self.x += ile_w_prawo


robak = Robaczek(3, 3, 1)
robak.pokaz_gdzie_jestes()
robak.idz_w_gore(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_gore(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(20)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(5)
robak.pokaz_gdzie_jestes()
