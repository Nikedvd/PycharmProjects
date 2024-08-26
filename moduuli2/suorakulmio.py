# Tehdään ohjelma, jossa kysytään suorakulmion kanta sekä korkeus
# Tämän jälkeen tulostetaan suorakulmion kanta sekä korkeus

import math

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna sitten korkeus: "))

pintaala = kanta * korkeus
piiri = kanta + kanta + korkeus + korkeus

print (f"Tällöin suorakulmion pinta-ala on {pintaala} neliömetriä  ja piiri on {piiri} metriä ")

