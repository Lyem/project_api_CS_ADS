import pymysql

conexao = pymysql.connect(
    host='',
    user='',
    passwd='',
    database=''
)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE empresa(id INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(255) NOT NULL UNIQUE,senha VARCHAR(255) NOT NULL,nome VARCHAR(255) NOT NULL UNIQUE,numero VARCHAR(255) NOT NULL,endereco VARCHAR(255) NOT NULL,bairro VARCHAR(255) NOT NULL,telefone VARCHAR(255) NOT NULL,cidade VARCHAR(255) NOT NULL,uf VARCHAR(2) NOT NULL,dinheiro VARCHAR(3) NOT NULL,credito VARCHAR(3) NOT NULL,debito VARCHAR(3) NOT NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(255) NOT NULL UNIQUE,senha VARCHAR(255) NOT NULL,nome VARCHAR(255) NOT NULL UNIQUE,numero VARCHAR(255) NOT NULL,endereco VARCHAR(255) NOT NULL,bairro VARCHAR(255) NOT NULL,telefone VARCHAR(255) NOT NULL,cidade VARCHAR(255) NOT NULL,uf VARCHAR(2) NOT NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE servicos(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL UNIQUE,preco REAL NOT NULL,horario TIME NOT NULL,FOREIGN KEY(id) REFERENCES empresa(id))')
cursor.execute('CREATE TABLE datacliente(id INT AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL,horarioinicio TIME NOT NULL,FOREIGN KEY(id) REFERENCES clientes(id),FOREIGN KEY(id) REFERENCES servicos(id))')
cursor.execute('CREATE TABLE dataempresa(id INT AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL,horarioinicio TIME NOT NULL,horariofim TIME NOT NULL,FOREIGN KEY(id) REFERENCES empresa(id),FOREIGN KEY(id) REFERENCES clientes(id))')

cursor.close()