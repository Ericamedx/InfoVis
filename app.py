# https://github.com/adilmoujahid/kaggle-talkingdata-visualization/blob/master/app.py
# ctrl + shift + b för att bygga py i Atom, gå sen in på hemsidan

# för att slippa bygga app.py varje gång skriv set FLASK_DEBUG=1 i kommandotolken
# set FLASK_APP = app.py "bestäm" vilken fil som ska köra flask, dock ska den välja app.py av sig själv
import pandas as pd

# flask skapar server
from flask import Flask
# pip install flask
from flask import render_template
# vi behöver få in geojson här

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/data") # data representation
def get_data():
    data = pd.read_csv('/data/glovalterrorismdb_0718dist.csv')
    # här får vi skapa variabler osv

if __name__ == "__main__": # skicka till "hemsidan"
    app.run(host='0.0.0.0', port=5000, debug=True)
