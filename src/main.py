import os
from flask import Flask, request
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

class server():

    def conect(self):
        conexao = pymysql.connect(
        host = 'sql10.freemysqlhosting.net',
        user = 'sql10343231',
        passwd = 'zdDyscJ4Fd',
        database= 'sql10343231'
        )
        return conexao

class On(Resource):
    def get(self):
        return {'status':'online'}

class Empresas(Resource):
    def get(self):
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute('SELECT nome FROM empresa')
        resultado = cursor.fetchall()
        re = [{'nome': str(i)} for i in resultado]

        return re

    def post(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        nome = dados['nome']
        endereco = dados['endereco']
        bairro = dados['bairro']
        numero = dados['numero']
        telefone = dados['telefone']
        cidade = dados['cidade']
        uf = dados['uf']
        dinheiro = dados['dinheiro']
        credito = dados['credito']
        debito = dados['debito']
        try:
            com_sql = "INSERT INTO empresa(usuario,senha,nome,endereco,numero,bairro,telefone,cidade,uf,dinheiro,credito,debito) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            valor = (usuario, senha, nome, endereco, numero, bairro, telefone , cidade, uf, dinheiro, credito, debito)
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute(com_sql, valor)
            c.commit()
            c.close()
            return {'status':'sucesso'}
        except AttributeError:
            return{
                'status':'error',
                'mensagem': AttributeError
            }

class Empresa_infos(Resource):
    def get(self, nome):
        try:
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute("SELECT senha FROM empresa WHERE usuario = '" + nome + "'")
            senha = cursor.fetchall()
            senha = str(senha)
            senha = senha.replace("(", "")
            senha = senha.replace(")", "")
            senha = senha.replace(",", "")
            senha = senha.replace("'", "")
            cursor.execute("SELECT usuario FROM empresa WHERE usuario = '" + nome + "'")
            user = cursor.fetchall()
            user = str(user)
            user = user.replace("(", "")
            user = user.replace(")", "")
            user = user.replace(",", "")
            user = user.replace("'", "")
            cursor.execute("SELECT nome FROM empresa WHERE usuario = '" + nome + "'")
            name = cursor.fetchall()
            name = str(name)
            name = name.replace("(", "")
            name = name.replace(")", "")
            name = name.replace(",", "")
            name = name.replace("'", "")
            cursor.execute("SELECT cidade FROM empresa WHERE usuario = '" + nome + "'")
            cit = cursor.fetchall()
            cit = str(cit)
            cit = cit.replace("(", "")
            cit = cit.replace(")", "")
            cit = cit.replace(",", "")
            cit = cit.replace("'", "")
            cursor.execute("SELECT numero FROM empresa WHERE usuario = '" + nome + "'")
            numero = cursor.fetchall()
            numero = str(numero)
            numero = numero.replace("(", "")
            numero = numero.replace(")", "")
            numero = numero.replace(",", "")
            numero = numero.replace("'", "")
            cursor.execute("SELECT endereco FROM empresa WHERE usuario = '" + nome + "'")
            endereco = cursor.fetchall()
            endereco = str(endereco)
            endereco = endereco.replace("(", "")
            endereco = endereco.replace(")", "")
            endereco = endereco.replace(",", "")
            endereco = endereco.replace("'", "")
            cursor.execute("SELECT bairro FROM empresa WHERE usuario = '" + nome + "'")
            bairro = cursor.fetchall()
            bairro = str(bairro)
            bairro = bairro.replace("(", "")
            bairro = bairro.replace(")", "")
            bairro = bairro.replace(",", "")
            bairro = bairro.replace("'", "")
            cursor.execute("SELECT telefone FROM empresa WHERE usuario = '" + nome + "'")
            telefone = cursor.fetchall()
            telefone = str(telefone)
            telefone = telefone.replace("(", "")
            telefone = telefone.replace(")", "")
            telefone = telefone.replace(",", "")
            telefone = telefone.replace("'", "")
            cursor.execute("SELECT uf FROM empresa WHERE usuario = '" + nome + "'")
            uf = cursor.fetchall()
            uf = str(uf)
            uf = uf.replace("(", "")
            uf = uf.replace(")", "")
            uf = uf.replace(",", "")
            uf = uf.replace("'", "")
            cursor.execute("SELECT credito FROM empresa WHERE usuario = '" + nome + "'")
            credito = cursor.fetchall()
            credito = str(credito)
            credito = credito.replace("(", "")
            credito = credito.replace(")", "")
            credito = credito.replace(",", "")
            credito = credito.replace("'", "")
            cursor.execute("SELECT debito FROM empresa WHERE usuario = '" + nome + "'")
            debito = cursor.fetchall()
            debito = str(debito)
            debito = debito.replace("(", "")
            debito = debito.replace(")", "")
            debito = debito.replace(",", "")
            debito = debito.replace("'", "")
            cursor.execute("SELECT dinheiro FROM empresa WHERE usuario = '" + nome + "'")
            dinheiro = cursor.fetchall()
            dinheiro = str(dinheiro)
            dinheiro = dinheiro.replace("(", "")
            dinheiro = dinheiro.replace(")", "")
            dinheiro = dinheiro.replace(",", "")
            dinheiro = dinheiro.replace("'", "")

            response = {
                'nome':name,
                'cidade':cit,
                'usuario':user,
                'senha':senha,
                'numero':numero,
                'endereco':endereco,
                'bairro':bairro,
                'telefone':telefone,
                'uf':uf,
                'credito':credito,
                'debito':debito,
                'dinheiro':dinheiro
            }
            return response
        except AttributeError:
            return{'status':'error','menssagem':AttributeError}
    #def put(self, nome):
        #empresa = Empresa.query.filter_by(nome=nome).first()
        #dados = request.json
       # try:
          #  empresa.nome = dados['nome']
         #   empresa.usuario = dados['usuario']
        #    empresa.senha = dados['senha']
       #     empresa.numero = dados['numero']
            #empresa.endereco = dados['endereco']
           # empresa.bairro = dados['bairro']
          #  empresa.telefone = dados['telefone']
         #   empresa.cidade = dados['cidade']
        #    empresa.uf = dados['uf']
       #     empresa.save()
      #      return {'status':'sucesso'}
     #   except AttributeError:
    #        return{'status':'error','mensagem':AttributeError}
   # def delete(self, nome):
      #  try:
     #       empresa = Empresa.query.filter_by(nome=nome).first()
    #        empresa.delete()
   #         return{'status':'sucesso'}
  #      except AttributeError:
 #           return{'status':'error','menssagem':AttributeError}

class Clientes_infos(Resource):
    def get(self, nome):
        try:
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute("SELECT senha FROM clientes WHERE usuario = '" + nome + "'")
            senha = cursor.fetchall()
            senha = str(senha)
            senha = senha.replace("(", "")
            senha = senha.replace(")", "")
            senha = senha.replace(",", "")
            senha = senha.replace("'", "")
            cursor.execute("SELECT usuario FROM clientes WHERE usuario = '" + nome + "'")
            user = cursor.fetchall()
            user = str(user)
            user = user.replace("(", "")
            user = user.replace(")", "")
            user = user.replace(",", "")
            user = user.replace("'", "")
            cursor.execute("SELECT nome FROM clientes WHERE usuario = '" + nome + "'")
            name = cursor.fetchall()
            name = str(name)
            name = name.replace("(", "")
            name = name.replace(")", "")
            name = name.replace(",", "")
            name = name.replace("'", "")
            cursor.execute("SELECT cidade FROM clientes WHERE usuario = '" + nome + "'")
            cit = cursor.fetchall()
            cit = str(cit)
            cit = cit.replace("(", "")
            cit = cit.replace(")", "")
            cit = cit.replace(",", "")
            cit = cit.replace("'", "")
            cursor.execute("SELECT numero FROM clientes WHERE usuario = '" + nome + "'")
            numero = cursor.fetchall()
            numero = str(numero)
            numero = numero.replace("(", "")
            numero = numero.replace(")", "")
            numero = numero.replace(",", "")
            numero = numero.replace("'", "")
            cursor.execute("SELECT endereco FROM clientes WHERE usuario = '" + nome + "'")
            endereco = cursor.fetchall()
            endereco = str(endereco)
            endereco = endereco.replace("(", "")
            endereco = endereco.replace(")", "")
            endereco = endereco.replace(",", "")
            endereco = endereco.replace("'", "")
            cursor.execute("SELECT bairro FROM clientes WHERE usuario = '" + nome + "'")
            bairro = cursor.fetchall()
            bairro = str(bairro)
            bairro = bairro.replace("(", "")
            bairro = bairro.replace(")", "")
            bairro = bairro.replace(",", "")
            bairro = bairro.replace("'", "")
            cursor.execute("SELECT telefone FROM clientes WHERE usuario = '" + nome + "'")
            telefone = cursor.fetchall()
            telefone = str(telefone)
            telefone = telefone.replace("(", "")
            telefone = telefone.replace(")", "")
            telefone = telefone.replace(",", "")
            telefone = telefone.replace("'", "")
            cursor.execute("SELECT uf FROM clientes WHERE usuario = '" + nome + "'")
            uf = cursor.fetchall()
            uf = str(uf)
            uf = uf.replace("(", "")
            uf = uf.replace(")", "")
            uf = uf.replace(",", "")
            uf = uf.replace("'", "")

            response = {
                'nome':name,
                'cidade':cit,
                'usuario':user,
                'senha':senha,
                'numero':numero,
                'endereco':endereco,
                'bairro':bairro,
                'telefone':telefone,
                'uf':uf,
            }
            return response
        except AttributeError:
            return{'status':'error','menssagem':AttributeError}

class Clientes(Resource):

    def post(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        nome = dados['nome']
        endereco = dados['endereco']
        bairro = dados['bairro']
        numero = dados['numero']
        telefone = dados['telefone']
        cidade = dados['cidade']
        uf = dados['uf']
        try:
            com_sql = "INSERT INTO clientes(usuario,senha,nome,endereco,numero,bairro,telefone,cidade,uf) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            valor = (usuario, senha, nome, endereco, numero, bairro, telefone, cidade, uf)
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute(com_sql, valor)
            c.commit()
            c.close()
            return {'status':'sucesso'}
        except AttributeError:
            return{
                'status':'error',
                'mensagem': AttributeError
            }

api.add_resource(On, '/')
api.add_resource(Empresa_infos, '/empresa/<string:nome>/')
api.add_resource(Empresas, '/empresas/')
api.add_resource(Clientes, '/clientes/')
api.add_resource(Clientes_infos, '/cliente/<string:nome>/')

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()