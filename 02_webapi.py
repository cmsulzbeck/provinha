from flask import Flask, jsonify
from flask.globals import request
from flask_restx import Resource, Api
from utils.csvToJson import csvToJson
from models.idlike import IdLike
import pandas as pd
import os
import sqlite3


# Inicialização Flask
app = Flask(__name__)
api = Api(app)

# Inicializando variável caminho
caminho = f"{os.getcwd()}\\bases"

# Inicializando Dataframes pandas
residencias = pd.read_csv(f"{caminho}\\residencias.csv")
media_preco = pd.read_csv(f"{caminho}\\media_preco.csv")

@api.route('/residencias')
class Residencias(Resource):
    # Endpoint get de residencias
    def get(self):
       
        # Filtrando bases com parâmetro get passado por uri
        residencias_filtered = residencias[residencias.neighbourhood_group.isin([request.args.get('neighbourhood_group')])]
        
        # Base filtrada estava vindo com coluna 'Unnamed: 0' por algum motivo, por isso o drop da coluna
        residencias_filtered.drop('Unnamed: 0', axis='columns', inplace=True)
        # Drop da coluna 'neighbourhood_group' para geração correta de json
        residencias_filtered.drop('neighbourhood_group', axis='columns', inplace=True)

        # retornadno json na view da api
        return csvToJson(residencias_filtered)

    # Endpoint post de residencias
    def post(self):
        # Recebendo json do corpo da requisição
        data = request.get_json()

        # persistindo dados na tabela idlike do banco de dados provinha.db
        # Abrindo conexão com banco de dados
        conn = sqlite3.connect('provinha.db')

        # Inicializando cursor para execução de comandos
        c = conn.cursor()

        # Inicializando objeto IdLike
        idlike = IdLike(data['id'], data['like'])

        # Verificando se id já existe no banco de daods
        c.execute("SELECT * FROM idlike where id = :id", {'id': idlike.id})
        conn.commit()
        
        # Armazenando resultado do select para verificação de existência de registro
        result_sql = c.fetchone()
        
        # Verificando existência de registro no banco de dados
        if result_sql is not None:
            conn.close()
            return "Cannot insert into table, row already exists"
        else:
            c.execute("INSERT INTO idlike VALUES (:id, :like)", {'id': idlike.id, 'like': idlike.like})
            conn.commit()
            conn.close()
            return jsonify(data)

@api.route('/preco-medio')
class PrecoMedio(Resource):
    # Endpoint get de preco-medio
    def get(self):

        # Filtrando bases com parâmetrto get passado por uri
        media_preco_filtered = media_preco[media_preco.neighbourhood_group.isin([request.args.get('neighbourhood_group')])]

        # Retornando json na View do endpoint
        return csvToJson(media_preco_filtered)

if __name__ == '__main__':
    app.run(debug=True)
