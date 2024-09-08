#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(numeroita):
    return sum(numeroita)



if __name__ == "__main__":
    numerolista = [3, 4, 9, 12, 15, 11]
    summa1 = summa(numerolista)
    print(f"Numerolistan {numerolista} numeroista summaksi saadaan {summa1} ")

