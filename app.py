import json
import pymysql
from flask import Flask
from flask import request
import random

if __name__ == "__main__":
    def hello():
        #Conecanto com o banco
        #conexao = pymysql.connect(host='localhost',
                            #      user='root',
                            #      password='chatbot123',
                            #      db='dbchatbot',
                            #      charset='utf8mb4',
                             #     cursorclass=pymysql.cursors.DictCursor)
        if (intent == '2-apresentacao.nome'):
            nomePaciente = data['queryResult']['outputContexts'][0]['parameters']['nome.original']
            esposta = dict(fulfillmentText= nomePaciente)


        #obtendo estrutura do arquivo Json
        data = request.get_json(silent=True)
        intent = data['queryResult']['intent']['displayName']
        #result = data.get('queryResult')
        #intent = result.get('intent').get('displayName')
        if(intent == '2-apresentacao.nome'):

            try:
                with conexao.cursor() as cursor:
                    nomePaciente = data['queryResult']['outputContexts'][0]['parameters']['nome.original']
                    sql = "SELECT `nome` FROM `usuario` WHERE `nome`=%s"
                    cursor.execute(sql, (nomePaciente),)
                    result = cursor.fetchone()
                    if result is not None:
                        resposta = dict(fulfillmentText="Tudo bem %r, já estava com saudades! Agora me conta!"
                                                        "\n\nSó pra relembrar, voce ainda recordar o que é TCC?" % str(nomePaciente))
                    else:
                        sql = "insert into `usuario` (`id_us`, `nome`,`data`, `data_update`,`sexo`, `status`,`data_exp`)" \
                              "values (%r, %s, now(), null, null, null, null)"
                        matricula = random.randrange(1,100,5)
                        cursor.execute(sql, (matricula, nomePaciente))
                        resposta = dict(fulfillmentText="Oiii! %r \n\nUm..!!! temos novidades, ainda nao tinha visto você por aqui! \n\n"
                                                        "Para começarmos, vou me apresentar."
                                                        "\n\nMe chamo Wilna, sempre estou por aqui para conversar"
                                                        "\n\nMeu pai me criou para conversar com pessoas em tempos difíceis.\n"
                                                        "\n\nEu fui treinado em Terapia Comportamental Cognitiva(TCC). "
                                                        "\nVocê sabe o que é isso?"% str(nomePaciente))

                    conexao.commit()
            finally:
                conexao.close()

        elif(intent =='5-desenvolvimento-comportamento-humor'):
            defi_pensamento = data['queryResult']['outputContexts'][0]['parameters']['ops_personalidade']
            if (defi_pensamento == 'Pensamento'):
                resposta = dict(
                    fulfillmentText="Pensamento - Isso mesmo. O pensamento é um dos elementos mais fáceis de controlar. "
                                    "O outro elemento também fácil de controlar é o comportamento. "
                                    "Muitas pessoas se frustram porque querem controlar logo seus sentimentos, "
                                    "e isso é mais difícil.")


            elif (defi_pensamento == 'Sentimento'):
                resposta = dict(
                    fulfillmentText="Sentimento: Veja, o sentimento é o elemento menos fácil de controlar. "
                                    "Muitas pessoas se frustram porque querem controlar logo seus sentimentos. "
                                    "O pensamento e o comportamento são os elementos mais fáceis de controlar.")
            elif (defi_pensamento == 'Comportamento'):
                resposta = dict(
                    fulfillmentText="Comportamento - Isso mesmo. O comportamento é um dos elementos mais fáceis de controlar. "
                                    "O outro elemento fácil de controlar é o pensamento. "
                                    "Muitas pessoas se frustram porque querem controlar logo seus sentimentos, "
                                    "e isso é mais difícil.")

            elif (defi_pensamento == 'Não sei'):
                resposta = dict(
                    fulfillmentText="O pensamento e o comportamento são os elementos mais fáceis de controlar. "
                                    "Muitas pessoas se frustram porque querem controlar logo seus sentimentos, "
                                    "e isso é mais difícil.")









        return json.dumps(resposta)
    #def processRequest(req):
        #result = req.get('queryResult')
        #intent = result.get('intent').get('displayName')
        #outputContexts = result.get('outputContexts')
        #parameters = result.get('parameters')
        #nomePaciente = parameters.get('nome.original')
        #tcc_sim_nao = parameters.get('tcc_sim_nao.original')
        #mora = parameters.get('residencia.original')



