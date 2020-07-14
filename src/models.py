import pymysql

conexao = pymysql.connect(
    host='',
    user='',
    passwd='',
    database=''
)
cursor = conexao.cursor()

cursor.execute('CREATE TABLE empresa(id_empresa INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(25) NOT NULL UNIQUE,senha VARCHAR(10) NOT NULL,nome VARCHAR(50) NOT NULL,numero VARCHAR(8) NOT NULL,endereco VARCHAR(50) NOT NULL,bairro VARCHAR(20) NOT NULL,telefone VARCHAR(20) NOT NULL,cidade VARCHAR(50) NOT NULL,uf VARCHAR(2) NOT NULL,dinheiro VARCHAR(3) NOT NULL,credito VARCHAR(3) NOT NULL,debito VARCHAR(3) NOT NULL,hatendimentoi VARCHAR(20) NULL,hatendimentof VARCHAR(20) NULL,segunda VARCHAR(3) NULL,quinta VARCHAR(3) NULL,domingo VARCHAR(3) NULL,terca VARCHAR(3) NULL,sexta VARCHAR(3) NULL,quarta VARCHAR(3) NULL,sabado VARCHAR(3) NULL,fsemanaabres VARCHAR(20) NULL,fsemanafechas VARCHAR(20) NULL,fsemanaabred VARCHAR(20) NULL,fsemanafechad VARCHAR(20) NULL,feriado VARCHAR(3) NULL,feriadoa VARCHAR(20) NULL,feriadof VARCHAR(20) NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE clientes(id_clientes INT AUTO_INCREMENT PRIMARY KEY,usuario VARCHAR(25) NOT NULL UNIQUE,senha CHAR(10) NOT NULL,nome VARCHAR(50) NOT NULL,numero VARCHAR(8) NOT NULL,endereco VARCHAR(50) NOT NULL,bairro VARCHAR(20) NOT NULL,telefone VARCHAR(20) NOT NULL,cidade VARCHAR(50) NOT NULL,uf VARCHAR(2) NOT NULL,INDEX (nome),INDEX (usuario))')
cursor.execute('CREATE TABLE servicos(id_servicos INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(20) NOT NULL UNIQUE,preco VARCHAR(50) NOT NULL,horario VARCHAR(20) NOT NULL,id_empresa INT,FOREIGN KEY(id_empresa) REFERENCES empresa(id_empresa))')
cursor.execute('CREATE TABLE pedido(id_pedido INT AUTO_INCREMENT NOT NULL, id_servicos INT NOT NULL, data DATE NOT NULL,horarioinicio VARCHAR(20) NOT NULL,id_clientes INT NOT NULL, id_empresa INT NOT NULL, PRIMARY KEY(id_pedido), FOREIGN KEY(id_servicos) REFERENCES servicos(id_servicos), FOREIGN KEY(id_clientes) REFERENCES clientes(id_clientes),FOREIGN KEY(id_empresa) REFERENCES empresa(id_empresa) ON DELETE CASCADE)')

cursor.close()
