import pymysql

conexao = pymysql.connect(
    host = 'sql10.freemysqlhosting.net',
    user = 'sql10343231',
    passwd = 'zdDyscJ4Fd',
    database= 'sql10343231'
)
cursor = conexao.cursor()

class comandos:
    def executar(self):
        com_sql = "INSERT INTO empresa(usuario,senha,nome,endereco,bairro,telefone,cidade,uf,dinheiro,credito,debito) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        valor = ("usuario", "senha", "nome", "endereco", "bairro", "telefone", "cidade", "uf", "dinheiro", "credito", "debito")
        cursor.execute(com_sql,valor)
        conexao.commit()
    def salvar(self):
        conexao.commit()

def init():
    cursor.execute('CREATE TABLE empresa(id INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(255) NOT NULL UNIQUE,senha VARCHAR(255) NOT NULL,nome VARCHAR(255) NOT NULL UNIQUE,numero VARCHAR(255) NOT NULL,endereco VARCHAR(255) NOT NULL,bairro VARCHAR(255) NOT NULL,telefone VARCHAR(255) NOT NULL,cidade VARCHAR(255) NOT NULL,uf VARCHAR(2) NOT NULL,dinheiro VARCHAR(3) NOT NULL,credito VARCHAR(3) NOT NULL,debito VARCHAR(3) NOT NULL,INDEX (nome),INDEX (usuario))')
    cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(255) NOT NULL UNIQUE,senha VARCHAR(255) NOT NULL,nome VARCHAR(255) NOT NULL UNIQUE,numero VARCHAR(255) NOT NULL,endereco VARCHAR(255) NOT NULL,bairro VARCHAR(255) NOT NULL,telefone VARCHAR(255) NOT NULL,cidade VARCHAR(255) NOT NULL,uf VARCHAR(2) NOT NULL,INDEX (nome),INDEX (usuario))')

if __name__ == '__main__':
    init()
