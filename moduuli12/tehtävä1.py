# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests


def chuck_vitsit():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        vitsit = response.json()
        return vitsit['value']
    else:
        return "Vitsiä ei saatu haettua."


vitsi = chuck_vitsit()
print(f"\n{vitsi}")


