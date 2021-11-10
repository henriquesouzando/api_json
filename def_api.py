# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# No terminal digitamos o comando 'curl' mais a url (http://127.0.0.1:5000/)
# Teremos como response uma mensagem de boas vindas.
# diferença entre get e post, no get a requisição é feita via URL e tem limite de caracteres que é 255, já no post não limite de caracteres, pois a mensagem é enviada junto com o corpo da requisição http. 
# Nessa função temos apenas o método get disponível 

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "Hello tech recruiter! Welcome my api in function."
        return jsonify({'data': data})
  
# Um simple função para calcular a raiz quadrada
# O numero pode ser enviado pela url com método GET
# No terminal podemos testar utilizando o comando curl e a url (http://127.0.0.1:5000/square/10)
# O retorno será no formato json

@app.route('/square/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})
  

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)


