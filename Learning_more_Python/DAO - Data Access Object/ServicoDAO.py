from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


class ServicoDAO:

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
        # -------------------------------------------------------------------------------------------------

    def create(self, servico):
        self.ses.add(servico)
        self.ses.commit()

    def readAll(self):
        servicos = self.ses.query(self.tb_servico).all()
        return servicos

    def readById(self, id):
        servico = self.ses.query(self.tb_servico).filter_by(idt_servico=id).first()
        return servico

    def readByName(self, name):
        servicos = self.ses.query(self.tb_servico).filter(self.tb_servico.dsc_servico.ilike('%' + name + '%')).all()
        return servicos

    def update(self):
        self.ses.commit()

    def delete(self, servico):
        self.ses.delete(servico)
        self.ses.commit()

    def __del__(self):
        self.ses.close()
