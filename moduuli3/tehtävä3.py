# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Hei, oletko biologisesti mies vai nainen?: ")
globiini = int(input("Ja mikä on hemoglobiiniarvosi?: "))
if sukupuoli == "mies" and globiini < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "mies" and  134 <= globiini < 196:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies" and globiini >= 196:
    print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "nainen" and globiini < 117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "nainen" and  117 <= globiini < 176:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "nainen" and globiini >= 176:
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Syötä kelvollinen sukupuoli. ")

