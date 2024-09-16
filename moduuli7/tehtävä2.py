# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

def nimikysyja():
    nimilista = set()

    while True:
        nimi = input("Syötä haluamasi nimi: ")
        if nimi == "":
            break
        elif nimi in nimilista:
            print("Tämä nimi on aiemmin syötetty")
        else:
            print("Uusi nimi havaittu")
            nimilista.add(nimi)

    print("Ohjelmaan syötetyt nimet: ")
    for nimi in nimilista:
        print(nimi)

nimikysyja()
