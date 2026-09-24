from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, scoped_session

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/taskflow')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id_pessoa = Column(Integer, primary_key=True)
    nome_pessoa = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha_hash = Column(String(20), nullable=False)
    papel = Column(String(100), default='usuario',nullable=False)
    criado_em = Column(Date, nullable=False, server_default=func.now())

    def __repr__(self):
        return f'Pessoa {self.nome_pessoa}, Email {self.email}, Papel {self.papel}'

class Atividade(Base):
    __tablename__ = 'atividades'
    id_atividade = Column(Integer, primary_key=True)
    nome_atividade = Column(String(100), nullable=False)
    data_execucao = Column(Date, nullable=False, server_default=func.now())
    descricao_atividade = Column(String(10000), nullable=False)
    prioridade = Column(String(10), nullable=False)
    responsavel = Column(Integer, ForeignKey('pessoas.id_pessoa'))

    def __repr__(self):
        return f'Atividade {self.nome_atividade}, Data Execução {self.data_execucao}, Descrição {self.descricao_atividade}, Responsavel {self.responsavel}, Prioridade {self.prioridade}'

class Tipo(Base):
    __tablename__ = 'tipos'
    id_tipo = Column(Integer, primary_key=True)
    nome_tipo = Column(String(100), nullable=False)
    descricao_tipo = Column(String(10000), nullable=False)

class Recurso(Base):
    __tablename__ = 'recursos'
    id_recurso = Column(Integer, primary_key=True)
    nome_recurso = Column(String(50), nullable=False)
    descricao_recurso = Column(String(10000), nullable=False)

    def __repr__(self):
        return f'Recurso {self.nome_recurso}, Descrição {self.descricao_recurso}'