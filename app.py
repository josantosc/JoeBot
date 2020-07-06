import json
import pymysql
from flask import Flask
from flask import request
import random

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    #Conecanto com o banco
    #conexao = pymysql.connect(host='localhost',
     #                         user='root',
     #                         password='chatbot123',
     #                         db='dbchatbot',
     #                         charset='utf8mb4',
     #                         cursorclass=pymysql.cursors.DictCursor)


    #obtendo estrutura do arquivo Json
    data = request.get_json(silent=True)
    intent = data['queryResult']['intent']['displayName']
    nomePaciente = data['queryResult']['outputContexts'][0]['parameters']['nome.original']

    if (intent == '2-apresentacao.nome'):
        resposta = dict(
                fulfillmentText="Responsta do back-end")

    return json.dumps(resposta)
#def processRequest(req):
    #result = req.get('queryResult')
    #intent = result.get('intent').get('displayName')
    #outputContexts = result.get('outputContexts')
    #parameters = result.get('parameters')
    #nomePaciente = parameters.get('nome.original')
    #tcc_sim_nao = parameters.get('tcc_sim_nao.original')
    #mora = parameters.get('residencia.original')


if __name__ == "__main__":
    app.run(debug=True)
