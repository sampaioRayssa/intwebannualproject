from flask import *
from myfunctions import *

app = Flask(__name__)

app.secret_key = "f8X$wLk2V#bQ!zC9jM@1ZpTg"

@app.route("/")
def index():
    return render_template("index.html",session=session)



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
        
    return render_template("login.html",session=session)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":    
        usuario = Load.users_general_list()
        
        cpf = request.form["cpf"]
        email = request.form["email"]
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        senha = request.form["password"]
        entregador = request.form.get('entregador') == 'on'
        
        if not cpf in usuario:
            users.create(cpf,email,nome,telefone,senha)
            
            if entregador:
                users.set_as.deliverer(cpf)
                
            return redirect(url_for("index"))
        
    return render_template("signup.html",session=session)

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
            
    return render_template("clientInterface.html",deliveriyng=deliveriyng,delivered=delivered,session=session)

@app.route('/createdelivery', methods=['GET', 'POST'])
def createdelivery():
    if request.method == "POST":
        cliente = session['cpf']
        destinatario = request.form["destinatario"]
        descricao = request.form["descricao"]
        valor = request.form["valor"]
        
        deliverys.create(cliente,destinatario,descricao,valor)
        
        
        return redirect(url_for("client"))
        
    return render_template("create_delivery.html",session=session)

@app.route('/deliverer', methods=['GET','POST'])
def deliverer():
    user_cpf = session["cpf"]
    
    deliveriyng = deliverys.get.by_deliverer.deliverying(user_cpf)
    delivered = deliverys.get.by_deliverer.delivered(user_cpf)
    confirmed = deliverys.get.by_deliverer.confirmed(user_cpf)
    
    return render_template("deliverInterface.html",deliveriyng=deliveriyng,delivered=delivered,confirmed=confirmed,session=session)

@app.route('/deliver', methods=['POST'])
def deliver():
    Id = request.form["id"]
    
    deliverys.process.deliver(Id)
    
    return redirect(url_for("deliverer"))

@app.route('/confirm', methods=['POST'])
def confirm():
    Id = int(request.form["id"])
    
    deliverys.process.confirm(Id)
    
    return redirect(url_for("client"))

@app.route("/editprofile/<cpf>", methods=['GET', 'POST'])
def editprofile(cpf):
    if "adm" not in session and cpf != session.get("cpf"):
        abort(401)

    contas = Load.users_general_list()

    if cpf not in contas:
        abort(404)

    conta = users.get.by_cpf(cpf)
    if request.method == "POST":
        
        email = request.form["email"]
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        senha = request.form["password"]
        
        entregador = request.form.get("entregador") == 'on'
        admin = request.form.get("admin") == 'on'
        
        users.edit(cpf,email,nome,telefone,senha)
        
        contas = Load.users_general_list()
        
        if entregador:
            users.set_as.deliverer(cpf)
            session['entregador'] = True
        else:
            users.unset_as.deliverer(cpf)
            session['entregador'] = False
            
        if admin:
            users.set_as.administrator(cpf)
            session['adm'] = True
        else:
            users.unset_as.administrator(cpf)
            session['adm'] = False

            
        Save.users_general_list(contas)
            
        return redirect(url_for("index"))
    
    ent = False
    if cpf in Load.deliverers_list():
        ent = True
        
    adm = False
    if cpf in Load.administrators_list():
        adm = True

    return render_template("editProfile.html",session=session,cpf=cpf,conta=conta,ent=ent,adm=adm)
    

@app.route("/editdelivery/<eID>", methods=['GET', 'POST'])
def editdelivery(eID):
    eID = int(eID)
    entregas = Load.deliverys_list()
    entrega = entregas[eID]
    
    if "adm" in session:
        user = "adm"
        
    elif entrega["cliente"] == session["cpf"]:
        user = "cliente"
            
    elif entrega["entregador"] == session["cpf"]:
        user = "entregador"
    
    else:
        abort(401)
        
    if request.method == "POST":
        status = request.form["status"]
        cliente = request.form["cliente"]
        destinatario = request.form["destinatario"]
        descricao = request.form["descricao"]
        valor = request.form["valor"]
        entregador = request.form["entregador"]
        
        deliverys.update(eID,entregador,status,cliente,destinatario,descricao,valor)

        
        return redirect(url_for("index"))
    
    
    return render_template("editDelivery.html",session=session, user=user, entrega=entrega, eID=eID)
    
    
            
            
    


if __name__ == '__main__':
    app.run(debug=True)