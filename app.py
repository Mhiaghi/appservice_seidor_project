#Librerias

from flask import Flask, render_template, redirect, url_for, flash, request, session, g, jsonify
from flask_cors import CORS, cross_origin
import json
import pymysql
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import base64
import io
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
    return "Prueba con http://127.0.0.1:5000/datos?dispositivo=T03"

@app.route("/datos")
def show_data():
    #http://127.0.0.1:5000/datos?dispositivo=T03
    param = request.args.get('dispositivo', 'Nulo')
    if param != "No existente":
        cnx = pymysql.connect(
            user = "Mhiaghi",
            password = 'Miguel123',
            host = 'msaturno-database.mysql.database.azure.com',
            port = 3306,
            database = 'SEIDORLAB'
            )
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM devices WHERE Codigo = '%s'" % (param))
        valores = cursor.fetchall()
        if valores != (): 
            cursor.execute("SELECT fecha_entrada FROM devices WHERE Codigo = '%s'" % (param))
            fechas = cursor.fetchall()
            cursor.execute("SELECT valor FROM devices WHERE Codigo = '%s'" % (param))
            datos = cursor.fetchall()
            fig = Figure(figsize=(12,7))
            ax = fig.subplots()
            #fecha_salida = now.strftime("%Y-%m-%d %H:%M:%S")
            fechas2 = []
            for i in range(len(fechas)):
                #now = now - timedelta(hours= 5)
                fechas2.append((fechas[i][0] -timedelta(hours=5)).strftime("%H:%M:%S"))

            ax.plot(fechas2,datos)

            ax.set_title("Valores de %s del dispositivo %s" %(valores[0][0], valores[0][1]))
            ax.set_xlabel('Tiempo')
            ax.set_ylabel('Valor en %s'%(valores[0][3]))
            buf = io.BytesIO()
            fig.savefig(buf, format = "png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii") 
            delay = timedelta(seconds=0)
            for i in range(len(valores)):
                delay = delay + valores[i][5] - (valores[i][4] - timedelta(hours=5))
            delay = (delay/len(valores))
            print(fechas2)
            return f"<img src = 'data:image/png;base64,{data}'/><br><p>Tiempo promedio delay: {delay} segundos</p>"

        else:
            return "No hay valores con {}".format(param)
        return 'El dispositivo es {}'.format(param)
    return 'El dispositivo no existe'

@app.route("/funciones", methods = ["POST", "GET"])
def get_data_from_functions():

    return "XD"

if __name__ == '__main__':
    app.run()