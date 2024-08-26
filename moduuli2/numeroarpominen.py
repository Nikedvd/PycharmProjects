# Tehdään ohjelma, joka arpoo ja tulostaa kolminumeroisen numerolukon koodin väliltä 0-9
# Sekä nelinumeroisen koodin joiden numeromerkit on 1-6 väliltä

import math
import random

random_numbera = random.randint(0, 9)
random_numberb = random.randint(0, 9)
random_numberc = random.randint(0, 9)

print(f"Kolminumeroinen numerolukkosi koodi on: {random_numbera}, {random_numberb}, {random_numberc}")

random_numberd = random.randint(1, 6)
random_numbere = random.randint(1, 6)
random_numberf = random.randint(1, 6)
random_numberg = random.randint(1, 6)

print(f"Nelinumeroisen numerolukkosi koodi on: {random_numberd}, {random_numbere}, {random_numberf}, {random_numberg}")