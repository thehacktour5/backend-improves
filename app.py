from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

alunos = {
       "Atilio":{
              "idade":25,
              "gostosura":"lindo"
       },
       "Hector":{
              "idade":25,
              "gostosura":"lindo"
       }
}

class AlunosEndPoint(Resource):
       def get(self):
              return [alunos[key] for key in alunos.keys()]

class AlunosGeralEndPoint(Resource):
       def put(self, alunos_id):
              alunos[alunos_id] = request.form['data']
              return {alunos: alunos[alunos_id]}

api.add_resource(AlunosEndPoint, '/')
api.add_resource(AlunosGeralEndPoint, '/alunos/<string:alunos>/')

if __name__ == "__main__":
       app.run()
