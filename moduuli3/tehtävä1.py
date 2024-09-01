# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

import math


pituus = int(input("Mikä on kuhan pituus senttimetreissä?: "))
kuha = 37
if pituus >= 37:
    print(f"Kuha on sallitussa pyyntimitassa, hyvä!")
else:
    print(f"Kuha ei ole sallitussa pyyntimitassa, siitä puuttuu {kuha - pituus} senttiä. Laske kuha takaisin veteen ja yritä uudestaan. ")