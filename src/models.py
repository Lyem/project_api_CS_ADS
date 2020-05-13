from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine =  create_engine('sqlite:///contas.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Empresa(Base):
    __tablename__='empresa'
    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    senha = Column(String)
    nome = Column(String)

class Clientes(Base):
    __tablename__='clientes'
    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    senha = Column(String)
    nome = Column(String)

class EmpresaConf(Base):
    __tablename__='empresaconf'
    id = Column(Integer, primary_key=True)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship('Empresa')

class Clientconf(Base):
    __tablename__='clientconf'
    id = Column(Integer, primary_key=True)
    clientes_id = Column(Integer, ForeignKey('clientes.id'))
    clientes = relationship('clientes')

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()