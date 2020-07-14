import os
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)
api = Api(app)

class clear():

    def clear(conteudo):
        conteudo = str(conteudo)
        conteudo = conteudo.replace("(", "")
        conteudo = conteudo.replace(")", "")
        conteudo = conteudo.replace(",", "")
        conteudo = conteudo.replace("'", "")

        return conteudo

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
        v = clear.clear(v)
        if (v == "1"):
            cursor.execute("select id_clientes from clientes where usuario ='" + usuario + "' and senha ='" + senha + "'")
            id = cursor.fetchall()
            id = clear.clear(id)
            response = {
                'id': id,
                'status': 'sim'
            }
            return response
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
        v = clear.clear(v)
        if (v == "1"):
            cursor.execute("SELECT nome FROM empresa WHERE usuario = '" + usuario + "'")
            name = cursor.fetchall()
            name = clear.clear(name)
            cursor.execute("SELECT cidade FROM empresa WHERE usuario = '" + usuario + "'")
            cit = cursor.fetchall()
            cit = clear.clear(cit)
            cursor.execute("SELECT numero FROM empresa WHERE usuario = '" + usuario + "'")
            numero = cursor.fetchall()
            numero = clear.clear(numero)
            cursor.execute("SELECT endereco FROM empresa WHERE usuario = '" + usuario + "'")
            endereco = cursor.fetchall()
            endereco = clear.clear(endereco)
            cursor.execute("SELECT bairro FROM empresa WHERE usuario = '" + usuario + "'")
            bairro = cursor.fetchall()
            bairro = clear.clear(bairro)
            cursor.execute("SELECT telefone FROM empresa WHERE usuario = '" + usuario + "'")
            telefone = cursor.fetchall()
            telefone = clear.clear(telefone)
            cursor.execute("SELECT uf FROM empresa WHERE usuario = '" + usuario + "'")
            uf = cursor.fetchall()
            uf = clear.clear(uf)
            cursor.execute("SELECT credito FROM empresa WHERE usuario = '" + usuario + "'")
            credito = cursor.fetchall()
            credito = clear.clear(credito)
            cursor.execute("SELECT debito FROM empresa WHERE usuario = '" + usuario + "'")
            debito = cursor.fetchall()
            debito = clear.clear(debito)
            cursor.execute("SELECT dinheiro FROM empresa WHERE usuario = '" + usuario + "'")
            dinheiro = cursor.fetchall()
            dinheiro = clear.clear(dinheiro)
            cursor.execute("SELECT usuario FROM empresa WHERE usuario = '" + usuario + "'")
            user = cursor.fetchall()
            user = clear.clear(user)
            cursor.execute("SELECT hatendimentoi FROM empresa WHERE usuario = '" + usuario + "'")
            hatendimentoi = cursor.fetchall()
            hatendimentoi = clear.clear(hatendimentoi)
            cursor.execute("SELECT hatendimentof FROM empresa WHERE usuario = '" + usuario + "'")
            hatendimentof = cursor.fetchall()
            hatendimentof = clear.clear(hatendimentof)
            cursor.execute("SELECT segunda FROM empresa WHERE usuario = '" + usuario + "'")
            segunda = cursor.fetchall()
            segunda = clear.clear(segunda)
            cursor.execute("SELECT quinta FROM empresa WHERE usuario = '" + usuario + "'")
            quinta = cursor.fetchall()
            quinta = clear.clear(quinta)
            cursor.execute("SELECT domingo FROM empresa WHERE usuario = '" + usuario + "'")
            domingo = cursor.fetchall()
            domingo = clear.clear(domingo)
            cursor.execute("SELECT terca FROM empresa WHERE usuario = '" + usuario + "'")
            terca = cursor.fetchall()
            terca = clear.clear(terca)
            cursor.execute("SELECT sexta FROM empresa WHERE usuario = '" + usuario + "'")
            sexta = cursor.fetchall()
            sexta = clear.clear(sexta)
            cursor.execute("SELECT quarta FROM empresa WHERE usuario = '" + usuario + "'")
            quarta = cursor.fetchall()
            quarta = clear.clear(quarta)
            cursor.execute("SELECT sabado FROM empresa WHERE usuario = '" + usuario + "'")
            sabado = cursor.fetchall()
            sabado = clear.clear(sabado)
            cursor.execute("SELECT fsemanaabres FROM empresa WHERE usuario = '" + usuario + "'")
            fsemanaabres = cursor.fetchall()
            fsemanaabres = clear.clear(fsemanaabres)
            cursor.execute("SELECT fsemanafechas FROM empresa WHERE usuario = '" + usuario + "'")
            fsemanafechas = cursor.fetchall()
            fsemanafechas = clear.clear(fsemanafechas)
            cursor.execute("SELECT fsemanaabred FROM empresa WHERE usuario = '" + usuario + "'")
            fsemanaabred = cursor.fetchall()
            fsemanaabred = clear.clear(fsemanaabred)
            cursor.execute("SELECT fsemanafechad FROM empresa WHERE usuario = '" + usuario + "'")
            fsemanafechad = cursor.fetchall()
            fsemanafechad = clear.clear(fsemanafechad)
            cursor.execute("SELECT feriado FROM empresa WHERE usuario = '" + usuario + "'")
            feriado = cursor.fetchall()
            feriado = clear.clear(feriado)
            cursor.execute("SELECT feriadoa FROM empresa WHERE usuario = '" + usuario + "'")
            feriadoa = cursor.fetchall()
            feriadoa = clear.clear(feriadoa)
            cursor.execute("SELECT feriadof FROM empresa WHERE usuario = '" + usuario + "'")
            feriadof = cursor.fetchall()
            feriadof = clear.clear(feriadof)
            cursor.execute("SELECT id_empresa FROM empresa WHERE usuario = '" + usuario + "'")
            id = cursor.fetchall()
            id = clear.clear(id)

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
                'hatendimentoi': hatendimentoi,
                'hatendimentof': hatendimentof,
                'segunda': segunda,
                'quinta': quinta,
                'domingo': domingo,
                'terca': terca,
                'sexta': sexta,
                'quarta': quarta,
                'sabado': sabado,
                'fsemanaabres': fsemanaabres,
                'fsemanafechas': fsemanafechas,
                'fsemanaabred': fsemanaabred,
                'fsemanafechad': fsemanafechad,
                'feriado': feriado,
                'feriadoa': feriadoa,
                'feriadof': feriadof,
                'id': id,
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
        hatendimentoi = dados['hatendimentoi']
        hatendimentof = dados['hatendimentof']
        segunda = dados['segunda']
        quinta = dados['quinta']
        domingo = dados['domingo']
        terca = dados['terca']
        sexta = dados['sexta']
        quarta = dados['quarta']
        sabado = dados['sabado']
        fsemanaabres = dados['fsemanaabres']
        fsemanafechas = dados['fsemanafechas']
        fsemanaabred = dados['fsemanaabred']
        fsemanafechad = dados['fsemanafechad']
        feriado = dados['feriado']
        feriadoa = dados['feriadoa']
        feriadof = dados['feriadof']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("UPDATE empresa SET usuario = '"+ usuario +"', senha = '"+ senha +"', nome = '"+ nome +"', numero = '"+ numero +"', endereco = '"+ endereco +"', bairro = '"+ bairro +"', telefone = '"+ telefone +"', cidade = '"+ cidade +"', uf = '"+ uf +"', credito = '"+ credito +"', debito = '"+ debito +"', dinheiro = '"+ dinheiro +"', hatendimentoi = '"+hatendimentoi+"', hatendimentof = '"+hatendimentof+"', segunda = '"+segunda+"', quinta = '"+quinta+"', domingo = '"+domingo+"', terca = '"+terca+"', sexta = '"+sexta+"', quarta = '"+quarta+"', sabado = '"+sabado+"', fsemanaabres = '"+fsemanaabres+"', fsemanafechas = '"+fsemanafechas+"', fsemanaabred = '"+fsemanaabred+"', fsemanafechad = '"+fsemanafechad+"', feriado = '"+feriado+"', feriadoa = '"+feriadoa+"', feriadof = '"+feriadof+"' WHERE usuario ='"+usuariov+"' and senha ='"+senhav+"'")
        c.commit()
        c.close()
        return {'status': 'sucesso'}

