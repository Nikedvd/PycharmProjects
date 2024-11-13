# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import json
import requests


city = input(f"Anna kaupungin nimi: ")
API_KEY = "02cc09dee8da7c9fa5feff38cda004b1"
kaantaja = "&units=metric&lang=FI"
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def getweather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}{kaantaja}"
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Verkkovirhe!")
        return

    # testataan, että http status koodi OK, muuten lopetetaan suoritus tähän.
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return


    print(print(json.dumps(response_body, indent=2)))
    lämpötila = response_body["main"]["temp"]
    print(f"Lämpötila paikassa {city} on nyt {lämpötila} astetta")
    kuvaus = response_body["weather"][0]["main"]
    print(f"Sään kuvaus on {kuvaus}")

getweather()
