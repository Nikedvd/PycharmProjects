# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.atm_nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettum = 0

    def auton_tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}")
        print(f"Auton huippunopeus on {self.huippunopeus} km/h")
        print(f"Auton nopeus on {self.atm_nopeus} km/h")
        print(f"Auton kuljettu matka on {self.kuljettum} km")

    def aseta_nopeus(self, nopeus):
        if 0 <= nopeus <= self.huippunopeus:
            self.atm_nopeus = nopeus
        else:
            print("Virhe: Nopeus ylittää huippunopeuden tai on negatiivinen.")

    def aja(self, tuntia):
        self.kuljettum += self.atm_nopeus * tuntia


class Sahko(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def auton_tiedot(self):
        super().auton_tiedot()
        print(f"\nSähköauton akkukapasiteetti on {self.akkukapasiteetti} kWh\n")


class Polttomoottori(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

    def auton_tiedot(self):
        super().auton_tiedot()
        print(f"\nPolttomoottorilla toimivan auton bensatankin koko on {self.bensatankin_koko} l")


# Pääohjelma
if __name__ == "__main__":
    sahko = Sahko("ABC-15", 180, 52.5)
    polttomoottori = Polttomoottori("ACD-123", 165, 32.3)

    sahko.aseta_nopeus(154)
    polttomoottori.aseta_nopeus(160)

    sahko.aja(8)
    polttomoottori.aja(11)

    sahko.auton_tiedot()
    polttomoottori.auton_tiedot()