class Empresas(Resource):
    def get(self, i=None):
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute('SELECT nome FROM empresa')
        resultado = cursor.fetchall()
        v = clear.clear(resultado)
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
        hatendimentoi = dados['hatendimentoi']
        hatendimentof = dados['hatendimentof']
        segunda = dados['segunda']
        quinta = dados['quinta']
        domingo = dados['domingo']
        terca = dados['terca']
        sexta = dados['sexta']
        quarta = dados['quarta']
        sabado = dados['sabado']
        fsemanaabres = dados['fsemanaabres']
        fsemanafechas = dados['fsemanafechas']
        fsemanaabred = dados['fsemanaabred']
        fsemanafechad = dados['fsemanafechad']
        feriado = dados['feriado']
        feriadoa = dados['feriadoa']
        feriadof = dados['feriadof']
        try:
            com_sql = "INSERT INTO empresa(usuario,senha,nome,endereco,numero,bairro,telefone,cidade,uf,dinheiro,credito,debito,hatendimentoi,hatendimentof,segunda,quinta,domingo,terca,sexta,quarta,sabado,fsemanaabres,fsemanafechas,fsemanaabred,fsemanafechad,feriado,feriadoa,feriadof) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            valor = (usuario, senha, nome, endereco, numero, bairro, telefone , cidade, uf, dinheiro, credito, debito, hatendimentoi, hatendimentof, segunda, quinta, domingo, terca, sexta, quarta, sabado, fsemanaabres, fsemanafechas, fsemanaabred, fsemanafechad, feriado, feriadoa, feriadof)
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
    def post(self):
        try:
            dados = request.json
            nome = dados['nome']
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute("SELECT nome FROM empresa WHERE nome = '" + nome + "'")
            name = cursor.fetchall()
            name = clear.clear(name)
            cursor.execute("SELECT cidade FROM empresa WHERE nome = '" + nome + "'")
            cit = cursor.fetchall()
            cit = clear.clear(cit)
            cursor.execute("SELECT numero FROM empresa WHERE nome = '" + nome + "'")
            numero = cursor.fetchall()
            numero = clear.clear(numero)
            cursor.execute("SELECT endereco FROM empresa WHERE nome = '" + nome + "'")
            endereco = cursor.fetchall()
            endereco = clear.clear(endereco)
            cursor.execute("SELECT bairro FROM empresa WHERE nome = '" + nome + "'")
            bairro = cursor.fetchall()
            bairro = clear.clear(bairro)
            cursor.execute("SELECT telefone FROM empresa WHERE nome = '" + nome + "'")
            telefone = cursor.fetchall()
            telefone = clear.clear(telefone)
            cursor.execute("SELECT uf FROM empresa WHERE nome = '" + nome + "'")
            uf = cursor.fetchall()
            uf = clear.clear(uf)
            cursor.execute("SELECT credito FROM empresa WHERE nome = '" + nome + "'")
            credito = cursor.fetchall()
            credito = clear.clear(credito)
            cursor.execute("SELECT debito FROM empresa WHERE nome = '" + nome + "'")
            debito = cursor.fetchall()
            debito = clear.clear(debito)
            cursor.execute("SELECT dinheiro FROM empresa WHERE nome = '" + nome + "'")
            dinheiro = cursor.fetchall()
            dinheiro = clear.clear(dinheiro)
            cursor.execute("SELECT id_empresa FROM empresa WHERE nome = '" + nome + "'")
            id = cursor.fetchall()
            id = clear.clear(id)


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
                'dinheiro':dinheiro,
                'id': id
            }
            return response
        except AttributeError:
            return{'status':'error','menssagem':AttributeError}

