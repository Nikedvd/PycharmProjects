# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.


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

    def kulje(self, tunti):
        self.kuljettum = self.atm_nopeus * tunti


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

auto1.kiihdyta(60)
print(f"\nAuton nopeus on {auto1.atm_nopeus}")


print(f"\nAuto lähtee matkaan ja kulkee 1,5 tuntia")
auto1.kulje(1.5)
print(f"Auton kuljettu matka on nyt {auto1.kuljettum}")



