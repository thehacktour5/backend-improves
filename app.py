from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True


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

@app.route('/')
def AllUsers():
       return jsonify(users)

@app.route('/users', methods=['POST'])
def AddUser():
       user = request.get_json()
       users.append(user)
       return {'Usuarios': users}

@app.route('/users/<int:index>/', methods=['DELETE'])
def DeleteUser(index):
       users.pop(index)
       return 'None',200

if __name__ == "__main__":
       app.run(debug=True)
