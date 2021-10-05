from flask_restful import Resource, abort, reqparse
from flask import jsonify
import agendamentoDAO

class Agendamento(Resource):
  def __init__(self):
      self.parser = reqparse.RequestParser()
      self.parser.add_argument('id', type=int)
      self.parser.add_argument('cod_servico', type=int)
      self.parser.add_argument('cod_cliente', type=int)
      self.parser.add_argument('db_agendamento')
      self.parser.add_argument('completo')

      self.dao = agendamentoDAO.AgendamentoDAO()

  def get(self):
      args = self.parser.parse_args()
      if args['cod_servico'] is None and args['cod_cliente'] is None and args['id'] is None:
          agendamentos = self.dao.readAll()
          if agendamentos is None:
              abort(404, message="Agendamentos não encontrados!!!")
          else:
              res = {}
              for age in agendamentos:
                  if args['completo'] is None:
                      res[age.idt_agendamento] = {
                          'identificador': age.idt_agendamento,
                          'cod_servico': age.cod_servico,
                          'cod_cliente': age.cod_cliente,
                          'db_agendamento': age.db_agendamento
                      }
                  else:
                      res[age.idt_agendamento] = {
                          'identificador': age.idt_agendamento,
                          'cod_servico': age.cod_servico,
                          'cod_cliente': age.cod_cliente,
                          'db_agendamento': age.db_agendamento,
                          'Servico': {
                              'idt_servico': age.tb_servico.idt_servico,
                              'dsc_servico': age.tb_servico.dsc_servico,
                              'vlr_servico': str(age.tb_servico.vlr_servico),
                              'tmp_servico': age.tb_servico.tmp_servico
                          },
                          'Cliente': {
                              'idt_cliente': age.tb_cliente.idt_cliente,
                              'nme_cliente': age.tb_cliente.nme_cliente,
                              'end_cliente': age.tb_cliente.end_cliente,
                              'tel_cliente': age.tb_cliente.tel_cliente
                          }
                      }
              return jsonify(res)
      else:
          if args['cod_servico'] is not None:
              agendamentos = self.dao.readByServico(args['cod_servico'])
              if agendamentos is None:
                  abort(404, message="Agendamentos não encontrados!!!")
              else:
                  res = {}
                  for age in agendamentos:
                      if args['completo'] is None:
                          res[age.idt_agendamento] = {
                              'identificador': age.idt_agendamento,
                              'cod_servico': age.cod_servico,
                              'cod_cliente': age.cod_cliente,
                              'db_agendamento': age.db_agendamento
                          }
                      else:
                          res[age.idt_agendamento] = {
                              'identificador': age.idt_agendamento,
                              'cod_servico': age.cod_servico,
                              'cod_cliente': age.cod_cliente,
                              'db_agendamento': age.db_agendamento,
                              'Servico': {
                                  'idt_servico': age.tb_servico.idt_servico,
                                  'dsc_servico': age.tb_servico.dsc_servico,
                                  'vlr_servico': str(age.tb_servico.vlr_servico),
                                  'tmp_servico': age.tb_servico.tmp_servico
                              },
                              'Cliente': {
                                  'idt_cliente': age.tb_cliente.idt_cliente,
                                  'nme_cliente': age.tb_cliente.nme_cliente,
                                  'end_cliente': age.tb_cliente.end_cliente,
                                  'tel_cliente': age.tb_cliente.tel_cliente
                              }
                          }
                  return jsonify(res)
          elif args['cod_cliente'] is not None:
              agendamentos = self.dao.readByCliente(args['cod_cliente'])
              if agendamentos is None:
                  abort(404, message="Agendamentos não encontrados!!!")
              else:
                  res = {}
                  for age in agendamentos:
                      if args['completo'] is None:
                          res[age.idt_agendamento] = {
                              'identificador': age.idt_agendamento,
                              'cod_servico': age.cod_servico,
                              'cod_cliente': age.cod_cliente,
                              'db_agendamento': age.db_agendamento
                          }
                      else:
                          res[age.idt_agendamento] = {
                              'identificador': age.idt_agendamento,
                              'cod_servico': age.cod_servico,
                              'cod_cliente': age.cod_cliente,
                              'db_agendamento': age.db_agendamento,
                              'Servico': {
                                  'idt_servico': age.tb_servico.idt_servico,
                                  'dsc_servico': age.tb_servico.dsc_servico,
                                  'vlr_servico': str(age.tb_servico.vlr_servico),
                                  'tmp_servico': age.tb_servico.tmp_servico
                              },
                              'Cliente': {
                                  'idt_cliente': age.tb_cliente.idt_cliente,
                                  'nme_cliente': age.tb_cliente.nme_cliente,
                                  'end_cliente': age.tb_cliente.end_cliente,
                                  'tel_cliente': age.tb_cliente.tel_cliente
                              }
                          }
                  return jsonify(res)
          elif args['id'] is not None:
              age = self.dao.readById(args['id'])
              if age is None:
                  abort(404, message="Agendamento não encontrado!!!")
              else:
                  res = {}
                  if args['completo'] is None:
                      res[age.idt_agendamento] = {
                          'identificador': age.idt_agendamento,
                          'cod_servico': age.cod_servico,
                          'cod_cliente': age.cod_cliente,
                          'db_agendamento': age.db_agendamento
                      }
                  else:
                      res[age.idt_agendamento] = {
                          'identificador': age.idt_agendamento,
                          'cod_servico': age.cod_servico,
                          'cod_cliente': age.cod_cliente,
                          'db_agendamento': age.db_agendamento,
                          'Servico': {
                              'idt_servico': age.tb_servico.idt_servico,
                              'dsc_servico': age.tb_servico.dsc_servico,
                              'vlr_servico': str(age.tb_servico.vlr_servico),
                              'tmp_servico': age.tb_servico.tmp_servico
                          },
                          'Cliente': {
                              'idt_cliente': age.tb_cliente.idt_cliente,
                              'nme_cliente': age.tb_cliente.nme_cliente,
                              'end_cliente': age.tb_cliente.end_cliente,
                              'tel_cliente': age.tb_cliente.tel_cliente
                          }
                      }
                  return jsonify(res)
          else:
              abort(404, message="Parâmetro de consulta não encontrado!!!")

  def post(self):
      args = self.parser.parse_args()
      age = self.dao.ta_agendamento()
      age.cod_servico = args['cod_servico']
      age.cod_cliente = args['cod_cliente']
      age.db_agendamento = args['db_agendamento']
      self.dao.create(age)
      return jsonify("{'message' : 'Agendamento id (" + str(age.idt_agendamento) + ") criado!'}")

  def put(self, id):
      age = self.dao.readById(id)
      if age is None:
          abort(404, message="Agendamento não encontrado!!!")
      else:
          args = self.parser.parse_args()
          if args['cod_servico'] is not None:
              age.cod_servico = args['cod_servico']
          if args['cod_cliente'] is not None:
              age.cod_cliente = args['cod_cliente']
          if args['ddb_agendamento'] is not None:
              age.db_agendamento = args['db_agendamento']
          self.dao.update()
          return jsonify("{'message' : 'Agendamento id (" + str(age.idt_agendamento) + ") alterado!'}")

  def delete(self, id):
      age = self.dao.readById(id)
      if age is None:
          abort(404, message="Agendamento não encontrado!!!")
      else:
          self.dao.delete(age)
          return jsonify("{'message' : 'Agendamento excluído!'}")
