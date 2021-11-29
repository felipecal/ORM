from flask import Flask
from flask_restful import Api
from rest import ClienteRest

app = Flask(__name__)
api = Api(app)

api.add_resource(ClienteRest.Cliente, '/cliente', '/cliente/<id>')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


if __name__ == '__main__':
    app.run(debug=True)
