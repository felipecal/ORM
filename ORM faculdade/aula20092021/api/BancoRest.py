from flask_restful import Resource, abort, reqparse

class Banco(Resource):
    bancos = {
        '1': {'Nome': 'MySQL', 'Ano': '1995'},
        '2': {'Nome': 'Oracle', 'Ano': '1978'},
        '3': {'Nome': 'Postgres', 'Ano': '1994'}
    }


    def __init__(self):
           self.parser = reqparse.RequestParser()
           self.parser.add_argument('Nome')
           self.parser.add_argument('Ano')

    def get(self, id):
        self.senaoexiste(id)
        return Banco.bancos[id]

    def post(self, id):
        args = self.parser.parse_args()
        banco = {'Nome': args['Nome'], 'Ano': args['Ano']}
        Banco.bancos[id] = banco
        return "Banco Incluído"

    def put(self, id):
        args = self.parser.parse_args()
        Banco.bancos[id] = {'Nome': args['Nome'], 'Ano': args['Ano']}
        return "Banco Alterado"

    def delete(self, id):
        Banco.bancos.pop(id)
        return "Banco Excluído"

    def senaoexiste(self,id):
        if id not in Banco.bancos:
            abort(404, msg="Banco {} não existe".format(id))
