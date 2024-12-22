from ..app import app
from flask import Flask, render_template
import requests

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.route('/retrieve_wikidata/<string:id>', methods=['GET']) #Valeur par défaut
def retrieve_wikidata(id:str):
    url = 'https://www.wikidata.org/w/api.php'
    params = { #définition des paramètres
                'action': 'wbgetentities',
                'ids': id,
                'format': 'json',
                'languages': 'fr'
        }
 
    data = requests.get(url, params=params)
    content_type = data.headers['Content-Type']
    code_http = data.status_code
    data = data.json()

    if 'error' in data.keys():
        data = None

    return render_template('pages/wikidata.html', id=id, data=data, code_http=code_http, content_type=content_type)