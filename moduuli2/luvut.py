# Tehdään ohjelma, joka kysyy kolme kokonaislukua.
# Tämän jälkeen ohjelma tulostaa niiden summan, tulon ja keskiarvon

import math

eka = float(input("Anna ensimmäinen kokonaisluku: "))
toka = float(input("Anna toinen kokonaisluku: "))
kolme = float(input("Anna kolmas kokonaisluku: "))

summa = eka + toka + kolme
tulo = eka * toka * kolme
keskiarvo = (eka + toka + kolme)/3

print (f"Näiden lukujen summa olisi {summa}, tulo olisi {tulo} ja keskiarvo olisi {keskiarvo}")

