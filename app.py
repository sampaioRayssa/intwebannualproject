from flask import *
import random
import json
import os
from myfunctions import *

app = Flask(__name__)

users_general_list = users_general_list()


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/cliente')
def cliente():
    return "Coming soon"

@app.route('/entregador')
def cliente():
    return "Coming soon"



if __name__ == '__main__':
    app.run()