from flask import *
import random
import json
import os
from myfunctions import *

app = Flask(__name__)

users_general_list = load_users_general_list()


@app.route("/")
def index():
    return render_template("index.html")





if __name__ == '__main__':
    app.run()