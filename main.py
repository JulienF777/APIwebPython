from flask import Flask

#flask --ap main run --debug
#demarre le serveur

app = Flask(__name__)

#une route en get pour récupérer les produits, une route post pour en ajouter etc...

@app.route("/test/<name>", methods=['GET', 'POST'])
def hello_world(name):
    return name



