# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.

user_input = input("Minkä tarjolla olevista hyttivaihtoehdoista haluat? LUX, A, B vai C?: ")
if user_input == "LUX":
    print("Hyvä valinta, LUX on parvekkeellinen hytti yläkännella.")
elif user_input == "A":
    print("Hyvä valinta, A on ikkunallinen hytti autokannan yläpuolella.")
elif user_input == "B":
    print("Hyvä valinta, B on ikkunaton hytti autokannen yläpuolella.")
elif user_input == "C":
    print("Hyvä budjetillinen valinta, C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka. Yritä uudestaan. ")