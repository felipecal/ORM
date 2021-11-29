from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

class ClienteDAO:

    def __init__(self):
        # Ligação com o esquema de banco de dados
        engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")

        # Mapeamento Objeto Relacional com o SQLAlchemy
        DB = automap_base()
        DB.prepare(engine, reflect=True)
        self.tb_cliente = DB.classes.tb_cliente
        self.tb_servico = DB.classes.tb_servico
        self.ta_agendamento = DB.classes.ta_agendamento

        # Trabalho com sessões da base agora Objeto-Relacional
        session_factory = sessionmaker(bind=engine)
        self.ses = session_factory()
        #-------------------------------------------------------------------------------------------------

    def create(self, cliente):
       self.ses.add(cliente)
       self.ses.commit()

    def readAll(self):
       clientes = self.ses.query(self.tb_cliente).all()
       return clientes

    def readById(self, id):
       cliente = self.ses.query(self.tb_cliente).filter_by(idt_cliente=id).first()
       return cliente

    def readByName(self, name):
        clientes = self.ses.query(self.tb_cliente).filter(self.tb_cliente.nme_cliente.ilike('%' + name + '%')).all()
        return clientes

    def update(self):
        self.ses.commit()

    def delete(self, cliente):
        self.ses.delete(cliente)
        self.ses.commit()

