#Librerias

from flask import Flask, render_template, redirect, url_for, flash, request, session, g, jsonify
from flask_cors import CORS, cross_origin
import json
######################################################
#Database

######################################################
# Configuracion

from config import DevelopmentConfig
#######################################################
#Clases database

######################################################
#Blueprints


######################################################
app = Flask(__name__)
cors  = CORS(app,resources={r"/foo":{"origins":"*"}})
app.config.from_object(DevelopmentConfig)


######################################################
@app.route("/")
def index_page():
    return "Hello world"

@app.route("/datos")
def show_data():
    return "datos"

@app.route("/funciones", methods = ["POST", "GET"])
def get_data_from_functions():
    if request.method == "POST":
        content = request.json
        print(content)
        return content
    return "OK"

if __name__ == '__main__':
    app.run()