# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupunkilista = []

for i in range(5):
    kaupunkinimi = input("Anna haluamasi kaupungin nimi: ")
    kaupunkilista.append(kaupunkinimi)
    print("Kertomasi kaupungit ovat: ")
    for kaupunkinimi in kaupunkilista:
        print(kaupunkinimi)

