import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import func

def incluir():
    x=1
    while x==1:
        print('--'*60)
        print('Menu de Opções')
        print('Digite alguma das seguintes opções')
        print('')
        print('1 - Se deseja prosseguir para a inclusão de cliente')
        print('0 - Se deseja retornar para o menu')
        z = int(input(''))
        if z ==1:
            print ('Informe os dados a seguir para incluir cliente')
            serv = tb_cliente()
            serv.nme_cliente = input("Nome do Cliente: ")
            serv.end_cliente = input("Endereço do Cliente: ")
            serv.tel_cliente = int(input("Telefone Cliente: "))
            print('Cliente incluido com sucesso.')
            ses.add(serv)
            ses.commit()
        elif z==0:
            x -=1
        else:
            print('Opção ocorreta, digite novamente!')
    else:
        menu()


def consultar():
   tb_clientes = ses.query(tb_cliente).all()
   print('Listagem com todos os Clientes')
   for serv in tb_clientes:
       print('-------------------------------------------------------------------')
       print('Cliente:', serv.nme_cliente)
       print('Endereço:', serv.end_cliente)
       print('Telefone:', serv.tel_cliente)
   input("\nEnter - Para voltar ao Menu")

def alterar():
    x = 1
    while x == 1:
        print('--' * 60)
        print('Menu de Opções')
        print('Digite alguma das seguintes opções')
        print('')
        print('1 - Continuar para alteração de cliente.')
        print('0 - Retornar para o menu.')
        z = int(input(''))
        if z == 1:
           maior, menor = ses.query(func.count(tb_cliente.idt_cliente), func.count(tb_cliente.idt_cliente)).first()
           print('Alteração de dados do cliente')
           idt = int(input('Alterar cliente número? [{}-{}]: '.format(maior, menor)))
           serv = ses.query(tb_cliente).filter_by(idt_cliente=idt).first()
           serv.nme_cliente = input('Nome do Cliente [{}]: '.format(serv.nme_cliente))
           serv.end_cliente = input('Endereço do Cliente [{}]: '.format(serv.end_cliente))
           serv.tel_cliente = int(input('Telefone [{}]: '.format(serv.tel_cliente)))
           ses.commit()
           input("\nEnter - Para voltar ao Menu")
        elif z==0:
            x -=1
        else:
            print('Opção ocorreta, digite novamente!')
    else:
        menu()

def excluir():
   x = 1
   while x == 1:
       print('--' * 60)
       print('Menu de Opções')
       print('Digite alguma das seguintes opções')
       print('')
       print('1 - Continuar para exclusão de cliente.')
       print('0 - Retornar para o menu.')
       z = int(input(''))
       if z == 1:
           tb_clientes = ses.query(tb_cliente).all()
           for serv in tb_clientes:
               print(serv.idt_cliente, serv.nme_cliente, serv.end_cliente,serv.tel_cliente)
           idt = int(input('Qual o número do cliente para excluir? '))
           cod=idt
           ses.query(ta_agendamento).filter(ta_agendamento.cod_cliente == cod).delete()
           ses.query(tb_cliente).filter(tb_cliente.idt_cliente == idt).delete()
           input("\nEnter - Para voltar ao Menu")
       elif z == 0:
           x -=1
       else:
           print('Opção ocorreta, digite novamente!')
   else:
       menu()

def menu():
   continuar = True
   while continuar:
       print('\n' * 30)
       print('CRUD de Clientes - MENU')
       print('1 - Incluir')
       print('2 - Consultar')
       print('3 - Alterar')
       print('4 - Excluir')
       print('5 - Sair')
       opc = input('Qual a sua opção? ')
       print("\n" * 30)
       if opc == '1':
           incluir()
       elif opc == '2':
           consultar()
       elif opc == '3':
           alterar()
       elif opc == '4':
           excluir()
       elif opc == '5':
           continuar = False
       else:
           print ('Opção inválida')
           input()
   ses.close()
   sys.exit()

engine = create_engine("mysql+mysqlconnector://root:hiragi7@localhost/db_work?charset=utf8mb4")
DB = automap_base()
DB.prepare(engine, reflect=True)
tb_cliente = DB.classes.tb_cliente
ta_agendamento = DB.classes.ta_agendamento
session_factory = sessionmaker(bind=engine)
ses = session_factory()
menu()
