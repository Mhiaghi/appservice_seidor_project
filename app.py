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
    return "Test Seidor"


if __name__ == '__main__':
    app.run()