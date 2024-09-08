# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lukujono = []

user_input = input("Syötä luku: ")
while user_input!="":
    kokonaisluku = int(user_input)
    lukujono.append(kokonaisluku)
    lukujono.sort(reverse=True)
    user_input = input("Jatka syöttämällä luku tai lopeta painamlla enter: ")

print(lukujono[:5])

