# Kirjoitetaan ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

import math

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Selvitetään kuinka paljon nauloja on
naulatyht = leiviskat * 20 + naulat

# Selvitetään sen jälkeen luotien yhteismäärä
luodityht = naulatyht * 32 + luodit

# Lasketaan nyt grammoina, kun tiedämme luotien määrän.

grammatyht = luodityht * 13.3
print(grammatyht)

# Lisäksi on olemassa jakojäännösoperaatio (%), pelkän kokonaisosan palauttava jakolasku (//)

kg = int(grammatyht // 1000)
g = float(grammatyht % 1000)
print(f"Massaksi tulee siis: {kg} kiloagrammaa ja {g:.2f} grammaa")




