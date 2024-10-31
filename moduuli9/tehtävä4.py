# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.atm_nopeus = 0
        self.huippunopeus = huippunopeus
        self.kuljettum = 0

    def auton_tiedot(self):
        return f"Auton rekisteritunnus: {self.rekisteritunnus}, Auton huippunopeus, {self.huippunopeus} km/h, Auton tämän hetkinen nopeus:: {self.atm_nopeus} km/h,  Kuljettu matka: {self.kuljettum} km"

    def kiihdyta(self, nopeuden_muutos):
        self.atm_nopeus += nopeuden_muutos
        if self.atm_nopeus > self.huippunopeus:
            self.atm_nopeus = self.huippunopeus
        if self.atm_nopeus < 0:
            self.atm_nopeus = 0

    def kulje(self, tunti):
        self.kuljettum += self.atm_nopeus * tunti


def ohjelma():
    autot = []

    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu_kaynnissa = True
    while kilpailu_kaynnissa:
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

            if auto.kuljettum >= 10000:
                kilpailu_kaynnissa = False
                break

    print("Kilpailun tulokset:")
    print("Rekisteritunnus | Huippunopeus | Tämänhetkinen nopeus | Kuljettu matka")
    print("-" * 70)
    for auto in autot:
        print(auto.auton_tiedot())


if __name__ == "__main__":
    ohjelma()