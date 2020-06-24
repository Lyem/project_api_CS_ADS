import os
from flask import Flask, request
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

class server():

    def conect(self):
        conexao = pymysql.connect(
            host='',
            user='',
            passwd='',
            database=''
        )
        return conexao

class On(Resource):
    def get(self):
        return {'status':'online'}

class LoginC(Resource):
    def post(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("select count(*) from clientes where usuario ='"+ usuario +"' and senha ='"+ senha +"'")
        v = cursor.fetchall()
        v = str(v)
        v = v.replace("(", "")
        v = v.replace(")", "")
        v = v.replace(",", "")
        v = v.replace("'", "")
        if (v == "1"):
            return {'status':'sim'}
        else:
            return {'status':'nao'}

class EmpresaPostandPut(Resource):
    def post(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("select count(*) from empresa where usuario ='" + usuario + "' and senha ='" + senha + "'")
        v = cursor.fetchall()
        v = str(v)
        v = v.replace("(", "")
        v = v.replace(")", "")
        v = v.replace(",", "")
        v = v.replace("'", "")
        if (v == "1"):
            cursor.execute("SELECT nome FROM empresa WHERE usuario = '" + usuario + "'")
            name = cursor.fetchall()
            name = str(name)
            name = name.replace("(", "")
            name = name.replace(")", "")
            name = name.replace(",", "")
            name = name.replace("'", "")
            cursor.execute("SELECT cidade FROM empresa WHERE usuario = '" + usuario + "'")
            cit = cursor.fetchall()
            cit = str(cit)
            cit = cit.replace("(", "")
            cit = cit.replace(")", "")
            cit = cit.replace(",", "")
            cit = cit.replace("'", "")
            cursor.execute("SELECT numero FROM empresa WHERE usuario = '" + usuario + "'")
            numero = cursor.fetchall()
            numero = str(numero)
            numero = numero.replace("(", "")
            numero = numero.replace(")", "")
            numero = numero.replace(",", "")
            numero = numero.replace("'", "")
            cursor.execute("SELECT endereco FROM empresa WHERE usuario = '" + usuario + "'")
            endereco = cursor.fetchall()
            endereco = str(endereco)
            endereco = endereco.replace("(", "")
            endereco = endereco.replace(")", "")
            endereco = endereco.replace(",", "")
            endereco = endereco.replace("'", "")
            cursor.execute("SELECT bairro FROM empresa WHERE usuario = '" + usuario + "'")
            bairro = cursor.fetchall()
            bairro = str(bairro)
            bairro = bairro.replace("(", "")
            bairro = bairro.replace(")", "")
            bairro = bairro.replace(",", "")
            bairro = bairro.replace("'", "")
            cursor.execute("SELECT telefone FROM empresa WHERE usuario = '" + usuario + "'")
            telefone = cursor.fetchall()
            telefone = str(telefone)
            telefone = telefone.replace("(", "")
            telefone = telefone.replace(")", "")
            telefone = telefone.replace(",", "")
            telefone = telefone.replace("'", "")
            cursor.execute("SELECT uf FROM empresa WHERE usuario = '" + usuario + "'")
            uf = cursor.fetchall()
            uf = str(uf)
            uf = uf.replace("(", "")
            uf = uf.replace(")", "")
            uf = uf.replace(",", "")
            uf = uf.replace("'", "")
            cursor.execute("SELECT credito FROM empresa WHERE usuario = '" + usuario + "'")
            credito = cursor.fetchall()
            credito = str(credito)
            credito = credito.replace("(", "")
            credito = credito.replace(")", "")
            credito = credito.replace(",", "")
            credito = credito.replace("'", "")
            cursor.execute("SELECT debito FROM empresa WHERE usuario = '" + usuario + "'")
            debito = cursor.fetchall()
            debito = str(debito)
            debito = debito.replace("(", "")
            debito = debito.replace(")", "")
            debito = debito.replace(",", "")
            debito = debito.replace("'", "")
            cursor.execute("SELECT dinheiro FROM empresa WHERE usuario = '" + usuario + "'")
            dinheiro = cursor.fetchall()
            dinheiro = str(dinheiro)
            dinheiro = dinheiro.replace("(", "")
            dinheiro = dinheiro.replace(")", "")
            dinheiro = dinheiro.replace(",", "")
            dinheiro = dinheiro.replace("'", "")
            cursor.execute("SELECT usuario FROM empresa WHERE usuario = '" + usuario + "'")
            user = cursor.fetchall()
            user = str(user)
            user = user.replace("(", "")
            user = user.replace(")", "")
            user = user.replace(",", "")
            user = user.replace("'", "")
            response = {
                'nome': name,
                'cidade': cit,
                'numero': numero,
                'endereco': endereco,
                'bairro': bairro,
                'telefone': telefone,
                'uf': uf,
                'credito': credito,
                'usuario': user,
                'debito': debito,
                'dinheiro': dinheiro,
                'status': 'sim'
            }
            return response
        else:
            return {'status':'nao'}
    def put(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        usuariov = dados['uv']
        senhav = dados['sv']
        nome = dados['nome']
        numero = dados['numero']
        endereco = dados['endereco']
        bairro = dados['bairro']
        telefone = dados['telefone']
        cidade = dados['cidade']
        uf = dados['uf']
        credito = dados['credito']
        debito = dados['debito']
        dinheiro = dados['dinheiro']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("UPDATE empresa SET usuario = '"+ usuario +"', senha = '"+ senha +"', nome = '"+ nome +"', numero = '"+ numero +"', endereco = '"+ endereco +"', bairro = '"+ bairro +"', telefone = '"+ telefone +"', cidade = '"+ cidade +"', uf = '"+ uf +"', credito = '"+ credito +"', debito = '"+ debito +"', dinheiro = '"+ dinheiro +"' WHERE usuario ='"+usuariov+"' and senha ='"+senhav+"'")
        c.commit()
        c.close()
        return {'status': 'sucesso'}

class Empresas(Resource):
    def get(self, i=None):
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute('SELECT nome FROM empresa')
        resultado = cursor.fetchall()
        #re = [{'nome': str(i)} for i in resultado]
        v = str(resultado)
        v = v.replace("(", "")
        v = v.replace(")", "")
        v = v.replace(",", "")
        v = v.replace("'", "")
        return v

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
api.add_resource(EmpresaPostandPut, '/empresaget/')
api.add_resource(LoginC, '/cliente/login/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()