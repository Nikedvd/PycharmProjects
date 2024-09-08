# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def gallon_litraksi(gallonat):
    return gallonat * 3.785


while True:
    gallonat = float(input("Anna gallonamäärä jonka haluat muuntaa: "))
    if gallonat < 0:
        print("Virheellinen määrä, syötä positiivinen luku.")
        break
    if gallonat > 0:
        bensalitra = gallon_litraksi(gallonat)
        print(f"Antamasi määrä {gallonat} gallonaa on litroissa mitattuna {bensalitra:2f} litraa. ")

