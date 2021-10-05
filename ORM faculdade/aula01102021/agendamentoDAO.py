from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

class AgendamentoDAO:

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

   def create(self, agendamento):
      self.ses.add(agendamento)
      self.ses.commit()

   def readAll(self):
      agendamentos = self.ses.query(self.ta_agendamento).all()
      return agendamentos

   def readById(self, id):
      agendamento = self.ses.query(self.ta_agendamento).filter_by(idt_agendamento=id).first()
      return agendamento

   def readByServico(self, codigo):
       agendamentos = self.ses.query(self.ta_agendamento).filter(self.ta_agendamento.cod_servico == codigo).all()
       return agendamentos

   def readByCliente(self, codigo):
       agendamentos = self.ses.query(self.ta_agendamento).filter(self.ta_agendamento.cod_cliente == codigo).all()
       return agendamentos

   def update(self):
       self.ses.commit()

   def delete(self, agendamento):
       self.ses.delete(agendamento)
       self.ses.commit()