class ServicoGet(Resource):
    def post(self):
        dados = request.json
        id = dados['id']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("SELECT nome FROM servicos WHERE id_empresa = " + str(id) + "")
        nome = cursor.fetchall()
        nome = clear.clear(nome)
        cursor.execute("SELECT preco FROM servicos WHERE id_empresa = " + str(id) + "")
        preco = cursor.fetchall()
        preco = clear.clear(preco)
        cursor.execute("SELECT horario FROM servicos WHERE id_empresa = " + str(id) + "")
        horario = cursor.fetchall()
        horario = clear.clear(horario)
        cursor.execute("SELECT id_servicos FROM servicos WHERE id_empresa = " + str(id) + "")
        idd = cursor.fetchall()
        idd = clear.clear(idd)

        return {'nome': nome,'preco': preco,'horario': horario,'id': idd}

    def put(self):
        dados = request.json
        id = dados['id']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("SELECT nome FROM servicos WHERE id_servicos = " + str(id) + "")
        nome = cursor.fetchall()
        nome = clear.clear(nome)
        cursor.execute("SELECT preco FROM servicos WHERE id_servicos = " + str(id) + "")
        preco = cursor.fetchall()
        preco = clear.clear(preco)
        cursor.execute("SELECT horario FROM servicos WHERE id_servicos = " + str(id) + "")
        horario = cursor.fetchall()
        horario = clear.clear(horario)

        return {'nome': nome,'preco': preco,'horario': horario}
        pass

