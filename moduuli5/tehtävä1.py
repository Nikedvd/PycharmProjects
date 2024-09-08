# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
yhteis = 0
tulokset = []
kuutio_maara = int(input("Monta arpakuutiota heitetään?: "))
for i in range(kuutio_maara):
    tulos = random.randint(1,6)
    yhteis = yhteis + tulos
    tulokset.append(tulos)
print(f"Arpakuutioiden silmälukujen summa on yhteensä {yhteis}, noppien silmäluvut: {tulokset}")