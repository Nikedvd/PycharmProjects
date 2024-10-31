# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.atm_nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettum = 0

    def auton_tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}")
        print(f"Auton huippunopeus on {self.huippunopeus} km/h")
        print(f"Auton tämänhetkinen nopeus on {self.atm_nopeus} km/h")
        print(f"Auton kuljettu matka on {self.kuljettum} km")

    def kiihdyta(self, nopeuden_muutos):
        self.atm_nopeus = self.atm_nopeus + nopeuden_muutos
        if self.atm_nopeus > self.huippunopeus:
            self.atm_nopeus = self.huippunopeus
        if self.atm_nopeus < 0:
            self.atm_nopeus = 0


auto1 = Auto("ABC-123", 142)
auto1.auton_tiedot()
print(f"\nAuto lähtee kiihdyttämään")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus on {auto1.atm_nopeus}")
print(f"\nAuto tekee hätäjarrutuksen")
auto1.kiihdyta(-200)
print(f"\nAuton nopeus jarrutuksen jälkeen on {auto1.atm_nopeus}")
