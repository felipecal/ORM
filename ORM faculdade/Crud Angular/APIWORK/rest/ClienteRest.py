from flask_restful import Resource, abort, reqparse
from flask import jsonify
from dao import clienteDAO

class Cliente(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('nome')
        self.parser.add_argument('endereco')
        self.parser.add_argument('telefone')

        self.dao = clienteDAO.ClienteDAO()

    def get(self):
        args = self.parser.parse_args()
        if args['nome'] is None and args['id'] is None:
            clientes = self.dao.readAll()
            if clientes is None:
                abort(404, message="Clientes não encontrados!!!")
            else:
                res = []
                for cli in clientes:
                    res.append({
                        'identificador': cli.idt_cliente,
                        'nome': cli.nme_cliente,
                        'endereco': cli.end_cliente,
                        'telefone': cli.tel_cliente
                    })
                return jsonify(res)
        else:
            if args['nome'] is not None:
                clientes = self.dao.readByName(args['nome'])
                if clientes == []:
                    return "CNE"
                else:
                    res = []
                    for cli in clientes:
                        res.append({
                            'identificador': cli.idt_cliente,
                            'nome': cli.nme_cliente,
                            'endereco': cli.end_cliente,
                            'telefone': cli.tel_cliente
                        })

                    return jsonify(res)
            elif args['id'] is not None:
                cli = self.dao.readById(args['id'])
                if cli is None:
                    abort(404, message="Cliente não encontrado!!!")
                else:
                    res = {
                        'identificador': cli.idt_cliente,
                        'nome': cli.nme_cliente,
                        'endereco': cli.end_cliente,
                        'telefone': cli.tel_cliente
                    }
                    return jsonify(res)
            else:
                abort(404, message="Parâmetro de consulta não encontrado!!!")

    def post(self):
        args = self.parser.parse_args()
        cli = self.dao.tb_cliente()
        cli.nme_cliente = args['nome']
        cli.end_cliente = args['endereco']
        cli.tel_cliente = args['telefone']
        self.dao.create(cli)
        return jsonify('{"message" : "Cliente id (' + str(cli.idt_cliente) + ') criado!"}')

    def put(self, id):
        cli = self.dao.readById(id)
        if cli is None:
            abort(404, message="Cliente não encontrado!!!")
        else:
            args = self.parser.parse_args()
            if args['nome'] is not None:
                cli.nme_cliente = args['nome']
            if args['endereco'] is not None:
                cli.end_cliente = args['endereco']
            if args['telefone'] is not None:
                cli.tel_cliente = args['telefone']
            self.dao.update()
            return 'Cliente id (' + str(cli.idt_cliente) + ') alterado!'

    def delete(self, id):
        cli = self.dao.readById(id)
        if cli is None:
            abort(404, message="Cliente não encontrado!!!")
        else:
            self.dao.delete(cli)
            return "Cliente excluído com sucesso!"

