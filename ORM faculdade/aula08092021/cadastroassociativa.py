from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func

# --------------------------------------- VARIÁVEIS GLOBAIS ------------------------------------
# Ligação com o esquema de banco de dados
engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")

# Mapeamento Objeto Relacional com o SQLAlchemy
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_servico = DB.classes.tb_servico
tb_cliente = DB.classes.tb_cliente
ta_agendamento = DB.classes.ta_agendamento

# Trabalho com sessões da base agora Objeto-Relacional
session_factory = sessionmaker(bind=engine)
ses = session_factory()
#-------------------------------------------------------------------------------------------------

continuar = True
while continuar:
   print("\n" * 30)
   # Descobrindo o menor e maior identificador cadastrado
   menor, maior = ses.query(func.min(tb_cliente.idt_cliente), func.max(tb_cliente.idt_cliente)).first()
   idt = int(input('Agendar serviço para o cliente? [{}-{}]: '.format(menor, maior)))
   cli = ses.query(tb_cliente).filter_by(idt_cliente=idt).first()

   print("\n" * 30)
   # Listar os serviços disponíveis
   servicos = ses.query(tb_servico).all()
   print('Catálogo de Serviços')
   print('-' * 40)
   for s in servicos:
       print(s.idt_servico, '-', s.dsc_servico, 'R$', s.vlr_servico, s.tmp_servico, 'hora(s)')
   print('-' * 40)
   print('Cliente:', cli.nme_cliente)
   idt = int(input('Qual número do serviço para agendar? '))
   dta = input('Qual a data do agendamento [AAAA-MM-DD]? ')
   hor = input('Qual a hora do agendamento [HH:MM]? ')

   serv = ses.query(tb_servico).filter_by(idt_servico=idt).first()

   # Incluindo um novo agendamento
   a = ta_agendamento()
   a.tb_cliente = cli
   a.tb_servico = serv
   a.dti_agendamento = dta + ' ' + hor
   ses.add(a)
   ses.commit()

   # Listar os agendamentos do cliente
   print("\n" * 30)
   print('Cliente:', cli.nme_cliente)
   print('-' * 40)
   for a in cli.ta_agendamento_collection:
       print(a.tb_servico.dsc_servico, a.dti_agendamento)

   opc = input('Fazer mais um agendamento [S-N]? ')
   if opc.upper() == 'N':
       continuar = False

ses.close()
