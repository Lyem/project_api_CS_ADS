import pymysql

conexao = pymysql.connect(
    host='',
    user='',
    passwd='',
    database=''
)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE empresa(id_empresa INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(25) NOT NULL UNIQUE,senha VARCHAR(10) NOT NULL,nome VARCHAR(50) NOT NULL,numero VARCHAR(8) NOT NULL,endereco VARCHAR(50) NOT NULL,bairro VARCHAR(20) NOT NULL,telefone VARCHAR(20) NOT NULL,cidade VARCHAR(50) NOT NULL,uf VARCHAR(2) NOT NULL,dinheiro VARCHAR(3) NOT NULL,credito VARCHAR(3) NOT NULL,debito VARCHAR(3) NOT NULL,hatendimentoi INT NULL,hatendimentof INT NULL,segunda VARCHAR(3) NULL,quinta VARCHAR(3) NULL,domingo VARCHAR(3) NULL,terça VARCHAR(3) NULL,sexta VARCHAR(3) NULL,quarta VARCHAR(3) NULL,sabado VARCHAR(3) NULL,fsemanaabres INT NULL,fsemanafechas INT NULL,fsemanaabred INT NULL,fsemanafechad INT NULL,feriado VARCHAR(3) NULL,feriadoa INT NULL,feriadof INT NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE clientes(id_clientes INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(25) NOT NULL UNIQUE,senha CHAR(10) NOT NULL,nome VARCHAR(50) NOT NULL,numero VARCHAR(8) NOT NULL,endereco VARCHAR(50) NOT NULL,bairro VARCHAR(20) NOT NULL,telefone VARCHAR(20) NOT NULL,cidade VARCHAR(50) NOT NULL,uf VARCHAR(2) NOT NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE servicos(id_servicos INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(20) NOT NULL UNIQUE,preco REAL NOT NULL,horario TIME NOT NULL,id_empresa INT,FOREIGN KEY(id_empresa) REFERENCES empresa(id_empresa))')
cursor.execute('CREATE TABLE datacliente(id_datacli INT AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL,horarioinicio TIME NOT NULL,id_clientes INT NOT NULL,id_servicos INT,FOREIGN KEY(id_clientes) REFERENCES clientes(id_clientes),FOREIGN KEY(id_servicos) REFERENCES servicos(id_servicos))')
cursor.execute('CREATE TABLE dataempresa(id_dataem INT AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL,horarioinicio TIME NOT NULL,horariofim TIME NOT NULL,id_empresa INT,id_clientes INT,FOREIGN KEY(id_empresa) REFERENCES empresa(id_empresa),FOREIGN KEY(id_clientes) REFERENCES clientes(id_clientes))')

cursor.close()
