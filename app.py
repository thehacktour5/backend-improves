from flask import Flask, request, abort
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

users = [
       {
              'name':'Lindo',
              'age':22
       },
       {
              'name':'Gostoso',
              'age':56
       }
]

class AllUsers(Resource):
       def get(self):
              return {'Users':[user for user in users]}, 200


class UserById(Resource):
       def get(self, id):
              return {'User':users[id]}, 200

api.add_resource(AllUsers, '/')
api.add_resource(UserById, '/<int:id>/')
if __name__ == "__main__":
       app.run(debug=True)
