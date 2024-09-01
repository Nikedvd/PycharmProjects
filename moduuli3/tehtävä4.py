# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku: "))
if vuosi % 400 == 0 or (vuosi % 4 == 0 and not vuosi % 100 == 0):
    print("Tämä vuosi on karkausvuosi. ")
else:
    print("Tämä vuosi ei ole karkausvuosi. ")