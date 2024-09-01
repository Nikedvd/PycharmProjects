# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvoluku = random.randint(1, 10)

while True:
    arvuutus = int(input("Kone on valinnut luvun väliltä 1-10, arvaa mikä se on!: "))
    if arvuutus == arvoluku:
        print("Arvaus on oikein. Onneksi olkoon!")
        break
    if arvuutus < arvoluku:
        print("Arvauksesi on liian pieni.")
    if arvuutus > arvoluku:
        print("Arvauksesi on liian suuri.")
