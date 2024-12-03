# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response, render_template
import json
import alkulukulaskuri


app = Flask(__name__)


@app.route("/")
def moikka():
    return "Alkulukujutska"

@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)
        alkuluku = alkulukulaskuri.laske(luku)

        tilakoodi = 200


        vastaus = {
            "Number": luku,
            "isPrime": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku, alkulukua ei voida laskea."
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    #return Response(response=jsonvast, status=404, mimetype="application/json")
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)