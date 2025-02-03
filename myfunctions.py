import json
import random
import requests

def load_json(file_path):
    with open(file_path, 'r') as arquivo:
        return json.load(arquivo)

def save_json(file_path, data):
    with open(file_path, 'w') as arquivo:
        json.dump(data, arquivo, indent=4)

class Save():
    def users_general_list(update):
        save_json('database/usuarios.json', update)
        

    def administrators_list(update):
        save_json('database/administradores.json', update)

    def commons_list(update):
        save_json('database/comuns.json', update)
    
    def deliverers_list(update):
        save_json('database/entregadores.json', update)

    def deliverys_list(update):
        save_json('database/entregas.json', update)

class Load():
    def users_general_list():
        return load_json('database/usuarios.json')
    
    def administrators_list():
        return load_json('database/administradores.json')

    def commons_list():
        return load_json('database/comuns.json')

    def deliverers_list():
        return load_json('database/entregadores.json')

    def deliverys_list():
        return load_json('database/entregas.json')




class deliverys():
    def create(cliente,destinatario,descrição):
        entregas = Load.deliverys_list()
        
        entregadores = Load.deliverers_list()
        
        entregador = random.choice(entregadores)
        while cliente == entregador:
            entregador = random.choice(entregadores)
        
        id = len(entregas)

        nova_entrega = {
            "status": "deliverying",
            "cliente": cliente,
            "destinatario": destinatario,
            "descricao": descrição,
            "entregador": entregador,
            "id": id
        }

        entregas.append(nova_entrega)

        Save.deliverys_list(entregas)

        return id
    
    def update(id,entregador = '', status = '', cliente='', destinatario='', descricao=''):
        entregas = deliverys.get.all()

        if cliente:
            entregas[id]["cliente"] = cliente

        if destinatario:
            entregas[id]["destinatario"] = destinatario

        if descricao:
            entregas[id]["descricao"] = descricao

        if status:
            entregas[id]["status"] = status

        if entregador:
            entregas[id]["entregador"] = entregador
            

        Save.deliverys_list(entregas)

        return entregas[id]
    
    def delete(id):
        entregas = deliverys.get.all()

        entregas.pop(id)

        Save.deliverys_list(entregas)
    
    class get():
        class by_client():
            def all(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if i["cliente"] == user_cpf:
                        S.append(i)
                return S

            def deliverying(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "deliverying"):
                        S.append(i)
                return S
            
            def delivered(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "delivered"):
                        S.append(i)
                return S
                    
            def confirmed(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["cliente"] == user_cpf) and (i["status"] == "confirmed"):
                        S.append(i)
                return S

        class by_deliverer():
            def all(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if i["entregador"] == user_cpf:
                        S.append(i)
                return S

            def deliverying(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "deliverying"):
                        S.append(i)
                return S
            
            def delivered(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "delivered"):
                        S.append(i)
                return S
            
            def confirmed(user_cpf):
                entregas = Load.deliverys_list()
                S = []
                for i in entregas:
                    if (i["entregador"] == user_cpf) and (i["status"] == "confirmed"):
                        S.append(i)
                return S

        def all():
            return Load.deliverys_list()

    class process():
        def deliver(id):
            id = int(id)
            entregas = deliverys.get.all()

            entregas[id]['status'] = 'delivered'

            Save.deliverys_list(entregas)

            return entregas[id]
        
        def confirm(id):
            entregas = deliverys.get.all()

            entregas[id]['status'] = 'confirmed'

            Save.deliverys_list(entregas)

            return entregas[id]
        
        def refuse(id,old_entregador,cliente):
            entregadores = Load.deliverers_list()
            entregas = Load.deliverys_list()
            
            entregador = random.choice(entregadores)
            
            while cliente == entregador or old_entregador == entregador:
                entregador = random.choice(entregadores)
                
            entregas[id]["entregador"] = entregador
            
            Save.deliverys_list(entregas)
            
            return entregador
            
        
        def cancel(id):
            entregas = deliverys.get.all()

            entregas[id]['status'] = 'canceled'

            Save.deliverys_list(entregas)

class users():
    def create(cpf,email,nome,telefone,senha):
        usuarios = Load.users_general_list()

        if not cpf in usuarios:
            usuarios[cpf] ={
            "email": email,
            "nome": nome,
            "tel": telefone,
            "password": senha
            }

            Save.users_general_list(usuarios)

            return f"Usuário {nome} cadastrado com sucesso"
        
        return " este CPF já está cadastrado"
    
    def edit(cpf,email,nome,telefone,senha):
        usuarios = Load.users_general_list()
        
        if cpf in usuarios:
            new_data = {}
            
            if nome:
                new_data["nome"] = nome
            if email:
                new_data["email"] = email
            if telefone:
                new_data["tel"] = telefone
            if senha:
                new_data["password"] = senha

            
            
            usuarios[cpf] = new_data
                        
            Save.users_general_list(usuarios)
            
            return "Conta atualizada com sucesso"
        
        return "CPF não encontrado"
    
    def delete(cpf):
        usuarios = Load.users_general_list()
        
        s = usuarios.pop(cpf)
        
        Save.users_general_list(usuarios)
        
        return s
    
    class get():
        def all():
            return Load.users_general_list()
        
        def deliverers():

            entregadores = Load.deliverers_list()
            usuarios = Load.users_general_list()

            entregadores_dict = {cpf: usuarios[cpf] for cpf in entregadores if cpf in usuarios}

            return entregadores_dict
        
        def administrators():
            administradores = Load.administrators_list()  
            usuarios = Load.users_general_list()  

            adminis_dict = {cpf: usuarios[cpf] for cpf in administradores if cpf in usuarios}

            return adminis_dict

        def by_cpf(cpf):
            GL = Load.users_general_list()
            return GL[cpf]
        
        def username_by_cpf(cpf):
            GL = Load.users_general_list()
            username = GL[cpf]["nome"]
            return username
    
    class set_as():       
        def deliverer(cpf):
            entregadores = Load.deliverers_list()
            
            if not cpf in entregadores:
                entregadores.append(cpf)
                
                Save.deliverers_list(entregadores)
                
                return "now User is an Deliverer"
            
            return "User already on the deliverers list"

        
        def administrator(cpf):
            admins = Load.administrators_list()
            
            if not cpf in admins:
                admins.append(cpf)
                
                Save.administrators_list(admins)
                
                return "now User is an Administrator"
            
            return "User already on the Administrators list"
        
    class unset_as():
        def deliverer(cpf):
            entregadores = Load.deliverers_list()
            
            if cpf in entregadores:
                entregadores.remove(cpf)
                Save.deliverers_list(entregadores)
                return "User isn't anymore an Deliverer"
            return "User not found in Deliverers list"
        
        def administrator(cpf):
            admins = Load.administrators_list()
            
            if cpf in admins:
                admins.pop(cpf)
                Save.deliverers_list(admins)
                return "User isn't anymore an Admin"
            return "User not found in Admins list"
        


def get_adress_by_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"error":"CEP invalido"}