from ServicoDAO import ServicoDAO


def testeInc():
    dao = ServicoDAO()
    servico = dao.tb_cliente()
    servico.dsc_servico = 'Lavagem de Roupa'
    servico.vlr_servico = '49.90'
    servico.tmp_servico = '1'
    dao.create(servico)
    print("Inserir: ", servico.dsc_servico)


testeInc()


def testeLer():
    dao = ServicoDAO()
    for c in dao.readAll():
        print(c.dsc_servico)


def testeLerNome():
    dao = ServicoDAO()
    for c in dao.readByName('e'):
        print(c.dsc_servico)


def testeAlterar():
    dao = ServicoDAO()
    servico = dao.readById(4)
    servico.tmp_servico = 2
    dao.update()


def testeExcluir():
    dao = ServicoDAO()
    servico = dao.readById(6)
    dao.delete(servico)
