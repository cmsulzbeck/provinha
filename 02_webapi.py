from flask import Flask, jsonify
from flask.globals import request
from flask_restx import Resource, Api
from six import print_
from utils.csvToJson import csvToJson
from models.idlike import IdLike
import utils.sqlite_demo as sql
import pandas as pd
import os
import json
import sqlite3


# Inicialização Flask
app = Flask(__name__)
api = Api(app)

# Inicializando variável caminho
caminho = f"{os.getcwd()}\\bases"

# Inicializando Dataframes pandas
residencias = pd.read_csv(f"{caminho}\\residencias.csv")
media_preco = pd.read_csv(f"{caminho}\\media_preco.csv")

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Endpoint get de residencias
@api.route('/residencias')
class Residencias(Resource):
    def get(self):
       
        # Filtrando bases com parâmetro get passado por uri
        residencias_filtered = residencias[residencias.neighbourhood_group.isin([request.args.get('neighbourhood_group')])]
        
        # Base filtrada estava vindo com coluna 'Unnamed: 0' por algum motivo, por isso o drop da coluna
        residencias_filtered.drop('Unnamed: 0', axis='columns', inplace=True)
        # Drop da coluna 'neighbourhood_group' para geração correta de json
        residencias_filtered.drop('neighbourhood_group', axis='columns', inplace=True)

        # retornadno json na view da api
        return csvToJson(residencias_filtered)

    def post(self):
        data = request.get_json()
        print(data)

        # persistindo dados na tabela idlike do banco de dados provinha.db
        conn = sqlite3.connect('provinha.db')
        print('connecting to database')

        c = conn.cursor()
        print('creating cursor')

        # Inicializando objeto IdLike
        idlike = IdLike(data['id'], data['like'])
        print('associating idlike object')

        # Verificando se id já existe no banco de daods
        c.execute("SELECT * FROM idlike where id = :id", {'id': idlike.id})
        conn.commit()
        print('executing select')
        result_sql = c.fetchone()
        print('fetching results')
        
        if result_sql is not None:
            print('query failed')
            conn.close()
            return "Cannot insert into table, row already exists"
        else:
            print('query succesfull')
            c.execute("INSERT INTO idlike VALUES (:id, :like)", {'id': idlike.id, 'like': idlike.like})
            conn.commit()
            conn.close()
            return jsonify(data)

        
        # print(idlike.id)
        # print(idlike.like)

@api.route('/preco-medio')
class PrecoMedio(Resource):
    def get(self):

        # Filtrando bases com parâmetrto get passado por uri
        media_preco_filtered = media_preco[media_preco.neighbourhood_group.isin([request.args.get('neighbourhood_group')])]

        # Retornando json na View do endpoint
        return csvToJson(media_preco_filtered)

if __name__ == '__main__':
    app.run(debug=True)
