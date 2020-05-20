import os
from flask import Flask, request
from flask_restful import Resource, Api
from models import Empresa, Servicos

app = Flask(__name__)
api = Api(app)

class On(Resource):
    def get(self):
        return {'status':'online'}

class Empresa_infos(Resource):
    def get(self, nome):
        empresa = Empresa.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':empresa.nome,
                'id':empresa.id,
                'cidade':empresa.cidade
            }
            return response
        except AttributeError:
            return {
                'status':'error',
                'mensagem':'empresa não emcontrada'
            }
    def put(self, nome):
        empresa = Empresa.query.filter_by(nome=nome).first()
        dados = request.json
        try:
            empresa.nome = dados['nome']
            empresa.usuario = dados['usuario']
            empresa.senha = dados['senha']
            empresa.numero = dados['numero']
            empresa.endereco = dados['endereco']
            empresa.bairro = dados['bairro']
            empresa.telefone = dados['telefone']
            empresa.cidade = dados['cidade']
            empresa.uf = dados['uf']
            empresa.save()
            return {'status':'sucesso'}
        except AttributeError:
            return{'status':'error','mensagem':AttributeError}
    def delete(self, nome):
        try:
            empresa = Empresa.query.filter_by(nome=nome).first()
            empresa.delete()
            return{'status':'sucesso'}
        except AttributeError:
            return{'status':'error','menssagem':AttributeError}

class Empresas(Resource):
    def get(self):
        empresa = Empresa.query.all()
        response = [{'nome':i.nome} for i in empresa]
        return response
    def post(self):
        dados = request.json
        try:
            empresa = Empresa(usuario=dados['usuario'], senha=dados['senha'],nome=dados['nome'],numero=dados['numero'],endereco=dados['endereco'],bairro=dados['bairro'],telefone=dados['telefone'],cidade=dados['cidade'],uf=dados['uf'])
            empresa.save()
            return {'status':'sucesso'}
        except AttributeError:
            return{
                'status':'error',
                'mensagem': AttributeError
            }

class Servico(Resource):
    def post(self):
        dados = request.json
        empresa = Empresa.query.filter_by(nome=dados['empresa']).first()
        servico = Servicos(nome=dados['servico'],preco=dados['preco'], empresa=empresa)
        servico.save()
        return {'status':'sucesso'}

api.add_resource(On, '/')
api.add_resource(Empresa_infos, '/empresa/<string:nome>/')
api.add_resource(Empresas, '/empresas/')
api.add_resource(Servico, '/servicos/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)