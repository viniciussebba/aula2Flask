from crypt import methods
from math import degrees
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='view')

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autentica",methods=['POST'])
def autentica():
    usr = request.form['usuario']
    pswrd = request.form['senha']
    #Consultar se usuário existe, passando usr e pswrd!
    return render_template("usuario.html", usuario=usr, senha=pswrd)

@app.route("/signin", methods=['GET'])
def signin():
    return render_template("formCliente.html")

@app.route("/cadastra", methods=['POST'])
def cadastra():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    usr = request.form['usuario']
    pswrd = request.form['senha']
    #CREATE o usuário, passando os parâmetros lidos acima!
    return render_template("usuario.html", nome=nome, cpf=cpf, email=email, usuario=usr, senha=pswrd)

if __name__ == "__main__":
    app.run()