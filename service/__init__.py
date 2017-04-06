from flask import Flask, render_template

app = Flask(__name__, template_folder='../template', static_folder='../static')

from service.public import *


@app.route('/')
def index():
    from time import time
    return render_template("index.html")
