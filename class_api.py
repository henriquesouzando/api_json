from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# criando o app flask
app = Flask(__name__)
# criando objeto api
api = Api(app)
  
#recurso de envio e recebimento de dados
class Hello(Resource):
  
    
    # metodo get 
    def get(self):
  
        return jsonify({'message': "Hello tech recruiter! Welcome my api in class."})
  
    # metodo post 
    def post(self):
          
        data = request.get_json()  
        
        # status code
        return jsonify(data, 201)
  
  
# Recurso de raiz quadrada
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})
  
  
# adicionando os recursos definidos junto com suas urls correspondentes
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
  
  

if __name__ == '__main__':
  
    app.run(debug = True)