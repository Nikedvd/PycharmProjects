# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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
        self.kerros += 1
        print(f"\nHissi on mennyt ylöspäin ja on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"\nHissi on mennyt alaspäin ja on nyt kerroksessa {self.kerros}")


hissi = Hissi(0, 5)
hissi.siirry_kerrokseen(4)
hissi.siirry_kerrokseen(1)
