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
   tb_clientes = ses.query(tb_cliente).all()
   print('Listagem com todos os Clientes')
   for serv in tb_clientes:
      print('-------------------------------------------------------------------')
      print('Número do Cliente:', serv.idt_cliente)
      print('Cliente:', serv.nme_cliente)
      print('Endereço:', serv.end_cliente)
      print('Telefone:', serv.tel_cliente)
      print('')
   idt = int(input('Escreva o número do cliente para cancelar o agendamento? [{}-{}]: '.format(menor, maior)))
   cli = ses.query(tb_cliente).filter_by(idt_cliente=idt).first()
   print("\n" * 30)
   agendamentos = ses.query(ta_agendamento).filter_by(cod_cliente=idt).all()
   print('Agendamentos do cliente')
   print('-' * 40)
   for s in agendamentos:
       print(s.idt_agendamento, '-', s.db_agendamento,'Cod serviço:' ,s.cod_servico,'Cod cliente:', s.cod_cliente)
   print('-' * 40)
   print('Cliente:', cli.nme_cliente)
   num_agendamento = int(input('Qual número do agendamento para cancelar? '))
   serv = ses.query(ta_agendamento).filter(ta_agendamento.idt_agendamento == num_agendamento).delete()
   ses.commit()

   # Listar os agendamentos do cliente
   print("\n" * 30)
   print('Cliente:', cli.nme_cliente)
   print('-' * 40)
   for a in cli.ta_agendamento_collection:
       print(a.tb_servico.dsc_servico, a.db_agendamento)

   opc = input('Fazer mais um agendamento [S-N]? ')
   if opc.upper() == 'N':
       continuar = False

ses.close()
