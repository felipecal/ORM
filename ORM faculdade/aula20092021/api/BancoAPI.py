from flask import Flask
from flask_restful import Api
import BancoRest

app = Flask(__name__)
api = Api(app)

api.add_resource(BancoRest.Banco, '/banco/<id>')

if __name__ == '__main__':
   app.run(debug=True)
