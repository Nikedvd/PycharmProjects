# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

oikea_kayttajatunnus = "python"
oikea_salasana = "rules"
yrityskerrat = 0

while True:
    kayttaja = input("Anna käyttäjätunnus: ")
    salasana = input("Anna Salasanasi: ")
    if kayttaja == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tunnuksesi ovat oikein, tervetuloa!")
        break
    else:
        yrityskerrat += 1
        if yrityskerrat >= 5:
            print("Pääsysi on evätty, yritä myöhemmin uudestaan. ")
            break
        else:
            print("Väärä käyttäjätunnus tai salasana, ole hyvä ja yritä uudelleen. ")