class Servicos(Resource):
    def post(self):
        dados = request.json
        nome = dados['nome']
        preco = dados['preco']
        horario = dados['horario']
        id_empresa = dados['id_empresa']

        try:
            com_sql = "INSERT INTO servicos(nome,preco,horario,id_empresa) VALUES (%s,%s,%s,%s)"
            valor = (nome, preco, horario, int(id_empresa))
            c = server.conect(self)
            cursor = c.cursor()
            cursor.execute(com_sql, valor)
            c.commit()
            c.close()
            return {'status': 'sucesso'}
        except AttributeError:
            return {
                'status': 'error',
                'mensagem': AttributeError
            }

    def put(self):
        dados = request.json
        nome = dados['nome']
        preco = dados['preco']
        horario = dados['horario']
        id_empresa = dados['id_empresa']
        id_servico = dados['id_servico']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("UPDATE servicos SET nome = '"+ nome +"', preco = '"+ preco +"', horario = '"+ horario+"' WHERE id_empresa = "+str(id_empresa)+" and id_servicos = "+str(id_servico)+"")
        c.commit()
        c.close()
        return {'status': 'sucesso'}

    def delete(self):
        dados = request.json
        id = dados['id']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("DELETE FROM servicos WHERE id_servicos = "+str(id)+"")
        c.commit()
        c.close()
        return {'status': 'sucesso'}


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

class Calendarioempresa(Resource):
    def post(self):
        dados = request.json
        usuario = dados['usuario']
        senha = dados['senha']
        idpessoal = dados['idpessoal']
        data = dados['data']
        c = server.conect(self)
        cursor = c.cursor()
        cursor.execute("select count(*) from empresa where usuario ='" + usuario + "' and senha ='" + senha + "'")
        v = cursor.fetchall()
        v = clear.clear(v)
        if (v == "1"):
            data = datetime.strptime(data, '%d/%m/%Y').date()
            cursor.execute("SELECT clientes.nome FROM clientes INNER JOIN pedido ON clientes.id_clientes = pedido.id_clientes INNER JOIN servicos ON pedido.id_servicos = servicos.id_servicos WHERE pedido.id_empresa = "+ str(idpessoal) +" AND pedido.data = '"+str(data)+"' ORDER BY clientes.nome;")
            nomecliente = cursor.fetchall()
            nomecliente = clear.clear(nomecliente)
            cursor.execute("SELECT pedido.horarioinicio FROM clientes INNER JOIN pedido ON clientes.id_clientes = pedido.id_clientes INNER JOIN servicos ON pedido.id_servicos = servicos.id_servicos WHERE pedido.id_empresa = "+ str(idpessoal) +" AND pedido.data = '"+str(data)+"' ORDER BY clientes.nome;")
            horarioinicio = cursor.fetchall()
            horarioinicio = clear.clear(horarioinicio)
            cursor.execute("SELECT servicos.nome FROM clientes INNER JOIN pedido ON clientes.id_clientes = pedido.id_clientes INNER JOIN servicos ON pedido.id_servicos = servicos.id_servicos WHERE pedido.id_empresa = "+ str(idpessoal) +" AND pedido.data = '"+str(data)+"' ORDER BY clientes.nome;")
            servico = cursor.fetchall()
            servico = clear.clear(servico)
            cursor.close()
            return {"cliente": nomecliente, "horariodeinicio": horarioinicio, "nomeservico": servico}



class Pedido(Resource):
    def post(self):
        dados = request.json
        data = dados['data']
        data = datetime.strptime(data, '%d/%m/%Y').date()
        horarioinicio = dados['horarioinicio']
        id_clientes = dados['id_clientes']
        id_empresa = dados['id_empresa']
        id_servicos = dados['id_servicos']
        try:
            com_sql = "INSERT INTO pedido(id_servicos, data, horarioinicio, id_clientes, id_empresa) VALUES (%s,%s,%s,%s,%s)"
            valor = (id_servicos, data, horarioinicio, id_clientes, id_empresa)
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
api.add_resource(Empresa_infos, '/empresa/')
api.add_resource(Empresas, '/empresas/')
api.add_resource(Clientes, '/clientes/')
api.add_resource(EmpresaPostandPut, '/empresaget/')
api.add_resource(LoginC, '/cliente/login/')
api.add_resource(Servicos, '/servicos/')
api.add_resource(ServicoGet, '/servicoget/')
api.add_resource(Pedido, '/cliente/')
api.add_resource(Calendarioempresa, '/calendario/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()