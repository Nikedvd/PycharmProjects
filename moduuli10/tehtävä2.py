# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, kerrosvaihto):
        while self.kerros > kerrosvaihto:
            self.kerros_alas()

        while self.kerros < kerrosvaihto:
            self.kerros_ylös()

        if self.kerros == kerrosvaihto:
            print(f"\nHissi on nyt kerroksessa {self.kerros}")

    def kerros_ylös(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1
            print(f"\nHissi on mennyt ylöspäin ja on nyt kerroksessa {self.kerros}")


    def kerros_alas(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1
            print(f"\nHissi on mennyt alaspäin ja on nyt kerroksessa {self.kerros}")



class Talo:
    def __init__(self, alinkerros, ylinkerros, hissien_lukumaara):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = [Hissi(alinkerros, ylinkerros) for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)


# Pääohjelma
talo = Talo(0, 5, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 0)
