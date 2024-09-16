# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenaika = {12: "Talvi", 1: "Talvi", 2: "Talvi", 3:
    "Kevät",  4: "Kevät", 5: "Kevät", 6:
    "Kesä",  7: "Kesä", 8: "Kesä", 9:
    "Syksy", 10: "Syksy", 11: "Syksy"}


user_input = int(input("Anna kuukauden numero (1-12): "))
if 1 <= user_input <= 12:
    print(f"Syöttämäsi kuukausinumeron {user_input} vuoden aika on {vuodenaika[user_input]}")
else:
    print(f"Syötä kelvollinen kuukauden numero (väliltä 1-12)")
