# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

numbers = 1000
number_counter = 0
while number_counter < numbers:
    if numbers % 3 == 0:
        print(numbers)