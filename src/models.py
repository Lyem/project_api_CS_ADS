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
    usuario = Column(String, index=True)
    senha = Column(String)
    nome = Column(String, index=True)
    numero = Column(String)
    telefone = Column(String)
    cidade = Column(String)
    uf = Column(String)

    def __repr__(self):
        return '<Empresa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Servicos(Base):
    __tablename__='servico'
    id = Column(Integer, primary_key=True)
    servico = Column(String, index=True)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()