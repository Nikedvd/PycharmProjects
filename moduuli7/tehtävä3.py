# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

import mysql.connector

connection = mysql.connector.connect(
                host='127.0.0.1', # localhost
                port=3306,
                database='flight_game',
                user='nikedw',
                password='sad22',
                autocommit=True,
                collation='utf8mb4_general_ci'
                )


def ohjelmat():
    lentoasematlista = {}

    while True:
        print("Valitse jokin seuraavista toiminnoista jatkaaksesi:")
        print("1. Syötä uusi lentoasema: ")
        print("2. Hae haluamasi lentoaseman tiedot: ")
        print("3. Lopeta ohjelma.")
        valinta = input("Syötä valintasi 1, 2 tai 3: ")

        if valinta == '1':
            icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
            nimi = input("Syötä lentoaseman nimi: ")
            lentoasematlista[icao] = nimi
            print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

        elif valinta == '2':
            icao = input("Syötä haettavan lentoaseman ICAO-koodi: ")
            if icao in lentoasematlista:
                print(f"Hakemasi lentoaseman nimi on: {lentoasematlista[icao]}")
            else:
                print(f"Lentoasemaa tällä ICAO: {icao} koodilla ei löydy.")

        elif valinta == '3':
            print("Nyt ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta. Yritä uudelleen.")


if __name__ == "__main__":
    ohjelmat()