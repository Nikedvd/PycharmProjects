# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def is_alkuluku(num):
    # Ei testata nollaa tai negatiivisia lukuja ollenkaan
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            # Jos jaollinen jollakin 1:n arvolla, palautetaan false
            # jolloin funktion suoritus loppuu silloin siihen
            return False
    # Jos funktio suoritus kuitenkin on jatkunut tänne asti niin palautetaan True
    return True

# Lukee syötteen ja tulostaa vastauksen sen jälkeen
testiluku = int(input("Anna KOKONAISluku jota testataan (>O): "))

if is_alkuluku(testiluku):
    print(f"Luku {testiluku} on alkuluku.")
else:
    print(f"Luku {testiluku} ei ole alkuluku.")

