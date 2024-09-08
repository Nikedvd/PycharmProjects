# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def nopan_heitto(tahkot):
    return random.randint(1,tahkot)

tahkojen_yhteismaara = int(input("Anna tahkojen määrä: "))


tulos = 0
while tulos !=tahkojen_yhteismaara:
    tulos = nopan_heitto(tahkojen_yhteismaara)
    print(tulos)