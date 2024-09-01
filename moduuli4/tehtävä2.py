# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
while True:
    tuuma = float(input(f"Anna tuumien määrä jotka haluat muuntaa: "))
    if tuuma <= -1:
        break

    sentit = tuuma * 2.54
    if tuuma >= 0:
        print(f" [{tuuma} tuuma(a) on {sentit} senttimetriä")

