# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poisto_ohjelma(lukulista):
    parillinen_luku = [luku for luku in lukulista if luku % 2 == 0]
    return parillinen_luku

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    paritonlista = poisto_ohjelma(lista)
    print(f"Normaali lista lista on: {lista}")
    print(f"Pelkästään parillisia sisältävä lista on: {paritonlista}")