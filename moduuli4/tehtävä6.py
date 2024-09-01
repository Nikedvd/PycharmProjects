# π ≈ 4n/N, jossa N on kaikkien pisteiden lukumäärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
# jos pisteen koordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä

import random
import math
from collections.abc import Iterator

N = int(input("Montako pistettä haluat?: "))
n = 0 # Pisteet jotka osuvat ympyrään
iterator = 0
while iterator < N:
    n += 1
    iterator += 1
    # arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    print(x**2+ y**2 < 1)
    if x**2+ y**2 < 1:
        print("Piste on yksikköympyrässä. ")
    pii = (4*n/N)
    print(f"Piin likiarvo on {pii}")
