from flask import Flask, render_template
from functions import *
from db import sayyoralar

app = Flask(__name__)

@app.route("/")
def index():
    sayyoralar_ = sayyoralar_ruyhati(sayyoralar)
    return render_template("index.html", sayyoralar=sayyoralar_)

app.run(debug=True)