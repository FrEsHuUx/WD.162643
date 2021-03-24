class CiagArytemtyczny:
    pierwszy_wyraz = 0
    roznica = 0
    nty_wyraz = 0
    nty = 0.0
    liczba_elementow = 0

    def wyswietl_dane(self, pierwszy_wyraz, roznica, nty_wyraz):
        self.pierwszy_wyraz = pierwszy_wyraz
        self.roznica = roznica
        self.nty_wyraz = nty_wyraz
        print(('Pierwszy wyraz ciagu = %(z1)d \n'
               'roznica = %(z2)d  \n'
               'nty_wyraz = %(z3)d \n'
               % {'z1': self.pierwszy_wyraz, 'z2': self.roznica, 'z3': self.nty_wyraz}))

    def pobierz_parametry(self):
        print("Podaj parametry ")
        self.pierwszy_wyraz = int(input("Pierwszy element ciagu: "))
        self.roznica = int(input("Roznica ciagu: "))
        self.nty_wyraz = int(input("Nty wyraz ciagu: "))

    def policz_sume(self):
        ciag.pobierz_parametry()
        nty = self.pierwszy_wyraz + (self.nty_wyraz - 1) * self.roznica
        suma = ((self.pierwszy_wyraz + nty) * self.nty_wyraz) / 2
        return print("Suma wynosi", suma)

    def policz_elementy(self):
        ciag.pobierz_parametry()
        self.liczba_elementow = ((self.nty_wyraz - self.pierwszy_wyraz) / self.roznica) + 1
        return print("Liczba elementow wynosi = ", self.liczba_elementow)


ciag = CiagArytemtyczny()
ciag.wyswietl_dane(15, 10, 5)
ciag.pobierz_parametry()
ciag.policz_sume()
ciag.policz_elementy()
