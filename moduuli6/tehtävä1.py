# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopan_heitto():
    return random.randint(1,6)

tulos = 0
while tulos !=6:
    tulos = nopan_heitto()
    print(tulos)