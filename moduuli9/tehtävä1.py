# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.




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

auto1 = Auto("ABC-123", 142)
auto1.auton_tiedot()








