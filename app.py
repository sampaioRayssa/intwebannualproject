from flask import *
from myfunctions import *

app = Flask(__name__)

app.secret_key = "f8X$wLk2V#bQ!zC9jM@1ZpTg"

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/login', methods=['GET', 'POST'])
def login():
    usuarios = users.get.all()
    entregadores = Load.deliverers_list()
    administradores = Load.administrators_list()

    if request.method == "POST":
        cpf = request.form["cpf"]
        password = request.form["password"]

        for ID, Data in usuarios.items():
            if ID == cpf and Data["password"] == password:
                session["username"] = Data["nome"]
                session["cpf"] = cpf

                if cpf in entregadores:
                    session["entregador"] = True

                if cpf in administradores:
                    session["adm"] = True

                return redirect(url_for("index"))
        return render_template("login.html")
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":    
        usuario = Load.users_general_list()
        
        cpf = request.form["cpf"]
        email = request.form["email"]
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        senha = request.form["password"]
        entregador = bool(request.form["entregador"])
        
        if not cpf in usuario:
            users.create(cpf,email,nome,telefone,senha)
            
            if entregador:
                users.set_as.deliverer(cpf)
                
            return redirect(url_for("index"))
        
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("entregador", None)
    session.pop("adm", None)
    session.pop("cpf", None)
    
    return redirect(url_for("login"))

@app.route('/client')
def client():
    client_cpf = session["cpf"]
    
    deliveriyng = deliverys.get.by_client.deliverying(client_cpf)
    delivered = deliverys.get.by_client.delivered(client_cpf)
    
    print(deliveriyng)
        
    return render_template("clientInterface.html",deliveriyng=deliveriyng,delivered=delivered)

@app.route('/createdelivery', methods=['GET', 'POST'])
def createdelivery():
    if request.method == "POST":
        cliente = session['cpf']
        destinatario = request.form["destinatario"]
        descricao = request.form["descricao"]
        valor = request.form["valor"]
        
        deliverys.create(cliente,destinatario,descricao,valor)
        
        
        return redirect(url_for("client"))
        
    return render_template("create_delivery.html")



if __name__ == '__main__':
    app.run(debug=True)
    
    
'''
Testando Bernardo
'''