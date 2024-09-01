# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
max_num = min_num = int(input("Syötä luku: "))
while True:
    input_string = input("Syötä luku: ")
    if input_string == "":
        break
    number = int(input_string)
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f"Pienin numero on {min_num} , suurin numero on {max_num}")